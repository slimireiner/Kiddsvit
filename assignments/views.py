from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from assignments.models import TaskProgress, Course, Task
from assignments.serializers import TaskStartSerializer, AddCourseSerializer
from accounts.models import Children


@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def assign_course(request):
    serializers = AddCourseSerializer(data=request.data)
    if serializers.is_valid():
        course = Course.objects.filter(id=serializers.data['course_id']).first()
        child = Children.objects.filter(parent_id=request.user.pk, id=serializers.data['children_id']).first()
        child.assign_to_course(course=course)
        return Response(status=200)
    else:
        return Response(status=304)


@csrf_exempt
@api_view(['POST'])
def start_task(request):
    serializers = TaskStartSerializer(data=request.data)
    if serializers.is_valid():
        children = Children.objects.filter(id=serializers.data['children_id']).first()
        task = Task.objects.filter(id=serializers.data['task_id']).first()
        progress = TaskProgress.objects.filter(children=children, task=task).first()
        progress.change_status_task(status='in_progress')
        return Response(status=200)
    else:
        return Response(status=400)


@csrf_exempt
@api_view(['POST'])
def add_score_end_task(request):
    serializers = TaskStartSerializer(data=request.data)
    if serializers.is_valid():
        children = Children.objects.filter(id=serializers.data['children_id']).first()
        task = Task.objects.filter(id=serializers.data['task_id']).first()
        progress = TaskProgress.objects.filter(children=children, task=task, task_status='in_progress').first()
        progress.change_status_task(status='done')
        return Response(status=200)
    else:
        return Response(status=400)
