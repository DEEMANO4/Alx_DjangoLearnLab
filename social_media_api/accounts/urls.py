from django.urls import path
from .views import UserRegistrationView, UserLoginView, ProfileManagementView, FollowUserView, UnfollowUserView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('profile/', ProfileManagementView.as_view(), name='profile-management'),
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='followed')
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollowed')
]