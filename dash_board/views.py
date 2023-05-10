from django.shortcuts import render
from rest_framework import generics
from .models import Dashboard
from .serializer import DashboardGETSerializer, DashboardPOSTSerializer


class DashboardListCreate(generics.ListCreateAPIView):
    queryset = Dashboard.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return DashboardPOSTSerializer
        return DashboardGETSerializer


class DashboardRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dashboard.objects.all()
    serializer_class = DashboardPOSTSerializer

