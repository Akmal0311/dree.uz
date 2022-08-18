import requests, json, random, os.path, instaloader
from bs4 import BeautifulSoup as bs
from rest_framework import serializers
from .models import *

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'

class DashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dashboard
        fields = '__all__'

class TreePriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TreePrice
        fields = '__all__'

class TreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tree
        fields = ['tree_type', 'tree_name', 'tree_number']

class ClientSerializer(serializers.ModelSerializer):
    trees = TreeSerializer(many=True)

    class Meta:
        model = Client
        fields = '__all__'

    def create(self, validated_data):

        client = Client.objects.create(
            region=validated_data.pop('region'),
            district=validated_data.pop('district'),
            neighborhood_by=validated_data.pop('neighborhood_by'),
            neighborhood=validated_data.pop('neighborhood'),
            url=validated_data.pop('url'),
        )
        for data in validated_data.get('trees'):
             Tree.objects.create(
                client=client,
                tree_type=data.get('tree_type'),
                tree_name=data.get('tree_name'),
                tree_number=data.get('tree_number'),
            )

        insta_pic_down(str(client.url))


def insta_pic_down(url):

    username = url[26:-1]

    a = instaloader.Instaloader(sleep=False, dirname_pattern='media', save_metadata=False, compress_json=False)

    a.download_profile(username, profile_pic_only=True)



