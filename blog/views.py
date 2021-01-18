from django.shortcuts import render
from .models import Post, Tag
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    posts = Post.objects.all()

    paginator = Paginator(posts, 10)
    page_namber = request.GET.get('page', 1)
    page = paginator.get_page(page_namber)

    tags = Tag.objects.all()

    context = {'posts': page,
                'tags': tags
    }
    return render(request, 'blog/home.html', context=context)

def post_detail(request, slug):
    post = Post.objects.get(slug__iexact=slug)

    tags_post = post.tags.all()
    tags = Tag.objects.all()

    context = {'post': post,
                'tags': tags,
                'tags_post': tags_post
    }
    return render(request, 'blog/detail.html', context=context)

def tags(request, slug):
    tag = Tag.objects.get(slug__iexact=slug)

    tags = Tag.objects.all()

    posts = tag.posts.all()

    paginator = Paginator(posts, 10)
    page_namber = request.GET.get('page', 1)
    page = paginator.get_page(page_namber)

    context = {'tag': tag,
                'posts': page,
                'tags': tags
    }
    return render(request, 'blog/tags.html', context=context)