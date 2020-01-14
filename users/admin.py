from django.contrib import admin
from .models import Student, Subject, Mark


admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Mark)

admin.site.site_header = "My University admin"
admin.site.site_title = "University Admin Portal"
admin.site.index_title = "Welcome to Unviversity Admin Portal"

