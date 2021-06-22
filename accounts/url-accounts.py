from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path("register/",views.register, name="register" ),
    path("login/",views.login, name="login" ),
    # the logout view is already ready to use so no need to add view for it
    # also you have to set it in setting file to redirect to url after logout (LOGOUT_REDIRECT_URL = "your u url")
    path('logout/', auth_view.LogoutView.as_view(), name="logout"),
    path("dashboard/",views.dashboard, name="dashboard" ),
]