from django.contrib import admin
from . models import Student_login_details,StudentDetails,StudentRegInfoAdmin,StudentRegLogin

admin.site.register(Student_login_details)
admin.site.register(StudentDetails)
admin.site.register(StudentRegInfoAdmin)
admin.site.register(StudentRegLogin)

# Register your models here.
