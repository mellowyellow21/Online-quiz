from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from admin_user import urls
from quiz import urls
from admin_user.views import admin_index, user_logout
from student.views import student_index
from django.conf.urls import url
from . import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(('admin_user.urls'),namespace='admin_user')),
    path('',include(('quiz.urls'),namespace='student')),
    path('admin-dashboard', admin_index, name='admin_index'),
    url('student-dashboard', student_index, name='student_index'),
    url(r'^logout/$', user_logout,name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)