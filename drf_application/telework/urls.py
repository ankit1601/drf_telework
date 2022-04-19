from django.urls import path, include
from rest_framework import routers
from telework.views import StaffDataCreateView, StaffDataViewSet

router = routers.DefaultRouter()
router.register(r'staffdata', StaffDataViewSet, basename='staffdata')
print(router.urls)
urlpatterns = [path("staff_data/", StaffDataCreateView.as_view(), name='staff_data')]
urlpatterns += [path('', include(router.urls))]