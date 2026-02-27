from django.urls import path
from . import views

urlpatterns = [
    path('get_data/', views.GetDashboardData.as_view(), name='dashboard-data'),
]