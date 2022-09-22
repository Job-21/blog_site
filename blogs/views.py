from django.shortcuts import render
from .models import BlogDetails
# Create your views here.
def home(request):
    blog = BlogDetails.objects.all().values()
    # dictionary = {}
    # for x in blog:
    #     dictionary["title"] = x["title"]
    #     dictionary["blog_text"] = x["blog_text"]
    #     dictionary["blog_date"] = x["blog_date"]
    #     dictionary["author"] = x["author"]
    dictionary = {"contents":blog}
    return render(request, 'index.html', dictionary)