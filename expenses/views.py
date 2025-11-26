<<<<<<< HEAD
from rest_framework import generics, permissions
from .models import Expense
from .serializers import ExpenseSerializer, UserSerializer
from django.contrib.auth.models import User

# 1. REGISTER (Open to everyone)
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

# 2. LIST/CREATE (Protected: Only show my own expenses)
class ExpenseList(generics.ListCreateAPIView):
    serializer_class = ExpenseSerializer
    permission_classes = [permissions.IsAuthenticated] # Must be logged in

    def get_queryset(self):
        return Expense.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user) # Auto-assign owner

# 3. DETAIL/DELETE (Protected: Only edit my own)
class ExpenseDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ExpenseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Expense.objects.filter(owner=self.request.user)
=======
from django.shortcuts import render

# Create your views here.
>>>>>>> a1c5df22701f16e43c62c5ecea222cdf9b6559e6
