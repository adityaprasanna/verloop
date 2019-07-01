from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
import requests
from operator import itemgetter

class OrgViewSet(APIView):
    def post(self, request, format=None):
        try:
            requested_data = json.loads(request.body)
            org_id = requested_data["org"]

            # URL for API call
            baseURL = "https://api.github.com/user/"
            getRepos = "/repos?simple=yes&per_page=100&page=1"
            fullURL = baseURL + org_id + getRepos

            # Make GET request to Github API and retrieve all repos of org
            allRepos = requests.get(fullURL)
            allReposJson = allRepos.json()
            
            while 'next' in allRepos.links.keys():
                allRepos=requests.get(allRepos.links['next']['url'])
                allReposJson.extend(allRepos.json())

            results = []

            for repo in allReposJson:
                repoData = {
                        "name": repo["name"],
                        "stars": repo["stargazers_count"]
                }
                results.append(repoData)

            # sort results based on stars and return only top 3 repositories
            results = sorted(results, key=itemgetter('stars'), reverse=True)[:3]

            responseData = {}
            responseData["results"] = results
            return Response(responseData,status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({"msg": "failed"}, status=status.HTTP_404_NOT_FOUND)


