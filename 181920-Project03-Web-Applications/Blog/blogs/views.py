from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Blog, Article
from .forms import BlogForm, ArticleForm

def index(request):
    return render(request, 'blogs/index.html')

@login_required
def blogs(request):
    blogs = Blog.objects.filter(owner=request.user).order_by('pub_date')
    articles = {'blogs': blogs}
    return render(request, 'blogs/blogs.html', articles)

@login_required
def blog(request, topic_id):
    blog = Blog.objects.get(id=topic_id)
    _check_owner(request, blog)
    articles = blog.article_set.order_by('pub_date')
    context = {'blog': blog, 'articles': articles}
    return render(request, 'blogs/blog.html', context)

@login_required
def new_blog(request):
    if request.method != 'POST':
        form = BlogForm()
    else:
        form = BlogForm(data=request.POST)
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.owner = request.user
            if not new_blog.pub_date:
                new_blog.pub_date = timezone.now()
            new_blog.save()
            return redirect('blogs:blogs')

    context = {'form': form}
    return render(request, 'blogs/new_blog.html', context)

@login_required
def new_article(request, topic_id):
    blog = Blog.objects.get(id=topic_id)
    if request.method != 'POST':
        form = ArticleForm()
    else:
        form = ArticleForm(data=request.POST)
        if form.is_valid():
            new_article = form.save(commit=False)
            if not new_article.pub_date:
                new_article.pub_date = timezone.now()
            new_article.blog = blog
            new_article.save()
            return redirect('blogs:blog', topic_id=blog.id)

    context = {'form': form, 'blog': blog}
    return render(request, 'blogs/new_article.html', context)

@login_required
def edit_article(request, article_id):
    article = Article.objects.get(id=article_id)
    blog = article.blog
    _check_owner(request, blog)
    if request.method != 'POST':
        form = ArticleForm(instance=article)
    else:
        form = ArticleForm(data=request.POST, instance=article)
        if form.is_valid():
            new_article = form.save(commit=False)
            if not new_article.pub_date:
                new_article.pub_date = timezone.now()
            new_article.blog = blog
            new_article.save()
            return redirect('blogs:blog', topic_id=blog.id)

    context = {'article': article, 'form': form, 'blog': blog}
    return render(request, 'blogs/edit_article.html', context)

# Check if the user is the owner of the blog
def _check_owner(request, blog):
    if request.user != blog.owner:
        raise Http404
