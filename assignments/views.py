from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from assignments.models import Progress
from assignments.serializers import ProgressSerializer


class ChildrenAddCourse(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Progress.objects.all()
    serializer_class = ProgressSerializer
