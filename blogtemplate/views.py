from django.shortcuts import render, redirect, get_object_or_404
from blogtemplate.models import Blog
from .forms import BlogForm

def index(request):
	blogs = Blog.objects.all()
	return render(request, 'index.html', {"blog_list": blogs})

def blog_details(request, blog_id):
	blog = Blog.objects.get(pk=blog_id)
	return render(request, 'blog_details.html', {"blog": blog})


def blog_new(request):
	if request.method == "POST":
		form = BlogForm(request.POST)
		if form.is_valid():
			blog = form.save(commit = False)
			blog.save()
			return redirect('blog_details', blog_id=blog.pk)
	else:
		form = BlogForm()
		return render(request, 'blog_edit.html', {'form': form})

def blog_edit(request, blog_id):
	blog = get_object_or_404(Blog, pk=blog_id)
	if request.method == "POST":
		form = BlogForm(request.POST, instance=blog)
		if form.is_valid():
			blog = form.save(commit=False)
			blog.save()
			return redirect('blog_details', blog_id=blog.pk)
	else:
		form = BlogForm(instance=blog)
		return render(request, 'blog_edit.html', {'form': form})

def blog_delete(request, blog_id):
	blog = get_object_or_404(Blog, pk=blog_id)
	blog.delete()
	new_blogs = Blog.objects.all()
	return render(request, 'index.html', {"blog_list": new_blogs})

