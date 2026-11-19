from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from notes_app.models import NotesDb
from notes_app.serializers import RegisterSerializer, NotesSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied

# Create your views here.

class RegistrationView(APIView):
    def post(self, request):
        serializer_instance = RegisterSerializer(data= request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(data={"message":"registration successfull!"})
        return Response(data=serializer_instance.errors)

class NotesListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        notes = NotesDb.objects.filter(user=request.user)
        s_instance = NotesSerializer(notes, many=True)
        return Response(s_instance.data)

    def post(self, request):
        form_data = request.data
        s_instance = NotesSerializer(data= form_data)
        if s_instance.is_valid():
            s_instance.save(user= request.user)
            return Response(data= {'message':'note posted!'})
        return Response(data=s_instance.errors)

class NotesRetreiveUpdateDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        notes = get_object_or_404(NotesDb, id=pk)
        if notes.user != request.user:
            raise PermissionDenied("You are not authorised to access this note")
        
        s_instance = NotesSerializer(notes)
        return Response(data=s_instance.data)

    def put(self, request, pk):
        notes = get_object_or_404(NotesDb, id=pk)
        if notes.user != request.user:
            raise PermissionDenied("You are not authorised to access this note")

        form_data = request.data
        s_instance = NotesSerializer(data=form_data, instance=notes)
        if s_instance.is_valid():
            s_instance.save()
            return Response(data={"message":"note updated!"})
        return Response(data=s_instance.errors)

    def delete(self, request, pk):
        notes = get_object_or_404(NotesDb, id=pk)
        if notes.user != request.user:
            raise PermissionDenied("You are not authorised to access this note")

        notes.delete()
        return Response(data={"message":"note deleted!"})

# class NoteRUD2(APIView):
#     def get_object(self, request, id):
#         return get_object_or_404(NotesDb, id=id, user=request.user)

#     def put(self, request, id):
#         note = self.get_object(request, id)
#         s = NotesSerializer(note, data=request.data)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response(data={"message":"logged out successfully"})