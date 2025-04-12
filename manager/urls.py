from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, UserRegistrationViewSet

router = DefaultRouter()
router.register('books', BookViewSet)

urlpatterns = [
    path('register/', UserRegistrationViewSet.as_view(), name='register'),
    path('token/', obtain_auth_token, name='token-auth'),
]

urlpatterns += router.urls