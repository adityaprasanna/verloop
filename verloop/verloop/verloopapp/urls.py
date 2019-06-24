from django.urls import path
from .api import views

urlpatterns = [
    path('repos', views.OrgViewSet.as_view(), name='OrgViewSet'),
]