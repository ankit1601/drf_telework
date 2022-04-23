from django.urls import path, include
from rest_framework import routers
from telework.views import StaffDataCreateView, StaffDataViewSet, AccountDataView

router = routers.DefaultRouter()
router.register(r'staffdata', StaffDataViewSet, basename='staffdata')
router.register(r'accountdata', AccountDataView, basename='accounts')
print(router.urls)
urlpatterns = [path("staff_data/", StaffDataCreateView.as_view(), name='staff_data')]
urlpatterns += [path('', include(router.urls))]