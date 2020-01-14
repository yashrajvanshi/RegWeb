from rest_framework.serializers import (
        ModelSerializer,
        SerializerMethodField,
        CharField,
        ValidationError
        )

from users.models import Student,Subject,User


class StudentSerializer(ModelSerializer):
    user = SerializerMethodField()
    class Meta:
        model = Student
        fields =[
                'user',
                'student_id',
                'first_name',
                'last_name',
                'subject',
                ]
        
    def get_user(self,obj):
        return str(obj.user.username)

class StudentLoginSerializer(ModelSerializer):
    token = CharField(allow_blank=True,read_only=True)
    username = CharField()
    
    class Meta:
        model = User
        
        fields=[
                'username',
                'password',
                'token',
                ]
        extra_kwargs = {"password":{"write_only": True}}
        
    def validate(self,data):
        user_obj = None
        username = data.get("username",None)
        password = data.get("password",None)
        print(data,"0")
        if not username:
            raise ValidationError("Username is not Correct")
        print(data,"1")    
        user = User.objects.filter(username=username).distinct()
        
        if user.exists() and user.count() ==1:
            user_obj = user.first()
        
        else:
            raise ValidationError("This username is not valid")
        print(data,"3")    
        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError("Incorrect Credentials please try again")
                
        print(data,"4")        
        
        data["token"] = "Some Random token"
        
        print(data,"5")
        return data

                    
class StudentDetailSerializer(ModelSerializer):
    
    class Meta:
        model = Student
        fields =[
                'id',
                'student_id',
                'first_name',
                'last_name',
                'subject',
                ]
        
class SubjectCreateSearilizer(ModelSerializer):
    class Meta:
        model = Subject
        fields=[
                'subject_name',
                ]