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
        fields = ['id', 'link', 'title', 'tags', 'platform', 'notes']



class CreateProblemSerializer(serializers.ModelSerializer):
    email = serializers.CharField()
    class Meta:
        model = Problem
        fields = ['email', 'link', 'title', 'tags', 'platform', 'notes', 'solved']

    def save(self, **kwargs):
        try:
            user = CustomUser.objects.get(email=self.validated_data['email'])

            p = Problem.objects.create(
                linked_user=user, 
                link=self.validated_data['link'],
                title = self.validated_data['title'],
                platform = self.validated_data['platform'],
                notes = self.validated_data['notes'],
                solved = self.validated_data['solved'],
            )
            for tag in self.validated_data['tags']:
                p.tags.add(tag)
            return p
        except:
            return None
