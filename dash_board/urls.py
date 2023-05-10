from django.urls import path
from . import views

urlpatterns = [
    path('list-create/', views.DashboardListCreate.as_view()),
    path('r-u-d/<int:pk>/', views.DashboardRUD.as_view()),
]
