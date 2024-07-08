from rest_framework import serializers
from .models import *


class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']


class SubscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = '__all__'