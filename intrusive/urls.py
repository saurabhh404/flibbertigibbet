from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:pk>/", views.detail, name="detail"),
    path("tags/<str:tag>/", views.post_tags, name="post_tags"),
]
