from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        models = User
        fields = '__all__'


class InstructorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        models = Instructor
        fields = '__all__'
        depth = 1


class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        models = Client
        fields = '__all__'
        depth = 1


class RequestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        models = Request
        fields = '__all__'
        depth = 1


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        models = Category
        fields = '__all__'


class JobSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        models = Job
        fields = '__all__'
        depth = 1


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        models = Course
        fields = '__all__'
        depth = 1


class BlogSerializer(serializers.HyperlinkedModelSerializer):
    models = Blog
    fields = '__all__'
    depth = 1

    