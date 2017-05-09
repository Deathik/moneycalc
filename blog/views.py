from django.shortcuts import render, get_object_or_404


from .models import Post
from feedback.forms import FeedbackForm

def index(request):
    blog_posts = Post.objects.order_by('-pub_date')
    return render(request,
                  template_name='blog/blog_index.html',
                  context={'blog_posts': blog_posts,
                           'form': FeedbackForm()}
                  )


def post(request, post_id):
    post = get_object_or_404(Post, pk =post_id)
    return render(request,
                  'blog/post.html',
                  context={
                      'post': post,
                  }
                  )