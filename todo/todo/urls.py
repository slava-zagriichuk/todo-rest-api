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
# router.register('login', LoginViewSet, basename="login")

urlpatterns = [

    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    # path('api/v1/', include('rest_framework.urls')),  # Just regular authentication form
    path('api/v1/signup/', RegisterUserAPIView.as_view()),
    path('api/v1/changePassword/', ChangePasswordAPIView.as_view()),
    path('api/v1/signin/', TokenObtainPairView.as_view()),
    path('api/v1/signin/refresh/', TokenRefreshView.as_view()),
    path('api/v1/signin/verify/', TokenVerifyView.as_view()),

]
