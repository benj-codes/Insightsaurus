from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    path('register/', views.registerUser, name="register"),

    path('', views.profiles, name="profiles"),
    path('profile/<str:pk>/', views.userProfile, name="user-profile"),

    path('account/', views.userAccount, name="account"),
    path('edit-account/', views.editAccount, name="edit-account"),
    path('add-account-skills/', views.addSkill, name="add-account-skills"),
    path('update-account-skills/<str:pk>/', views.updateSkill, name="update-account-skills"),
    path('delete-account-skills/<str:pk>/', views.deleteSkill, name="delete-account-skills"),
]
