from rest_framework import serializers

from accounts.models import Children
from assignments.models import TaskProgress, Task


class AddCourseSerializer(serializers.Serializer):
    children_id = serializers.IntegerField(required=True)
    course_id = serializers.IntegerField(required=True)


class TaskProgressSerializer(serializers.ModelSerializer):
    children = serializers.SlugRelatedField(slug_field='id', queryset=Children.objects, required=True)
    task = serializers.SlugRelatedField(slug_field='id', queryset=Task.objects, required=True)

    class Meta:
        model = TaskProgress
        fields = ['children', 'task']

    def create(self, validated_data):
        progress = TaskProgress.objects.create(
            children=validated_data['children'],
            task=validated_data['task']
        )
        return progress


class TaskStartSerializer(serializers.Serializer):
    children_id = serializers.IntegerField(required=True)
    task_id = serializers.IntegerField(required=True)