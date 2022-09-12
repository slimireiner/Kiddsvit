import json

from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
import secrets
from accounts.models import User, Children, AllScore, ShareToken
from accounts.serializers import RegisterSerializer, CreateTokenSerializer, ChildSerializer, GetAllScoreSerializer
from kiddsvit.settings import DOMEIN_NAME


# Create your views here.
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class TokenCreate(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = CreateTokenSerializer


class ChildAdd(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ChildSerializer


@csrf_exempt
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_list_score(request):
    queryset = AllScore.objects.filter(kid__parent=request.user.pk)
    serializer = GetAllScoreSerializer(queryset, many=True)
    return Response(serializer.data)


@csrf_exempt
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def make_token(request, children_id: int):
    children = Children.objects.filter(parent_id=request.user.pk, id=children_id)
    token = ShareToken.objects.create(children=children.first(), token=secrets.token_urlsafe())
    return Response({'url': f'{DOMEIN_NAME}account/{token.token}'})

