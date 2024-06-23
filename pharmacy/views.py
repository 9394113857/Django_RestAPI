from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password, check_password
from .models import PatientDetails, AmbulanceBooking
from django.contrib.auth.models import User


def new_user(request):
    if request.method == 'POST':
        # Retrieve data from request
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')

        # Perform necessary validation (you can customize this part)
        if not username or not email or not phone or not password:
            return JsonResponse({'message': 'Invalid input'}, status=400)

        # Create a new User object
        user = User.objects.create_user(username=username, email=email, password=password)

        # Create a new PatientDetails object
        patient = PatientDetails.objects.create(
            PATIENT_ID=user.username,  # Use username as PATIENT_ID
            PATIENT_NAME=username,
            PATIENT_MAIL_ID=email,
            PATIENT_PHONE_NUMBER=phone,
            PATIENT_PASSWORD=user.password
        )

        return JsonResponse({'message': 'User Registered Successfully'})
    return JsonResponse({'message': 'Invalid input'}, status=400)

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Authenticate user
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'User logged in successfully'})
        else:
            return JsonResponse({'message': 'Invalid credentials'}, status=401)

    return JsonResponse({'message': 'Invalid input'}, status=400)

def logout_view(request):
    logout(request)
    return JsonResponse({'message': 'User logged out successfully'})

@login_required
def restricted_view(request):
    return JsonResponse({'message': 'You are accessing a restricted view.'})

def book(request):
    if request.method == 'POST':
        # Check if user is logged in
        if request.user.is_authenticated:
            # Retrieve data from request
            # Perform necessary validation
            # Create a new AmbulanceBooking object
            # Save to the database
            return JsonResponse({'message': 'successfully inserted'})
        else:
            return JsonResponse({'message': 'User not logged in'}, status=401)
    return JsonResponse({'message': 'invalid parameters'}, status=400)

# Define other views similarly
