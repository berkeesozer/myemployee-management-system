from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.login_view, name='login'),
    path('home/', views.home, name='home'),
    path('employees/', views.employee_list, name='employee_list'),
    path('add/', views.add_employee, name='add_employee'),
    path('employee/details/', views.employee_details, name='employee_details'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)