from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.utils import timezone
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer


@api_view(['GET'])
def post_list(request, format=None):
    queryset = Post.objects.order_by('date')
    serializer = PostSerializer(queryset, many=True)
    return Response({'post_list': serializer.data})
    
@api_view(['GET'])
def post_detail(request, post_id):
    queryset = Post.objects.get(id=post_id)
    serializer = PostSerializer(queryset)
    return Response({'post': serializer.data})

@api_view(['POST'])
def write_post(request):
    post = Post(title=request.data['title'], content=request.data['content'], date=timezone.now())
    post.save()
    return Response(status=status.HTTP_200_OK)

@api_view(['GET'])
def comment_list(request, post_id, format=None):
    queryset = Comment.objects.filter(post_id=post_id).order_by('-date')
    serializer = CommentSerializer(queryset, many=True)
    return Response({'comment_list': serializer.data})

@api_view(['POST'])
def write_comment(request, post_id):
    comment = Comment(post_id=post_id, content=request.data['content'], date=timezone.now())
    comment.save()
    return Response(status=status.HTTP_200_OK)
