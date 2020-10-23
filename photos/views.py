from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, permissions, viewsets

from .models import Photo
from .serializers import PhotoListSerializer, PhotoDetailSerializer, CommentCreateSerializer
from django_filters.rest_framework import DjangoFilterBackend

from .utils import PhotoFilter, PaginationPhotos


# class PhotoViewSet(viewsets.ReadOnlyModelViewSet):
#     """
#     Вывод списка фото
#     """
#     filter_backends = (DjangoFilterBackend,)
#     filterset_class = PhotoFilter
#     pagination_class = PaginationPhotos
#
#     def get_queryset(self):
#         photos = Photo.objects.all()
#         return photos
#
#     def get_serializer_class(self):
#         return PhotoListSerializer

class PhotoListView(generics.ListAPIView):
    """
    Вывод списка фото
    """
    queryset = Photo.objects.all()
    serializer_class = PhotoListSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = PhotoFilter
    pagination_class = PaginationPhotos
    permission_classes = [permissions.IsAuthenticated]

# class PhotoListView(APIView):
#
#     def get(self, request):
#         photos = Photo.objects.filter()
#         serializer = PhotoListSerializer(photos, many=True)
#         return Response(serializer.data)


class PhotoDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Вывод деталей фото
    """
    queryset = Photo.objects.all()
    serializer_class = PhotoDetailSerializer




class CommentCreateView(generics.CreateAPIView):
    """
     Создание комментария к фото
    """

    serializer_class = CommentCreateSerializer


# class CommentCreateView(APIView):

#     def post(self, request):
#         comment = CommentCreateSerializer(data=request.data)
#         if comment.is_valid():
#             comment.save()
#         return Response(status=201)
