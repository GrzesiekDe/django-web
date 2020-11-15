from django.shortcuts import render
from django.utils import timezone
from web.models import Post

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'web/post_list.html', {'posts': posts})