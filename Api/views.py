from rest_framework.generics import (
        ListAPIView, 
        RetrieveAPIView,
        DestroyAPIView,
        UpdateAPIView,
        CreateAPIView
        )
from users.models import Student,Subject
from .serializers import (StudentSerializer,
                          StudentDetailSerializer,
                          SubjectCreateSearilizer,
                          StudentLoginSerializer,
                          )
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny
from django.db.models import Q
from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK,HTTP_400_BAD_REQUEST



class StudentAPIView(ListAPIView):
    serializer_class = StudentSerializer
    
    def get_queryset(self,*args,**kwargs):
        queryset_list = Student.objects.all()
        query = self.request.GET.get('q')
        if query:
            queryset_list = queryset_list.filter(
                    Q(student_id__iexact=query)|
                    Q(first_name__iexact=query)
                    ).distinct()
        return queryset_list

class StudentLoginView(APIView):
    permission_class = [AllowAny]
    serializer_class = StudentLoginSerializer
    
    def post(self,request,*args,**kwargs):
        
        data = self.request.data
        serializer = StudentLoginSerializer(data=data)
        
        if serializer.is_valid(raise_exception =True):
            new_data = serializer.data        
            
            return Response(new_data,status=HTTP_200_OK)
        return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)
     
        
        
class StudentDetailView(RetrieveAPIView):
    
    queryset = Student.objects.all()
    serializer_class = StudentDetailSerializer
    lookup_field = 'pk'
    permission_classes = [IsAdminUser]

class StudentUpdateView(UpdateAPIView):
    
    queryset = Student.objects.all()
    serializer_class = StudentDetailSerializer
    lookup_field = 'pk'
    permission_classes = [IsAuthenticated]

class StudentDeleteView(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentDetailSerializer
    lookup_field = 'pk'    
    
class SubjectCreateView(CreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectCreateSearilizer
    
