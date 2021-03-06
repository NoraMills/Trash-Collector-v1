from django.http import HttpResponse
from django.shortcuts import render
from django.apps import apps
from .models import Employee

# Create your views here.

# TODO: Create a function for each path created in employees/urls.py. Each will need a template as well.


def index(request):
    # This line will get the Customer model from the other app, it can now be used to query the db for Customers
    Customer = apps.get_model('customers.Customer')
    return render(request, 'employees/index.html')


def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        user = request.user
        zipcode = request.POST.get('zipcode')

        new_employee = Employee(name=name, user=user, zipcode=zip)
        new_employee.save()
        return index(request)
    else:
        return render(request, 'employees/create.html')

def confirmpickup(request):
    user = request.user
    if request.method == 'POST':
        confirmed = request.POST.get('confirmed')
    else:
        return render(request, 'employees/confirmpickup.html')