from django.db import models
from django.db.models import fields
from rest_framework.utils import model_meta
from users.models import CustomUser
from rest_framework import serializers

from .models import Platform, Tag, SolvedProblem, Problem


class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class SolvedProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolvedProblem
        fields = ['solved_count']


class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = ['link', 'title', 'tags', 'platform', 'notes']

