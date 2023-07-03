from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post, Comment, HashTag
from .form import PostForm, CommentForm, HashTagForm
from django.urls import reverse_lazy, reverse


### Post
class Index(View):
    def get(self, request):
        # return HttpResponse('Index page GET class')

        # 데이터베이스 접근해서 값을 가져와야 함
        # 게시판에 글들을 보여줘야하기 때문에 데이터베이스에서 "값 조회"  all()
        post_objs = Post.objects.all()
        # context = 데이터베이스에서 가져온 값
        context = {
            "posts": post_objs
        }
        return render(request, 'blog/post_list.html', context)


# Django 자체의 클래스 뷰 기능도 강력, 편리
# model, templte_name, context_object_name
# paginate_by(보여주는 페이지 설정), form_class, form_valid(),
# django.views.generic -> ListView
# class List(ListView):
#     model = Post  # Model
#     template_name = 'blog/post_list.html'  # temlplate
#     context_object_name = 'posts'  # 변수 값의 이름


# class Write(CreateView):
#     model = Post  # Model
#     form_class = PostForm  # Form
#     success_url = reverse_lazy('blog:list')  # 성공시 보내줄 url

class Write(LoginRequiredMixin, View):
    # Mixin: LoginRequiredMixin
    def get(self, request):
        form = PostForm()
        context = {
            'form': form
        }
        return render(request, 'blog/post_form.html', context)

    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)  # commit=False 변수 할당만 우선 하고
            post.writer = request.user
            post.save()
            return redirect('blog:list')
        form.add_error(None, '폼이 유효하지 않습니다.')
        context = {
            'form': form
        }
        return render(request, 'blog/post_form.html')


class Update(UpdateView):
    model = Post
    template_name = 'blog/post_edit.html'
    fields = ['title', 'content']
    # success_url = reverse_lazy('blog:list')
    
    # initial 기능 사용 -> form에 값을 미리 넣어주기 위해서
    def get_initial(self):
        initial = super().get_initial()  # UpdateView(generic view)에서 제공하는 initial(딕셔너리)
        post = self.get_object()  # pk 기반으로 객체를 가져옴
        initial['title'] = post.title
        initial['content'] = post.content
        return initial
    
    def get_success_url(self):  # get_absolute_url
        post = self.get_object()  # pk 기반으로 현재 객체 가져오기
        return reverse('blog:detail', kwargs={ 'pk': post.pk })


class Delete(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:list')


class DetailView(View):
    def get(self, request, pk):
        # list -> object 상세 페이지 -> 상세 페이지 하나의 내용
        # pk 값을 왔다갔다, 하나의 인자

        # 데이터베이스 방문
        post = Post.objects.get(pk=pk)
        # 댓글
        comments = Comment.objects.filter(post=post)
        # 해시태그
        hashtags = HashTag.objects.filter(post=post)

        # 댓글 form
        comment_form = CommentForm()

        # 태그 form
        hashtag_form = HashTagForm()
        
        context = {
            'post': post,
            'comments': comments,
            'comment_form': comment_form,
            'hashtags': hashtags,
            'hashtag_form': hashtag_form,
        }
        

        return render(request, 'blog/post_detail.html', context)


### Comment
class CommentWrite(View):
    # def get(self, request):
    #     pass

    def post(self, request, comment_id):
        form = CommentForm(request.POST)
        if form.is_valid():
            # 사용자에게 댓글 내용을 받아옴
            content = form.cleaned_data['content']
            # 해당 아이디에 해당하는 글 불러옴
            post = Post.objects.get(pk=comment_id)
            # 댓글 객체 생성, Create 메서드를 사용할 때는 sava 필요 없음
            comment = Comment.objects.create(post=post, content=content)
            return redirect('blog:detail', pk=comment_id)


class CommentDelete(View):
    def post(self, request, comment_id):
        comment = Comment.objects.get(pk=comment_id)
        post_id = comment.post.id
        # post_id는 객체를 삭제하기 전에 받아와야 함
        comment.delete()

        return redirect('blog:detail', pk=post_id)



### Tag
class HashTagWrite(View):
    def post(self, request, hashtag_id):
        form = HashTagForm(request.POST)
        if form.is_valid():
            # 사용자에게 태그 내용을 받아옴
            name = form.cleaned_data['name']
            # 해당 아이디에 해당하는 글 불러옴
            post = Post.objects.get(pk=hashtag_id)
            # 댓글 객체 생성, Create 메서드를 사용할 때는 sava 필요 없음
            hashtag = HashTag.objects.create(post=post, name=name)
            return redirect('blog:detail', pk=hashtag_id)
        

class HashTagDelete(View):
    def post(self, request, hashtag_id):
        hashtag = HashTag.objects.get(pk=hashtag_id)
        post_id = hashtag.post.id
        # post_id는 객체를 삭제하기 전에 받아와야 함
        hashtag.delete()

        return redirect('blog:detail', pk=post_id)
