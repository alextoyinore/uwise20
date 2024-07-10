from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import make_password
from utils.funcs import hash_password, strip_sc
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()
    # slug = serializers.SerializerMethodField()
    # username = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}


    def get_token(self, obj):
        token, created = Token.objects.get_or_create(user=obj)
        return token.key
    
    # def get_slug(self, obj):
    #     username = obj.email.split('@')[0]
    #     username = strip_sc(username)
    #     return f'{username}{obj.id}'
    
    # def get_username(self, obj):
    #     username = obj.email.split('@')[0]
    #     username = strip_sc(username)
    #     return f'{username}{obj.id}'
    
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])  # Hash the password
        initial_data = self.initial_data
        
        email = initial_data.get('email')
        username = email.split('@')[0]
        username = strip_sc(username)

        # Create Username
        validated_data['username'] = f'{username}{User.objects.count() + 1}'
        # Create Slug
        validated_data['slug'] = f'{username}{User.objects.count() + 1}'
        
        return super().create(validated_data)
    
    
    def update(self, instance, validated_data):
        if validated_data['account_type'] == 2 and not validated_data['school_name']:
            raise serializers.ValidationError('school nameosrequired for instructor accounts.')
        
        if validated_data['account_type'] == 3 and not validated_data['org_name']:
            raise serializers.ValidationError('organization name is required for client accounts.')
        
        return super().update(instance, validated_data)
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        
        # Modify fields based on account_type
        account_type = instance.account_type
        
        if account_type == 1:  # Student
            excluded_fields = [
                'school_name', 'school_logo', 'org_name', 'org_logo', 'org_city', 'org_state', 'org_country'
            ]
        elif account_type == 2:  # Instructor
            excluded_fields = [
                'org_name', 'org_logo', 'org_city', 'org_state', 'org_country'
            ]
        else:  # Client
            excluded_fields = [
                'school_name', 'school_logo'
            ]

        for field in excluded_fields:
            representation.pop(field, None)
        
        return representation


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
    
    def create(self, validated_data):
        initial_data = self.initial_data
        title = initial_data.get('title')
        validated_data['slug'] = f'{title}'
        return super().create(validated_data)


class JobSerializer(serializers.HyperlinkedModelSerializer):
    slug = serializers.SerializerMethodField()

    class Meta:
        model = Job
        fields = '__all__'
        depth = 1

    def get_slug(self, obj):
        return strip_sc(obj.title)
    
    def create(self, validated_data):
        # if not User.objects.get(pk=validated_data['client']).account_type == 3:
        #     raise serializers.ValidationError('You need a client account to post a job')
        return super().create(validated_data)


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

