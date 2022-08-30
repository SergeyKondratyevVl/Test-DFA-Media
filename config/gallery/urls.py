from django.urls import path, include
from .views import CreateUserView, RetrieveUserView,\
                    CreateGalleryView, ListGalleryView,\
                    RetrievePhotoUserView, RetrieveGalleryView, DestroyFullGalleryView

urlpatterns = [
    path('register/', CreateUserView.as_view(), name='register'),
    path('user/<str:username>/', RetrieveUserView.as_view(), name='user'),
    path('user/<str:username>/<int:pk>/', RetrievePhotoUserView.as_view(), name='photo-detail'),    
    path('gallery/', ListGalleryView.as_view(), name='gallery-list'),
    path('gallery/<int:pk>/', RetrieveGalleryView.as_view(), name='gallery-detail'),
    path('gallery/add-photo/', CreateGalleryView.as_view(), name='gallery-post'),
    path('gallery/delete-all/', DestroyFullGalleryView.as_view(), name='delete-all'),
]

urlpatterns += [
    path('', include('rest_framework.urls')),
]
