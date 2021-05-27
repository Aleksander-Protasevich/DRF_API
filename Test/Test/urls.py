from django.urls import include, path
from rest_framework import routers
from fairmarkit import views
from django.contrib import admin
# from fairmarkit import urls as basic_urls



router = routers.DefaultRouter()
router.register(r'authors', views.AuthorViewSet)
router.register(r'books', views.BookViewSet)
router.register(r'genres', views.GenreViewSet, basename = 'genre-list')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]





