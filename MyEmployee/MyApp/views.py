from rest_framework import viewsets
from .models import Employee
from .serializers import EmployeeSerializer
from django.shortcuts import render
from .forms import EmployeeForm
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Admin

def employee_list(request):
    # Get sort parameters from request
    sort_by = request.GET.get('sort', 'last_name')  # Default sort by 'last_name'
    if sort_by not in ['last_name', 'start_date']: # or sort by 'start_date'
        sort_by = 'last_name'

    employees = Employee.objects.all().order_by(sort_by)

    # Pagination
    paginator = Paginator(employees, 10)  # Show 10 employees per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'sort_by': sort_by,
    }
    return render(request, 'employee_list.html', context)

def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Employee has been added successfully!')
            return render(request, 'add_employee.html', {'form': form})
    else:
        form = EmployeeForm()
    return render(request, 'add_employee.html', {'form': form})

def employee_details(request):
    employee_id = request.GET.get('id')
    employee = get_object_or_404(Employee, id=employee_id)
    return render(request, 'employee_details.html', {'employee': employee})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authentication
        if Admin.objects.filter(username=username, password=password).exists():
            # Add success message and redirect to home page
            messages.success(request, 'Login successful!')
            return render(request, 'home.html')
        else:
            # Add error message if credentials are incorrect
            messages.error(request, 'Invalid ID or Password')

    return render(request, 'login.html')



class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer