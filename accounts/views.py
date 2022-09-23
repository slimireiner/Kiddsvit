from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
import secrets
from accounts.models import User, ChildrenProfile, AllScore, ShareToken
from accounts.serializers import RegisterSerializer, CreateTokenSerializer, \
    GetStatisticSerializer, RegisterChildrenSerializer
from kiddsvit.settings import DOMEIN_NAME


# Create your views here.
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class TokenCreate(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = CreateTokenSerializer


@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def child_add(request):
    if User.objects.filter(id=request.user.pk, is_children=None):
        serializer = RegisterChildrenSerializer(data=request.data)
        if serializer.is_valid():
            children_user = User.objects.create(
                username=serializer.validated_data['username'],
                email=serializer.validated_data['email'],
                is_children=True,
                parent_id=request.user.pk
            )
            children_user.set_password(serializer.validated_data['password'])
            children_user.save()
            children = ChildrenProfile.objects.create(
                age=serializer.validated_data['age'],
                gender=serializer.validated_data['gender'],
                children_user=children_user)
            AllScore.objects.create(kid=children)
            return Response(status=200)


@csrf_exempt
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_list_score(request):
    queryset = ChildrenProfile.objects.filter(
        Q(children_user_id=request.user)
        | Q(children_user__parent=request.user)
    ).first()
    children = AllScore.objects.filter(
        Q(kid__children_user__parent=queryset.children_user.parent_id)
        | Q(kid__children_user=queryset.children_user)
    ).all()
    stats = []
    for child in children:
        stats.append({'name': child.kid.children_user.username,
                      'score': child.total_score})
    return Response(stats)


@csrf_exempt
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def make_token(request, children_id: int):
    serializer = GetStatisticSerializer(data={'children_id': children_id})
    if serializer.is_valid():
        children = ChildrenProfile.objects.filter(id=serializer.validated_data['children_id'],
                                                  children_user__parent=request.user.pk)
        token = ShareToken.objects.create(children=children.first(), token=secrets.token_urlsafe())
        return Response({'url': f'{DOMEIN_NAME}accounts/get_children_by_token/?token={token.token}'})
    else:
        return Response(status=304)


@csrf_exempt
@api_view(['GET'])
def get_static_token(request):
    children = ShareToken.objects.filter(token=request.GET.get('token'))
    queryset = AllScore.objects.filter(kid=children.first().children).first()
    return Response(queryset.get_score_token(queryset.kid_id))
