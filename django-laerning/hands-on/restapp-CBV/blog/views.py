from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.throttling import UserRateThrottle
from .models import Post, Comment, HashTag
from .form import PostForm
from .serializers import PostSerializer, CommentSerializer, HashTagSerializer


### Post
class Index(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serialized_posts = PostSerializer(posts, many=True)  # 직렬화
        return Response(serialized_posts.data)


class Write(APIView):
    
    Throttle_classes = [UserRateThrottle]

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            ## 2차 수정
            post = serializer.save()
            post.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Update(APIView):
    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def post(self, request, pk):
        try:
            # 기존 post를 가져옴
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            # 해당 pk로 post가 존재하지 않을 경우
            return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Delete(APIView):
    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        post.delete()
        return Response({ 'msg': 'Post deleted' }, status=status.HTTP_204_NO_CONTENT)


#  아래는 학습하고 진행하기
class DetailView(APIView):
    def get(self, request, pk):
        post = Post.objects.prefetch_related('comment_set', 'hashtag_set').get(pk=pk)
        
        comments = post.comment_set.all()
        serialized_comments = CommentSerializer(comments, many=True).data
        
        hashtags = post.hashtag_set.all()
        serialized_hashtags = HashTagSerializer(hashtags, many=True).data

        data = {
            "title": "Blog",
            "post_id": pk,
            "comments": serialized_comments,
            "hashtags": serialized_hashtags
        }
        
        return Response(data)


### Comment
class CommentWrite(APIView):
    
    Throttle_classes = [UserRateThrottle]
    
    def post(self, request, pk):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            comment = serializer.save(writer=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentDelete(APIView):
    def post(self, request, pk):
        comment = Comment.objects.get(pk=pk)
        comment.delete()
        return Response({ 'msg': 'Comment deleted' }, status=status.HTTP_204_NO_CONTENT)


### HashTag
class HashTagWrite(APIView):
    
    Throttle_classes = [UserRateThrottle]
    
    def post(self, request, pk):
        serializer = HashTagSerializer(data=request.data)
        if serializer.is_valid():
            hashtag = serializer.save(writer=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HashTagDelete(APIView):
    def post(self, request, pk):
        HashTag = HashTag.objects.get(pk=pk)
        HashTag.delete()
        return Response({ 'msg': 'HashTag deleted' }, status=status.HTTP_204_NO_CONTENT)
