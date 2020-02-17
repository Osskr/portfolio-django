from django.shortcuts import render, get_object_or_404
from .models import BlogPost
# Create your views here.
def allblogs(request):
    blog = BlogPost.objects
    return render(request,'blog/allblogs.html',{'blog':blog})

def detail(request, blog_id):
    detail_blog = get_object_or_404(BlogPost, pk=blog_id)
    return render(request,'blog/detail.html', {'blog':detail_blog})