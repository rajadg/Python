'''
Created on 26-May-2016

@author: dgraja
'''
from rest_framework import serializers
from ex02model.models import comment
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = comment
        fields = ('id', 'text', 'author')


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def comment_detail(request, pk):
    try:
        item = None
        if str(pk) != '0' or request.method == "GET":
            item = comment.objects.filter(pk=int(pk))[0]
    except comment.DoesNotExist:
        print "comment with id: %r does not exist" % item
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = CommentSerializer(item)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CommentSerializer(item, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return HttpResponse(status=204)


@csrf_exempt
def comment_list(request):
    data = ""
    try:
        result = comment.objects.all()
        if request.method == "GET":
            data = CommentSerializer(result, many=True)
            return JSONResponse(data.data)
        elif request.method == "POST":
            data = JSONParser().parse(request)
            serializer = CommentSerializer(data)
            if serializer.is_valid():
                serializer.save()
                return JSONResponse(serializer.data, status=201)
            return HttpResponse(status=400)
    except comment.DoesNotExist:
        print "comments empty"
    return HttpResponse(status=404)

