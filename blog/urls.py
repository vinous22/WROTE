from django.urls import path
from .views import post_list, post_share, post_detail, post_search

app_name = 'blog'


urlpatterns = [
    # post views
    path('', post_list, name='post_list'),
    path('tag/<slug:tag_slug>/', post_list, name='post_list_by_tag'),
    path('<int:post_id>/share/', post_share, name='post_share'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         post_detail,
         name='post_detail'),
    path('search/', post_search, name='post_search'),
]
