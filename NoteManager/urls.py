"""
URL configuration for NoteManager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from notes_app import views as v
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', v.RegistrationView.as_view()),
    path('api/login/', obtain_auth_token),

    path('api/notes/', v.NotesListCreateView.as_view()),
    path('api/notes/<int:pk>/', v.NotesRetreiveUpdateDeleteView.as_view()),
    
    path('api/logout/', v.LogoutView.as_view()),

    path('api/jwt_login/', TokenObtainPairView.as_view()),
    path('api/refresh/', TokenRefreshView.as_view()),

    path('api/tasks/', v.TaskListCreateView.as_view()),
    path('api/tasks/<int:id>/', v.TokenRetrieveUpdateDeleteView.as_view()),

    path('api/jwt_logout/', v.JWT_Logout.as_view()),
    
]
