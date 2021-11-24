from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from supermarket.models import Items, Category 
from supermarket.serializers import CategorySerializer,ItemSerializer


# Create your views here.


@csrf_exempt
def category(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CategorySerializer(data=data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def item(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        category = request.GET.get('category')
        sub_category = request.GET.get('sub_category')
        name = request.GET.get('name')
        items = Items.objects.all()
        if category:
            items = items.filter(category__name = category)
        if sub_category:
            items = items.filter(sub_category__name = sub_category)
        if name:
            items = items.filter(name = name)
        serializer = ItemSerializer(items, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ItemSerializer(data=data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
