from typing import Iterable
from django.db import models

# Create your models here.

class User(models.Model):
    email = models.EmailField(max_length=250, null=False, unique=True)
    username = models.CharField(max_length=100, null=True, unique=True)
    firstname = models.CharField(max_length=200, null=True)
    lastname = models.CharField(max_length=200, null=True)
    account_type = models.PositiveSmallIntegerField(default=1, choices={1:'student', 2: 'instructor', 3: 'client'})
    profile_image = models.URLField(null=True)
    bio = models.TextField(null=True)
    socials = models.JSONField(null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    nationality = models.CharField(max_length=200, null=True)
    date_joined = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)

    def __str__(self) -> str:
        return super().__str__()
    
    class Meta:
        db_table = 'Users'
        managed = True
        verbose_name = 'user'
        verbose_name_plural = 'users'


class Instructor(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=False)
    school_name = models.CharField(max_length=200, null=False)
    school_logo = models.URLField(null=True)
    date_created = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self) -> str:
        return super().__str__()

    class Meta:
        db_table = 'Instructors'
        managed = True
        verbose_name = 'instructor'
        verbose_name_plural = 'instructors'


class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=False)
    org_name = models.CharField(max_length=200, null=False)
    org_logo = models.URLField(null=True)
    org_city = models.CharField(max_length=200, null=False)
    org_state = models.CharField(max_length=200, null=False)
    org_country = models.CharField(max_length=200, null=False)


    def __str__(self) -> str:
        return super().__str__()
    
    class Meta:
        db_table = 'Clients'
        managed = True
        verbose_name = 'client'
        verbose_name_plural = 'clients'


class Request(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=False)
    title = models.CharField(max_length=200, null=False)
    slug = models.SlugField(unique=True)
    date_created = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self) -> str:
        return super().__str__()
    
    class Meta:
        db_table = 'Requests'
        managed = True
        verbose_name = 'request'
        verbose_name_plural = 'requests'


class Category(models.Model):
    title = models.CharField(max_length=200, null=False)
    icon = models.URLField(null=True)
    date_created = models.DateTimeField(auto_now=False, auto_now_add=False)
    slug = models.SlugField(unique=True)


    def __str__(self) -> str:
        return super().__str__()
    
    class Meta:
        db_table = 'Categories'
        managed = True
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class Job(models.Model):
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    title = models.CharField(max_length=250, null=False)
    slug = models.SlugField(unique=True)


class Course(models.Model):
    instructor = models.ForeignKey(Instructor, on_delete=models.PROTECT, null=False)
    title = models.CharField(max_length=250, null=False)
    slug = models.SlugField(unique=True)


class Blog(models.Model):
    slug = models.SlugField(unique=True)

