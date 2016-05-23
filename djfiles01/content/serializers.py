'''
Created on 21-May-2016

@author: dgraja
'''



from rest_framework import serializers
from content.models import comment


class CommentSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    text = serializers.CharField(max_length=1024)

    def create(self, validated_data):
        """
        Create and return a new `comment` instance, given the validated data.
        """
        return comment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `comment` instance, given the validated data.
        """
        instance.text = validated_data.get('text', instance.text)
        instance.save()
        return instance