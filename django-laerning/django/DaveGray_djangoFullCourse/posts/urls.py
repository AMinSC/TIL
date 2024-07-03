from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.posts_list, name="list"),
    # path('new-post/', views.posts_new, name="new-post"),
    path('<slug:slug>', views.post_page, name="page"),
]
