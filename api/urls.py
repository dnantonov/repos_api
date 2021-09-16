from django.urls import path

from api.views import get_repos_by_user, get_firsts_repos, update_repository

urlpatterns = [
    path('repos/', get_firsts_repos),
    path('update-repository/<int:pk>/', update_repository),
    path('<str:username>/', get_repos_by_user),

]
