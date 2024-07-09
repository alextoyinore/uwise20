from rest_framework import serializers
from .models import *
from utils.funcs import hash_password, strip_sc


class UserSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()
    slug = serializers.SerializerMethodField()
    user_password = serializers.SerializerMethodField()

    class Meta:
        model = User
        exclude = ['password']

    def get_token(self, obj):
        token, created = Token.objects.get_or_create(user=obj)
        return token.key
    
    def get_slug(self, obj):
        username = obj.email.split('@')[0]
        username = strip_sc(username)
        return f'{username}{obj.id}'
    
    def get_user_password(self, obj):
        if obj.is_admin or obj.is_superadmin:
            return hash_password(obj.password)


class InstructorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Instructor
        fields = '__all__'
        depth = 1


class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
        depth = 1


class RequestSerializer(serializers.HyperlinkedModelSerializer):
    slug = serializers.SerializerMethodField()

    class Meta:
        model = Request
        fields = '__all__'
        depth = 1

    def get_slug(self, obj):
        return strip_sc(obj.title)


class CategorySerializer(serializers.ModelSerializer):
    slug = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = '__all__'

    def get_slug(self, obj):
        return strip_sc(obj.title)


class JobSerializer(serializers.HyperlinkedModelSerializer):
    slug = serializers.SerializerMethodField()

    class Meta:
        model = Job
        fields = '__all__'
        depth = 1

    def get_slug(self, obj):
        return strip_sc(obj.title)


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    slug = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'
        depth = 1

    def get_slug(self, obj):
        return strip_sc(obj.title)


class BlogSerializer(serializers.HyperlinkedModelSerializer):
    slug = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = '__all__'
        depth = 1

    def get_slug(self, obj):
        return strip_sc(obj.title)

