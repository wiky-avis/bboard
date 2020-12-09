from django.urls import path
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView

from .views import index, other_page, BBLoginView, profile, BBLogoutView, ChangeUserInfoView, BBPasswordChangeView, RegisterUserView, RegisterDoneView, user_activate, DeleteUserView

app_name = 'main'
urlpatterns = [
    path('accounts/register/activate/<str:sign>/', user_activate, name='register_activate'),
    path('accounts/register/done/', RegisterDoneView.as_view(), name='register_done'),
    path('accounts/register/', RegisterUserView.as_view(), name='register'),
    path('accounts/logout/', BBLogoutView.as_view(), name='logout'),
    path('accounts/password/reset/', PasswordResetView.as_view(template_name='main/reset_password.html', subject_template_name='email/reset_subject.txt', email_template_name='email/reset_email.txt'), name='password_reset'),
    path('accounts/password/reset/done/', PasswordResetDoneView.as_view(template_name='main/email_sent.html'), name='password_reset_done'),
    path('accounts/password/confirm/complete/',),
    path('accounts/password/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='main/confirm_password.html'), name='password_reset_confirm'),
    path('accounts/password/change/', BBPasswordChangeView.as_view(), name='password_change'),
    path('accounts/profile/delete/', DeleteUserView.as_view(), name='profile_delete'),
    path('accounts/profile/change/', ChangeUserInfoView.as_view(), name='profile_change'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/login/', BBLoginView.as_view(), name='login'),
    path('<str:page>/', other_page, name='other'),
    path('', index, name='index'),
]