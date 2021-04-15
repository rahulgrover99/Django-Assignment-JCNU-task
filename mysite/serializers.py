from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from orientation.models import *


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"


class ProjectMentorSerializer(ModelSerializer):
    class Meta:
        model = ProjectMentor
        fields = "__all__"


class ProjectMenteeSerializer(ModelSerializer):
    class Meta:
        model = ProjectMentee
        fields = "__all__"


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class MentorMenteeSerializer(ModelSerializer):
    class Meta:
        model = MentorMentee
        fields = "__all__"
