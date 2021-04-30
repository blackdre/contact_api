from django.contrib.auth import get_user_model
from rest_framework import viewsets
from .models import Contact
from .serializers import ContactSerializer, UserSerializer


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
