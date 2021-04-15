import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db import IntegrityError

from mysite.serializers import *
from orientation.models import Project, User, ProjectMentor, ProjectMentee
from rest_framework.viewsets import ModelViewSet

import logging
logger = logging.getLogger(__name__)


def index(request):
    return HttpResponse("Hello, world.")


class TaskViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = TaskSerializer
    logger.info('Projects being accessed!')
    '''
    /tasks API END POINT
    '''
    @action(methods=['get'], detail=True)
    def mentees(self, request, pk=None):
        """
        /tasks/{id}/mentees API END POINT
        """
        query_ans = ProjectMentee.objects.filter(project_id=pk)
        result = ProjectMenteeSerializer(query_ans, many=True)
        return Response(result.data)

    @action(methods=['get'], detail=True)
    def mentors(self, request, pk=None):
        """
        /tasks/{id}/mentors API END POINT
        """
        query_ans = ProjectMentor.objects.filter(project_id=pk)
        result = ProjectMentorSerializer(query_ans,many=True)
        return Response(result.data)


class ProjectMentorViewSet(ModelViewSet):
    queryset = ProjectMentor.objects.all()
    serializer_class = ProjectMentorSerializer
    logger.info('Project mentor info being accessed!')


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    logger.info('Users info being accessed')
    '''
    /users API End point
    '''
    @action(methods=['get'], detail=True)
    def mentor_projects(self, request, pk=None):
        """
        /users/{id}/mentor_projects/
        """
        query_ans = ProjectMentor.objects.filter(mentor_id=pk)
        result = ProjectMentorSerializer(query_ans, many=True)
        return Response(result.data)

    @action(methods=['get'], detail=True)
    def mentee_projects(self, request, pk=None):
        """
        /users/{id}/mentee_projects/
        """
        query_ans = ProjectMentee.objects.filter(mentee_id=pk)
        result = ProjectMenteeSerializer(query_ans, many=True)
        return Response(result.data)

    @action(methods=['get'], detail=True)
    def mentees(self, request, pk=None):
        """
        /users/{id}/mentees/
        """
        query_ans = MentorMentee.objects.filter(mentor_id=pk)
        result = MentorMenteeSerializer(query_ans, many=True)
        return Response(result.data)


class ProjectMenteeViewSet(ModelViewSet):
    logger.info('Project mentees info being accessed!')
    queryset = ProjectMentee.objects.all()
    serializer_class = ProjectMenteeSerializer


class MentorMenteeViewSet(ModelViewSet):
    logger.info('Mentor and mentees info being accessed')
    queryset = MentorMentee.objects.all()
    serializer_class = MentorMenteeSerializer


@csrf_exempt
def get_mentees(request, mentor_id):
    try:
        mentee_ids = MentorMentee.objects.values_list('mentee_id').filter(mentor_id = mentor_id)
    except IntegrityError as e:
        response = {"message": e.message}
        return HttpResponse(json.dumps(response), status=400)

    result = []
    response = {}
    for mentee_id in mentee_ids:
        result.append(mentee_id)
    response["Mentee_IDS"] = result
    return JsonResponse(response, safe=False)


@csrf_exempt
def get_projects(request, mentor_id):
    try:
        project_ids = ProjectMentor.objects.values_list('project_id').filter(mentor_id = mentor_id)
    except IntegrityError as e:
        response = {"message": e.message}
        return HttpResponse(json.dumps(response), status=400)
    result = []
    response = {}
    for project_id in project_ids:
        result.append(project_id)
    response["Project_IDS"] = result
    return JsonResponse(response, safe=False)



@csrf_exempt
def get_users(request, project_id):
    try:
        mentor_ids = ProjectMentor.objects.values_list('mentor_id').filter(project_id= project_id)
        mentee_ids = ProjectMentee.objects.values_list('mentee_id').filter(project_id=project_id)
    except IntegrityError as e:
        response = {"message": e.message}
        return HttpResponse(json.dumps(response), status=400)
    response_1 = []
    response_2 = []
    response = {}
    for mentor_id in mentor_ids:
        response_1.append(mentor_id)
    for mentee_id in mentee_ids:
        response_2.append(mentee_id)
    response["Mentor_IDS"] = response_1
    response["Mentee_IDS"] = response_2
    return JsonResponse(response, safe=False)
