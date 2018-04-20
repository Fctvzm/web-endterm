from django.http import HttpResponse, JsonResponse, QueryDict
from django.views.decorators.csrf import csrf_exempt

from web_endterm.blogtemplates.models import Blog


@csrf_exempt
def index(request):
  if request.method == "GET":
    blogs = Blog.objects.all()
    blogs_json = [b.to_json() for b in blogs]
    return JsonResponse(blogs_json, safe=False)

  elif request.method == "POST":
    data = request.POST
    blog = Blog()
    blog.title = data.get('title', '')
    blog.body = data.get('body', '')
    blog.save()
    return JsonResponse(blog.to_json(), status=201)


@csrf_exempt
def blog_details(request, blog_id):
  try:
    blog = Blog.objects.get(pk=blog_id)
  except Exception as e:
    return JsonResponse({"error": str(e)}, status=404)

  if request.method == "GET":
    return JsonResponse(blog.to_json())
  elif request.method == "PUT":
    data = QueryDict(request.body)
    blog.title = data.get('title', blog.title)
    blog.body = data.get('body', blog.body)
    blog.save()
    return JsonResponse(blog.to_json())
  elif request.method == "DELETE":
    blog.delete()
    return JsonResponse(blog.to_json())