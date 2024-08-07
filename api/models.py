from django.db import models

# Create your models here.

class User(models.Model):
    email = models.EmailField(max_length=250, null=False, unique=True)
    password = models.CharField(max_length=250, null=False)
    username = models.CharField(max_length=250, null=True, unique=True)
    firstname = models.CharField(max_length=250, null=True)
    lastname = models.CharField(max_length=250, null=True)
    account_type = models.PositiveSmallIntegerField(default=1, choices={1:'student', 2: 'instructor', 3: 'client'})
    profile_image = models.URLField(null=True)
    bio = models.TextField(null=True)
    socials = models.JSONField(null=True)
    city = models.CharField(max_length=250, null=True)
    state = models.CharField(max_length=250, null=True)
    nationality = models.CharField(max_length=250, null=True)
    date_joined = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    # Instructor Details
    school_name = models.CharField(max_length=250, null=True)
    school_logo = models.URLField(null=True)

    # Client Details
    org_name = models.CharField(max_length=250, null=True)
    org_logo = models.URLField(null=True)
    org_city = models.CharField(max_length=250, null=True)
    org_state = models.CharField(max_length=250, null=True)
    org_country = models.CharField(max_length=250, null=True)

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'
    is_anonymous = None
    is_authenticated = None

    def __str__(self) -> str:
        return super().__str__()
    
    class Meta:
        db_table = 'Users'
        managed = True
        verbose_name = 'user'
        verbose_name_plural = 'users'


class Category(models.Model):
    staff = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=250, null=False, unique=True)
    icon = models.URLField(null=True)
    description = models.TextField(null=True)
    date_created = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, null=True)

    def __str__(self) -> str:
        return super().__str__()
    
    class Meta:
        db_table = 'Categories'
        managed = True
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class Request(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250, null=False)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, null=True)
    slug = models.SlugField(unique=True, null=True)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return super().__str__()
    
    class Meta:
        db_table = 'Requests'
        managed = True
        verbose_name = 'request'
        verbose_name_plural = 'requests'


class Job(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, null=True)
    short_description = models.TextField(null=True)
    long_description = models.TextField()
    date_created = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, null=True)

    def __str__(self) -> str:
        return super().__str__()
    
    class Meta:
        db_table = 'Jobs'
        managed = True
        verbose_name = 'job'
        verbose_name_plural = 'jobs'


class Course(models.Model):
    title = models.CharField(max_length=250, unique=True)
    instructors = models.JSONField()
    categories = models.JSONField()
    price = models.DecimalField(max_digits=11, decimal_places=2)
    intro_video = models.URLField(null=True)
    short_description = models.TextField(null=True)
    long_description = models.TextField()
    skills_to_gain = models.JSONField(null=True)
    objectives = models.JSONField(null=True)
    classes = models.JSONField(null=True) # classes will contain class links, time, date and other information
    date_created = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, null=True)

    def __str__(self) -> str:
        return super().__str__()

    class Meta:
        db_table = 'Courses'
        managed = True
        verbose_name = 'course'
        verbose_name_plural = 'courses'


class Blog(models.Model):
    authors = models.JSONField(null=False)
    title = models.CharField(max_length=250, unique=True)
    excerpt = models.TextField()
    content = models.JSONField()
    categories = models.JSONField()
    date_published = models.DateTimeField(auto_now=True, auto_created=True)
    slug = models.SlugField(unique=True, null=True)

    def __str__(self) -> str:
        return super().__str__()
    
    class Meta:
        db_table = 'Blogs'
        managed = True
        verbose_name = 'blog'
        verbose_name_plural = 'blogs'


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.PROTECT, related_name='sender')
    reciever = models.ForeignKey(User, on_delete=models.PROTECT, related_name='reciever')
    content = models.JSONField()
    date = models.DateTimeField(auto_now=False)
    slug = models.SlugField(null=True)

    def __str__(self) -> str:
        return super().__str__()
    
    class Meta:
        db_table = 'Messages'
        managed = True
        verbose_name = 'message'
        verbose_name_plural = 'messages'


class CourseClass(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    objectives = models.JSONField(null=True)
    skills_to_learn = models.JSONField(null=True)
    banner = models.URLField(null=True)
    slug = models.SlugField(null=True)
    date_created = models.DateTimeField(auto_now=False)

    def __str__(self) -> str:
        return super().__str__()
    
    class Meta:
        db_table = 'CourseClasses'
        managed = True
        verbose_name = 'courseclass'
        verbose_name_plural = 'courseclasses'

