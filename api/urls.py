from django.urls import path
from .views import *

urlpatterns = [
    path('token/', view=obtain_auth_token),
    path('users/', view=UserCreateListView.as_view(), name='users'),
    path('user/<int:pk>', view=UserDetailView.as_view(), name='user'),
    path('instructors/', view=InstructorCreateListView.as_view(), name='instructors'),
    path('instructor/<int:pk>', view=InstructorDetailView.as_view(), name='instructor'),
    path('clients/', view=ClientCreateListView.as_view(), name='clients'),
    path('client/<int:pk>', view=ClientDetailView.as_view(), name='client'),
    path('requests/', view=RequestCreateListView.as_view(), name='requests'),
    path('request/<int:pk>', view=RequestDetailView.as_view(), name='request'),
    path('categories/', view=CategoryCreateListView.as_view(), name='categories'),
    path('category/<int:pk>',view=CategoryDetailView.as_view(), name='category'),
    path('jobs/', view=JobCreateListView.as_view(), name='jobs'),
    path('job/<int:pk>',view=JobDetailView.as_view(), name='job'),
    path('courses/', view=CourseCreateListView.as_view(), name='courses'),
    path('course/<int:pk>', view=CourseDetailView.as_view(), name='course'),
    path('blogs/', view=BlogCreateListView.as_view(), name='blogs'),
    path('blog/<int:pk>', view=BlogDetailView.as_view(), name='blog'),
]
