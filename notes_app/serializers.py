from rest_framework import serializers
from django.contrib.auth.models import User
from notes_app.models import NotesDb, TaskDb

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username= validated_data['username'],
            email= validated_data['email'],
            password= validated_data['password']
        )
        return user

class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotesDb
        fields = "__all__"
        read_only_fields = ['id','user','created_at','updated_at']

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskDb
        fields = "__all__"
        read_only_fields = ['id','user','created_at','updated_at']
