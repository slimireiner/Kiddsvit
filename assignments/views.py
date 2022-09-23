import datetime
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from assignments.models import TaskProgress, Course, Task
from assignments.serializers import TaskStartSerializer, AddCourseSerializer
from accounts.models import ChildrenProfile


@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def assign_course(request):
    serializers = AddCourseSerializer(data=request.data)
    if serializers.is_valid():
        course = Course.objects.filter(id=serializers.data['course_id']).first()
        child = ChildrenProfile.objects.filter(Q(children_user__parent=request.user.pk) | Q(children_user_id=request.user.pk),
                                        id=serializers.data['children_id']).first()
        child.assign_to_course(course=course)
        return Response(status=200)
    else:
        return Response(status=304)


@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def start_task(request):
    serializers = TaskStartSerializer(data=request.data)
    if serializers.is_valid():
        print(request.user.pk)
        print(serializers.data['task_id'])
        children = ChildrenProfile.objects.filter(children_user_id=request.user.pk).first()
        task = Task.objects.filter(id=serializers.data['task_id']).first()
        progress = TaskProgress.objects.filter(children=children, task=task).first()
        print(progress)
        progress.created_ad = datetime.datetime.now()
        progress.change_status_task(status='in_progress')
        progress.save()
        return Response(status=200)
    else:
        return Response(status=400)


@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_score_end_task(request):
    serializers = TaskStartSerializer(data=request.data)
    if serializers.is_valid():
        children = ChildrenProfile.objects.filter(children_user_id=request.user.pk).first()
        if children:
            task = Task.objects.filter(id=serializers.data['task_id']).first()
            progress = TaskProgress.objects.filter(children=children, task=task, task_status='in_progress').first()
            progress.finished_ad = datetime.datetime.now()
            progress.change_status_task(status='done')
            if progress.is_all_tasks_done():
                course = children.course_rels.filter(course_id=progress.task.course_id).first()
                course.finish()
            progress.save()
            return Response(status=200)
    else:
        return Response(status=400)
