from dataclasses import fields
from rest_framework import serializers
from . models import Album, Vaccine , WatchStatus


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ('id','title', 'image', 'date','created_at', 'updated_at','user')


class VaccineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaccine
        fields = ('id','name', 'vacc_type', 'due_date','desc', 'age')

class WatchStatusSerializer(serializers.ModelSerializer):
    model = WatchStatus
    fields = ('status') 