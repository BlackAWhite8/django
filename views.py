from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Post
from .forms import New_Post, Add_comment
from django.utils import timezone
# Create your views here.

def index(request):
	post = Post.objects.order_by("-publish_date")
	return render(request,"blog/index.html", {"post":post})

def info(request):
	return render(request,"blog/info.html")


def create_post(request):
    if request.method == "POST":
        form = New_Post(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.publish_date = timezone.now()
            post.save()
    else:
        form = New_Post()
    return render(request, 'blog/create_post.html', {'form': form})

def show_comments(request,post_id):
	post = get_object_or_404(Post, pk=post_id)
	return render(request, 'blog/show_comments.html',{'post': post})

def create_comment(request):
	if request.method == "POST":
		form = Add_comment(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.save()
			return redirect('index')
	else:
		form = Add_comment()
	return render(request, 'blog/create_comments.html',{'form':form})
