'''
Created on 26-May-2016

@author: dgraja
'''

from rest_framework import serializers
from ex01simple.models import contact
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


class ContactSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=256)
    phone = serializers.CharField(max_length=16)

    def create(self, validated_data):
        """
        Create and return a new `comment` instance, given the validated data.
        """
        return contact.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `comment` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.save()
        return instance


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def contact_detail(request, pk):
    try:
        item = None
        if str(pk) != '0' or request.method == "GET":
            item = contact.objects.filter(pk=int(pk))[0]
    except contact.DoesNotExist:
        print "comment with id: %r does not exist" % item
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = ContactSerializer(item)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ContactSerializer(item, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return HttpResponse(status=204)


@csrf_exempt
def contact_list(request):
    data = ""
    try:
        result = contact.objects.all()
        if request.method == "GET":
            data = ContactSerializer(result, many=True)
            return JSONResponse(data.data)
        elif request.method == "POST":
            data = JSONParser().parse(request)
            serializer = ContactSerializer(data)
            if serializer.is_valid():
                serializer.save()
                return JSONResponse(serializer.data, status=201)
            return HttpResponse(status=400)
    except contact.DoesNotExist:
        print "comments empty"
    return HttpResponse(status=404)
