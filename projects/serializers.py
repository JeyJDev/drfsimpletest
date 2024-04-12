from django.db.models import fields
from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
  class Meta:
    model = Project
    fields = ('id', 'title', 'description', 'technology', 'create_at')
    read_only_fields = ('id', 'create_at',)