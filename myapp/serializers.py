# -*- coding: utf-8 -*-
from .models import mymodel
from rest_framework import serializers

class myserializer(serializers.ModelSerializer):
    class Meta:
        model = mymodel
        fields = ('name','major','number')
