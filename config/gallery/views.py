from rest_framework.generics import CreateAPIView, RetrieveAPIView,\
                                    RetrieveUpdateDestroyAPIView, ListAPIView, DestroyAPIView
                                    
from .serializers import CreateGalleryUserSerializer, GalleryREADSerializer, \
                        UserREADSerializer, UserCREATESerializer, GalleryRetrieveSerializer

from .permissions import IsAuthorOrReadOnly
from .models import Gallery
from django.contrib.auth import get_user_model
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response

User = get_user_model()

class CreateGalleryView(CreateAPIView):
    queryset = Gallery.objects.all()
    serializer_class = CreateGalleryUserSerializer

    def perform_create(self, serializer):
        serializer.save(to_user=self.request.user)

class ListGalleryView(ListAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GalleryREADSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('to_user__username',)
    ordering_fields = ('to_user__username', 'created', 'changed')

class RetrievePhotoUserView(RetrieveUpdateDestroyAPIView):
    serializer_class = GalleryRetrieveSerializer
    permission_classes = (IsAuthorOrReadOnly,)

    def get_queryset(self):
        username = self.kwargs.get('username')
        queryset = Gallery.objects.filter(to_user__username = username)
        return queryset        

class RetrieveGalleryView(RetrieveAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GalleryRetrieveSerializer
    permission_classes = (IsAuthorOrReadOnly,)

class RetrieveUserView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserREADSerializer
    lookup_field = 'username'


class CreateUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCREATESerializer
    permission_classes = (AllowAny,)

class DestroyFullGalleryView(DestroyAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GalleryREADSerializer
    permission_classes = (IsAdminUser,)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_queryset()
        self.perform_destroy(instance)
        return Response(status=204)
