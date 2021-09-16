from django.urls import path

from api.views import get_repos_by_user, get_firsts_repos, update_repository, create_repository, delete_repository, \
    get_repository_by_id

urlpatterns = [
    path('repos/', get_firsts_repos),
    path('get-repository/<int:pk>/', get_repository_by_id),
    path('update-repository/<int:pk>/', update_repository),
    path('delete-repository/<int:pk>/', delete_repository),
    path('create-repository/', create_repository),
    path('<str:username>/', get_repos_by_user),

]
