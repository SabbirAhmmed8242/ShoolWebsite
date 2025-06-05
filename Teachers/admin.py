from django.contrib import admin
from . models import secret_number_and_NID, teacher_login,TeacherDatas,NewApplyStudent

admin.site.register(secret_number_and_NID)
admin.site.register(teacher_login)
admin.site.register(TeacherDatas)
admin.site.register(NewApplyStudent)

# Register your models here.
