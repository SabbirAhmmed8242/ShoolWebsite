from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='Home'),
    path('apply/', views.Apply_student, name='NewApply'),
    path('students/', include('Students.urls')),
    path('teachers/', include('Teachers.urls')),
    path('Result/', include('Results.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
