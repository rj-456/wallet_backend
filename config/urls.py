"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
<<<<<<< HEAD
from rest_framework.authtoken.views import obtain_auth_token # Built-in Login
from expenses.views import ExpenseList, ExpenseDetail, RegisterView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', RegisterView.as_view()),      # Register
    path('api/login/', obtain_auth_token),              # Login
    path('api/expenses/', ExpenseList.as_view()),       # CRUD
    path('api/expenses/<int:pk>/', ExpenseDetail.as_view()),
=======

urlpatterns = [
    path('admin/', admin.site.urls),
>>>>>>> a1c5df22701f16e43c62c5ecea222cdf9b6559e6
]
