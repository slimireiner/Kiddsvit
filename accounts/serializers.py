import secrets

from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from accounts.models import User, Children, AllScore, ShareToken


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        extra_kwargs = {
            'username': {'required': True}
        }

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class CreateTokenSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(CreateTokenSerializer, cls).get_token(user)
        token['username'] = user.username
        return token


class ChildSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    parent = serializers.SlugRelatedField(slug_field='id', queryset=User.objects, required=True)
    age = serializers.IntegerField()
    gender = serializers.CharField()

    class Meta:
        model = Children
        fields = '__all__'

    def create(self, validated_data):
        child = Children.objects.create(
            name=validated_data['name'],
            parent=validated_data['parent'],
            age=validated_data['age'],
            gender=validated_data['gender'],
        )
        score = AllScore.objects.create(kid=child)
        score.save()
        return child


class GetAllScoreSerializer(serializers.ModelSerializer):
    kid = serializers.SlugRelatedField(slug_field='name', read_only=True)
    total_score = serializers.IntegerField()

    class Meta:
        model = AllScore
        fields = '__all__'


class GetStatisticTokenSerializer(serializers.ModelSerializer):
    kid = serializers.SlugRelatedField(slug_field='name', read_only=True)
    total_score = serializers.IntegerField()

    class Meta:
        model = AllScore
        fields = '__all__'


class GetStatisticSerializer(serializers.Serializer):
    children_id = serializers.IntegerField(required=True)