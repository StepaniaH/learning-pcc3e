from django.urls import path
from . import views

app_name = 'blogs'
urlpatterns = [
    path('', views.index, name='index'),

    path('blogs/', views.blogs, name='blogs'),

    path('blogs/<int:topic_id>/', views.blog, name='blog'),

    # The page for creating a new blog
    path('new_blog/', views.new_blog, name='new_blog'),

    # The page for creating a new article
    path('new_article/<int:topic_id>/', views.new_article, name='new_article'),

    # The page for editing an existing article
    path('edit_article/<int:article_id>/', views.edit_article, name='edit_article'),
]
