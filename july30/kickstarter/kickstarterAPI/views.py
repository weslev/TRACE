from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from kickstarterAPI.models import Kickstarter
from kickstarterAPI.serializer import KickstarterSerializer


# Create your views here.
def hello_world(request):
    return HttpResponse("Hello world!")

@csrf_exempt
def kickstarter_list(request):
    if request.method == 'GET':
        kickstarters = Kickstarter.objects.all()
        serializer = KickstarterSerializer(kickstarters, many = True)
        return JsonResponse(serializer.data, safe = False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = KickstarterSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def kickstarter_detail(request, pk):
    try:
        kickstarter = Kickstarter.objects.get(pk=pk)
    except kickstarter.DoesNotExist:
        return HttpResponse(status = 404)
    print(request.method)
    if request.method == 'GET':
        serializer = KickstarterSerializer(kickstarter)
        return JsonResponse(serializer.data)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = KickstarterSerializer(kickstarter, data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status = 400)

    elif request.method == 'DELETE':
        print("Do We get there")
        kickstarter.delete()
        return HttpResponse(status = 204)