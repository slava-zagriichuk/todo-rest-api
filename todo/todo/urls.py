from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, urls
from todoapp.views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

router = routers.SimpleRouter()
router.register(r'todos', ItemViewSet)

urlpatterns = [

    # path('admin/', admin.site.urls),  # uncomment if you need the django admin panel
    # path('api/v1/', include('rest_framework.urls')),  # and django authentication form
    path('api/v1/', include(router.urls)),
    path('api/v1/signup/', RegisterUserAPIView.as_view()),
    path('api/v1/changePassword/', ChangePasswordAPIView.as_view()),
    path('api/v1/signin/', TokenObtainPairView.as_view()),
    path('api/v1/signin/refresh/', TokenRefreshView.as_view()),
    path('api/v1/signin/verify/', TokenVerifyView.as_view()),

]
