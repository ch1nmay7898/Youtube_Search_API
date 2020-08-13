# Youtube_Search_API
Consumes YouTube API V3 and stores information

### Usage
Install dependencies.
```shell
pip install -r requirements.txt
```
Supply youtubeapiv3 keys in settings.py.
```shell
cd ytsearch/ytsearch
```
Edit settings.py file.
```
YT_KEY = '<Enter Key>'
YT_KEY_SUP = '<Enter Supplementary Key>'
```

Prepare database.
```shell
cd ..
python manage.py migrate
```

Start the server.
```shell
python manage.py runserver
```
Start background proccess tasks (on a separate terminal window)
```
python manage.py process_tasks
```
Go to the URL: `http://127.0.0.1:8000/`
This is the GET http url for our API.

To fetch the data from databse: add the argument `SavedVids/` to the URL.
Data is returned in a paginated response on Django REST framework.

To view the HTML render of data, go to: `http://127.0.0.1:8000/view`
