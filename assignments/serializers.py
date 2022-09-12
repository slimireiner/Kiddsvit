from rest_framework import serializers

from accounts.models import AllScore
from assignments.models import Progress, Task


class CourseSerializer(serializers.ModelSerializer):
    pass


class ProgressSerializer(serializers.ModelSerializer):
    children = serializers.SlugRelatedField(slug_field='id', queryset=AllScore.objects, required=True)
    task = serializers.SlugRelatedField(slug_field='id', queryset=Task.objects, required=True)

    class Meta:
        model = Progress
        fields = ['children', 'task']

    def create(self, validated_data):
        progress = Progress.objects.create(
            children=validated_data['children'],
            task=validated_data['task']
        )
        return progress
