from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Post, Comment, HashTag
from .serializers import PostSerializer, CommentSerializer, HashTagSerializer
from .form import PostForm, CommentForm, HashTagForm


### Post
class Index(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serialized_posts = PostSerializer(posts, many=True)  # 직렬화
        return Response(serialized_posts.data)


class Write(APIView):
    # def get(self, request):
    #     pass

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            post = serializer.save(commit=False)
            post.writer = request.user
            post.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


class Update(APIView):
    def post(self, request, pk):
        try:
            # 기존 post를 가져옴
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            # 해당 pk로 post가 존재하지 않을 경우
            return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)
        if serializer.is_valid():
            form = PostForm(request.POST)
            serializer = PostSerializer(data=request.data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Delete(APIView):
    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Delete(APIView):
    def delete(self, request, pk):
        try:
            # Retrieve post by pk
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            # Return 404 if post does not exist
            return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)
        
        # Delete the post
        post.delete()
        
        # Return a successful response
        return Response({'message': 'Post deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


#  아래는 학습하고 진행하기
class DetailView(APIView):
    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        comments = Comment.objects.select_related('writer').filter(post=post)
        hashtags = HashTag.objects.select_related('writer').filter(post=post)
        serialized = CommentSerializer(instance=post, data=request.data)


class CommentWrite(APIView):
    def post(self, request, pk):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            comment = serializer.save(writer=request.user)
            comment.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HashTagWrite(APIView):
    def post(self, request, pk):
        serializer = HashTagSerializer(data=request.data)
        if serializer.is_valid():
            hashtag = serializer.save(writer=request.user)
            hashtag.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
