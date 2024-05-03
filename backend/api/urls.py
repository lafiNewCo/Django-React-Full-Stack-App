from django.urls import path, include
from .views import CreateUserView, NoteListCreate, DeleteNote
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



urlpatterns = [
    path("user/register", CreateUserView.as_view(), name = "register"),
    path("token", TokenObtainPairView.as_view(), name="get_token"),
    path("token/refresh", TokenRefreshView.as_view(), name="refresh"),
    path("auth/", include("rest_framework.urls")),
    path("notes", NoteListCreate.as_view(), name = "note-list"),
    path("notes/delete/<int:pk>", DeleteNote.as_view(), name="delete-note"),

]