from users.models import CustomUser
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination

from .serializers import PlatformSerializer, TagSerializer, ProblemSerializer
from .models import Platform, Problem, Tag, SolvedProblem, UnsolvedProblem


class TagView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PlatfromView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        platform = Platform.objects.all()
        serializer = PlatformSerializer(platform, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CountProblemsView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        email = request.user.email
        user = CustomUser.objects.get(email=email)
        Solved_prob = SolvedProblem.objects.get(linked_user=user)
        unsolved = UnsolvedProblem.objects.get(linked_user=user)

        response = {
            'solved_total': Solved_prob.solved_count,
            'unsolved_total': unsolved.unsolved_count
        }

        problems = Solved_prob.solved_problems.all()
        
        for problem in problems:
            p_name = problem.platform.platform_name
            if p_name not in response:
                response[p_name] = 0
            response[p_name]+=1

        return Response(response)


class SolvedProblemsView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        email = request.user.email
        user = CustomUser.objects.get(email=email)
        solved_probs = SolvedProblem.objects.get(linked_user=user)
        problems = solved_probs.solved_problems.all()
        
        paginator = PageNumberPagination()
        results = paginator.paginate_queryset(problems, request)
        serializer = ProblemSerializer(results, many=True)
        
        return paginator.get_paginated_response(serializer.data)



class ProblemView(APIView):
    def get(self, request):
        pass

    def post(self, request):
        pass
    
    def put(self, reques):
        pass

    def delete(self, request):
        pass