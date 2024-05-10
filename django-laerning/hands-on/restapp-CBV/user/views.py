from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.contrib.auth import authenticate, login, logout
from .models import Profile
from .form import RegisterForm, LoginForm
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProfileSerializer

# Create your views here.
# user 관련된 기능
# 회원가입
# 로그인
# 로그아웃

### Registration
class Registration(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('blog:list')
        # 회원가입 페이지
        # 정보를 입력할 폼을 보여주어야 한다.
        form = RegisterForm()
        context = {
            'form': form,
            'title': 'User'
        }
        return render(request, 'user/user_register.html', context)
    
    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # 로그인한 다음 이동
            return redirect('user:login')
        context = {
            'form': form
        }
        return render(request, 'user/user_register.html', context)


### Login
class Login(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('blog:list')
        
        form = LoginForm()
        context = {
            'form': form,
            'title': 'User'
        }
        return render(request, 'user/user_login.html', context)
        
    def post(self, request):
        if request.user.is_authenticated:
            return redirect('blog:list')
        
        form = LoginForm(request, request.POST)
        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=email, password=password)  # True, False
            
            if user:
                login(request, user)
                return redirect('blog:list')
            
        form.add_error(None, '아이디가 없습니다.')
        
        context = {
            'form': form
        }
        
        return render(request, 'user/user_login.html', context)


### Logout
class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('blog:list')


### Profile
class ProfileView(APIView):
    # def get(self, request):
    #     pass

    def post(self, request):
        image = request.data.get('image')
        age = request.data.get('age')

        profile = Profile.objects.create(user=request.user, image=image, age=age)
        serializer = ProfileSerializer(profile)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ProfileUpdate(APIView):
    def get(self, request):
        profile = Profile.objects.get(user=request.user)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    def post(self, request):
        try:
            profile = Profile.objects.get(user=request.user)
        except Profile.DoesNotExist:
            return Response({'error': 'Profile not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_vaild():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileDelete(APIView):
    def post(self, request):
        profile = Profile.objects.get(user=request.user)
        profile.delete()
        return Response({'msg': 'Profile deleted'}, status=status.HTTP_200_OK)
