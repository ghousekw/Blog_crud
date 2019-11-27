from django.urls import path

from . views import post_lists, post_detail, post_create, post_update, post_delete

urlpatterns = [
    path('', post_lists),
    path('create/', post_create),
    path('<int:post_id>/', post_detail),
    path('<int:post_id>/update/', post_update),
    path('<int:post_id>/delete/', post_delete),
]