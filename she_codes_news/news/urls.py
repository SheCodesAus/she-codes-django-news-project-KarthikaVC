from django.urls import path
from . import views


app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.StoryView.as_view(), name='story'),
    path('add-story/', views.AddStoryView.as_view(), name='newStory'),
    path('myStories/',views.MyStoriesView.as_view(),name='myStories'),
    path('search_author/',views.search_author,name='search_author'),
    path('post_delete/<int:pk>/',views.post_delete,name='post_delete'),
    path('post_edit/<int:pk>/',views.post_edit,name='post_edit'),
]
