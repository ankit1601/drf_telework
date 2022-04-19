from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, status
from .serializers import StaffDataSerializer
from .models import StaffData

# Create your views here.


class StaffDataViewSet(viewsets.ModelViewSet):
    queryset = StaffData.objects.all()
    serializer_class = StaffDataSerializer

    def list(self, request):
        queryset = StaffData.objects.all()
        serializer = StaffDataSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = StaffDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def retrieve(self, request, pk=None):
        print("inside retrieve")
        user = get_object_or_404(self.queryset, pk=pk)
        serializer = StaffDataSerializer(user)
        return Response(serializer.data)

    def update(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        serializer = StaffDataSerializer(user, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        serializer = StaffDataSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True),
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        self.perform_destroy(user)
        return Response(status=status.HTTP_204_NO_CONTENT)


class StaffDataCreateView(APIView):
    queryset = StaffData.objects.all()

    def get(self, request):
        queryset = StaffData.objects.all()
        serializer = StaffDataSerializer(queryset, many=True)
        data = serializer.data
        return Response(data=data, status=200)

    def post(self, request):
        data = request.data
        serializer = StaffDataSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            data = {"data is created"}
            status = 200
        else:
            data = serializer.errors
            status = 400
        return Response(data=data, status=status)

