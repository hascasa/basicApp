from django.urls import include, path
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from insurance_app import views

router = DefaultRouter()
router.register(r'insurance', views.InsuranceViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include('insurance_app.urls')), 
]
