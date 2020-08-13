from rest_framework import serializers

from .models import SavedVids

class SavedVidsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SavedVids
        fields = ('title', 'description', 'publishedAt', 'thumbnails_url')