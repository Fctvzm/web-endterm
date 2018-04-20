from django.shortcuts import render
from blogtemplate.models import Blog
from django.http import HttpResponse, JsonResponse, QueryDict

def index(request):
	if request.method == "GET":
		blogs = Blog.objects.all()
		return render(request, 'index.html', {"blog_list": blogs})
	elif request.method == "POST":
	    data = request.POST
	    blog = Blog()
	    blog.title = data.get('title', '')
	    blog.body = data.get('body', '')
	    blog.save()
	    return render(request, 'index.html', {"blog_list": blogs})

def blog_details(request, blog_id):
 	blog = Blog.objects.get(pk=blog_id)

 	if request.method == "GET":
		return render(request, 'blog_details.html', {"blog": blog})
	elif request.method == "PUT":
	    data = QueryDict(request.body)
	    blog.title = data.get('title', blog.title)
	    blog.body = data.get('body', blog.body)
	    blog.save()
	    return render(request, 'blog_details.html', {"blog": blog})
	elif request.method == "DELETE":
	    blog.delete()
	 	return render(request, 'index.html', {"blog_list": blogs})

