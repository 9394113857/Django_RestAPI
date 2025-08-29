from django.db import models
from django.contrib.auth.models import AbstractUser

class PatientDetails(models.Model):
    PATIENT_ID = models.CharField(max_length=20, primary_key=True)
    PATIENT_NAME = models.CharField(max_length=100)
    PATIENT_MAIL_ID = models.EmailField(unique=True)
    PATIENT_PHONE_NUMBER = models.CharField(max_length=15)
    PATIENT_PASSWORD = models.CharField(max_length=128)  # Store hashed passwords

    def __str__(self):
        return self.PATIENT_NAME

class AmbulanceBooking(models.Model):
    patient = models.ForeignKey(PatientDetails, on_delete=models.CASCADE)
    SITUATION_TYPE = models.CharField(max_length=100)
    AMB_TYPE = models.CharField(max_length=100)
    BASIC_OR_ADVANCE = models.CharField(max_length=100)
    CAUSE_TYPE = models.CharField(max_length=100)
    PRICE = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Ambulance Booking for {self.patient.PATIENT_NAME}"
