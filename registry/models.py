from django.db import models


class Contact(models.Model):
    id_number = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    # Gender Choices
    MALE = 'male'
    FEMALE = 'female'
    OTHER = 'other'
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
    )
    gender = models.CharField(
        max_length=25, choices=GENDER_CHOICES, default=MALE)
    # Contact Details
    contact_number = models.CharField(max_length=200)
    email = models.EmailField(blank=True)
    address = models.TextField()
    electricity_meter_number = models.CharField(max_length=200)
    water_meter_number = models.CharField(max_length=200)
    # employment details
    EMPLOYED = 'employed'
    UNEMPLOYED = 'unemployed'
    SELF_EMPLOYED = 'self_employed'
    EMPLOYMENT_STATUS = (
        (EMPLOYED, 'Employed'),
        (UNEMPLOYED, 'Unemployed'),
        (SELF_EMPLOYED, 'Self_employed'),
    )
    employment_status = models.CharField(
        max_length=20, choices=EMPLOYMENT_STATUS, default=UNEMPLOYED)

    def __str__(self):
        return self.first_name
