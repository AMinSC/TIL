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
    #     # 사용자 작성 Form 만들어서 보내줌
    #     pass
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
        serializer = PostSerializer(post)
        if serializer.is_valid():
            post.delete()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)


#  아래는 학습하고 진행하기
class DetailView(APIView):
    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        comments = Comment.objects.select_related('writer').filter(post=post)
        hashtags = HashTag.objects.select_related('writer').filter(post=post)
        serialized = CommentSerializer(instance=post, data=request.data)


### Comment
class CommentWrite(APIView):
    def post(self, request, pk):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            comment = serializer.save(writer=request.user)
            comment.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class CommentDelete(APIView):
    def post(self, request, pk):
        comment = Comment.objects.get(pk=pk)
        serializer = CommentSerializer(comment)

        if serializer.is_valid():
            comment.delete()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)


### HashTag
class HashTagWrite(APIView):
    def post(self, request, pk):
        serializer = HashTagSerializer(data=request.data)
        if serializer.is_valid():
            hashtag = serializer.save(writer=request.user)
            hashtag.save()
            return Response(serializer.data, status=status.stats_HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HashTagDelete(APIView):
    def post(self, request, pk):
        HashTag = HashTag.objects.get(pk=pk)

        serializer = HashTagSerializer(HashTag)
        HashTag.delete()
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
