from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    # user/
    # 회원가입
    path('register/', views.Registration.as_view(), name='register'),
    # 로그인
    path('login/', views.Login.as_view(), name='login'),
    # 로그아웃
    path('logout/', views.Logout.as_view(), name='logout'),
    # 프로파일 view
    path('profile/', views.ProfileView.as_view(), name='profile-view'),
    # 프로파일 update
    path('profile/update/', views.ProfileUpdate.as_view(), name='profile-update'),
    # 프로파일 delete
    path('profile/delete/', views.ProfileDelete.as_view(), name='profile-delete'),
]
