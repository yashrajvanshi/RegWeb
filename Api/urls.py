from django.urls import path
from .views import (
        StudentAPIView,
        StudentDetailView,
        StudentUpdateView,
        StudentDeleteView,
        SubjectCreateView,
        StudentLoginView,
        )
from rest_framework_jwt.views import obtain_jwt_token
 
urlpatterns = [
   path('student/',StudentAPIView.as_view(),name='list'),
   path('login/',StudentLoginView.as_view(),name='api-login'),
   path('student/<int:pk>/detail',StudentDetailView.as_view(),name='detail'),
   path('student/<int:pk>/detail-update',StudentUpdateView.as_view(),name='update'), 
   path('student/<int:pk>/detail-delete',StudentDeleteView.as_view(),name='delete'),
   path('subject/create',SubjectCreateView.as_view(),name='subject-create'),
   path('token/auth', obtain_jwt_token,name="auth"),
   
]


"""
curl -X POST -d "username=5867&password=amizonenetwork" http://localhost:8000/api/token/auth

curl -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjozLCJ1c2VybmFtZSI6IjU4NjciLCJleHAiOjE1NzQ0NDkyNjEsImVtYWlsIjoiIn0.nT0q5sOshaNBe3GA9CbW7rET9lwfqANcqM5gn1BzNtk" http://localhost:8000/api/student/8/detail


"""
