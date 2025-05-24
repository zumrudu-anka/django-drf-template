from django.urls import path
from .views.user_views import (
    registerUser,
    getUserProfile,
    updateUserProfile,
    getUsers,
    getUserById,
    updateUser,
    deleteUser,
    MyTokenObtainPairView,
)

app_name = "api"

urlpatterns = [
    path("users/", getUsers, name="users"),
    path('users/login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path("users/register/", registerUser, name="register"),
    path("users/profile/", getUserProfile, name="users-profile"),
    path("users/profile/update/", updateUserProfile, name="user-profile-update"),
    path("users/<str:pk>/", getUserById, name="user"),
    path("users/update/<str:pk>/", updateUser, name="user-update"),
    path("users/delete/<str:pk>/", deleteUser, name="user-delete"),
]
