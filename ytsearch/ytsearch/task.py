"""
from ytsearch.celery import app
from celery.task.schedules import crontab
from datetime import timedelta
from celery.decorators import periodic_task
"""
from search.models import SavedVids
from django.conf import settings
from background_task import background

@background(repeat=30)
def API_call():
    url = 'https://www.googleapis.com/youtube/v3/search'
    params = {
        'part' : 'snippet',
        'q' : 'Product Review',
        'type' : 'video',
        'order' : 'date',
        'publishedAfter' : '2019-01-01T00:00:00Z',
        'key' : settings.YT_KEY
    }
    r = requests.get(url, params=params)
    print(r.text)
    items = r.json()['items']
    vidid = items[0]['id']['videoId']
    title = items[0]['snippet']['title']
    description = items[0]['snippet']['description']
    thumbnail_url = items[0]['snippet']['thumbnails']['default']['url']
    date_time = items[0]['snippet']['publishedAt']
    savedvids = SavedVids.objects.all()
    print(savedvids)
    last = savedvids.last()
    if last.videoId != vidid:
        f = SavedVids(videoId=vidid, title=title, description=description, thumbnails_url=thumbnail_url, publishedAt=date_time)
        return f.save()
    else:
        return print("No Updates")