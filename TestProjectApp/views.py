from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Inspection, Condition
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Inspection, Condition

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

@login_required
def home_view(request):
    inspections = Inspection.objects.all()

    return render(request, 'home.html', {'username': request.user.username, 'inspections': inspections})

@login_required
def conditions_view(request, inspection_id):
    # Retrieve the inspection based on the ID
    inspection = get_object_or_404(Inspection, id=inspection_id)

    # Fetch all conditions associated with the inspection (foreign key)
    conditions = Condition.objects.filter(Inspection_id=inspection.id)

    return render(request, 'conditions.html', {
        'username': request.user.username,  # Logged-in username
        'inspection': inspection,          # The requested inspection
        'conditions': conditions           # Related conditions
    })


def logout_view(request):
    logout(request)
    return redirect('login')
