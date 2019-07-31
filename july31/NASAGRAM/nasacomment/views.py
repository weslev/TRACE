from django.shortcuts import render
from nasacomment import views
from django.http import HttpResponse, HttpResponseRedirect
from nasacomment.models import Comment
from datetime import datetime, date
import requests

# Create your views here.
def view_home(request):
    return render(request, 'homepage.html')


def picture_list(request):
    dateBase = "2019-05-0"
    urls = []
    for x in range(1,6):
        newDate = dateBase + str(x)
        tempUrl = f"https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY&date={newDate}"
        response = requests.get(tempUrl).json()
        responseURL = response['url']
        urls.append(responseURL)
    return render(request, 'picture_list.html', context = {'urls': urls})

def create(request):
    if request.method == 'GET':
        photoUrl = (request.GET.get('photourl', 'ERROR'))
        comments = Comment.objects.all().filter(image=photoUrl)
        return render(request, 'form.html', context = {'photoUrl': photoUrl, 'comments': comments})

    elif request.method == 'POST':
        Comment.objects.create(
            comment = request.POST.get('comment', 'Default Comment'),
            rating = request.POST.get('rating', ''),
            image = request.POST.get('url', '')
        ) 
        return HttpResponseRedirect("http://127.0.0.1:8000/create?photourl=" + request.POST.get('url', '/home'))

def delete(request, id):
    print("delete")
    if request.method == 'POST':
        print("Delete")
        Comment.objects.get(pk=id).delete()
        return HttpResponse("DELETED", status = 204)
