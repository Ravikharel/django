from django.shortcuts import render
from .models import Post
from django.http import Http404
import random 


def post_list(request):
    posts = Post.published.all()
    return render(
        request,
        'blog/post/list.html',
        {'posts': posts}
    )

def post_detail(request, pk):
    try:
        post = Post.published.get(pk=pk)
    except Post.DoesNotExist:
        raise Http404("No Post found.")

    # Sample comments for demo purposes
    sample_comments = [
        {'author': 'Alice', 'text': 'This was such a helpful post, thank you!'},
        {'author': 'Bob', 'text': 'Great writing, very informative.'},
        {'author': 'Charlie', 'text': 'I learned a lot from this!'},
        {'author': 'Daisy', 'text': 'Please write more about this topic.'},
        {'author': 'Evan', 'text': 'Loved the examples, so clear!'},
    ]

    random_comments = random.sample(sample_comments, k=3)

    return render(
        request,
        'blog/post/detail.html',
        {
            'post': post,
            'comments': random_comments,
        }
    )