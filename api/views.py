import django
import requests
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from api.models import Repo, Owner
from api.serializers import RepoSerializer


def create_data_in_db(url):
    """Get json data from url and collect to the database."""
    r = requests.get(url)
    data_list = r.json()
    for data in data_list:
        try:
            owner = Owner.objects.get(login=data['owner']['login'], node_id=data['owner']['node_id'])
        except Owner.DoesNotExist:
            owner = Owner.objects.create(login=data['owner']['login'], node_id=data['owner']['node_id'])
        try:
            Repo.objects.create(id=data['id'], node_id=data['node_id'], name=data['name'],
                                full_name=data['full_name'], private=data['private'], owner=owner,
                                html_url=data['html_url'], description=data['description'])
        except django.db.utils.IntegrityError:
            pass


@api_view(('GET',))
@renderer_classes((JSONRenderer,))
def get_repos_by_user(request, username):
    """Get repositories by username"""
    url = f'https://api.github.com/users/{username}/repos'
    create_data_in_db(url)
    query = Repo.objects.filter(owner__login=username)
    serializer = RepoSerializer(data=query, many=True)
    serializer.is_valid()
    return Response(serializer.data)


@api_view(('GET',))
@renderer_classes((JSONRenderer,))
def get_firsts_repos(request):
    """Get 50 repositories from github"""
    url = 'https://api.github.com/repositories'
    create_data_in_db(url)
    query = Repo.objects.all()[:50]
    serializer = RepoSerializer(data=query, many=True)
    serializer.is_valid()
    return Response(serializer.data)


@api_view(('GET',))
@renderer_classes((JSONRenderer,))
def get_repository_by_id(request, pk):
    """Get repository info by id"""
    repo = Repo.objects.get(id=pk)
    serializer = RepoSerializer(repo)
    return Response(serializer.data)


@api_view(('POST',))
@renderer_classes((JSONRenderer,))
def update_repository(request, pk):
    """Update repository information by id"""
    repo = Repo.objects.get(id=pk)
    serializer = RepoSerializer(instance=repo, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(('POST',))
@renderer_classes((JSONRenderer,))
def create_repository(request):
    """Create repository"""
    serializer = RepoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
@renderer_classes((JSONRenderer,))
def delete_repository(request, pk):
    """Delete repository by id"""
    repo = Repo.objects.get(id=pk)
    repo.delete()
    return Response('Repository successfully deleted!')
