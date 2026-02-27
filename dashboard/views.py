from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

class GetDashboardData(APIView):
    def get(self, request):
        return Response(
            {
                'message': 'Dashboard data retrieved successfully',
                'status': 'success'
            }
        )