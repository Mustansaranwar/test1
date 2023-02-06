from django.shortcuts import render,HttpResponse
import requests
import json
# import urllib2
from django.http import HttpResponse
from urllib.parse import urlencode
from urllib.request import Request,urlopen
from one.models import Publisher, Book, Store
import uuid
import requests
# from flask import Flask, render_template, session, request, redirect, url_for
# from flask_session import Session  # https://pythonhosted.org/Flask-Session
import msal
# import app_config
from django.db.models import Prefetch

def home(request):
    # citys = Province.objects.prefetch_related('city_set').get(name__iexact=u"Punjab")
    # queryset = Store.objects.first().Book.P()
    # queryset = Publisher.objects.all().prefetch_related(Prefetch('Publisher', data=Store.objects.filter(name='jinnah')))
    # queryset = Publisher.objects.distinct(name)

    # b = Store.objects.prefetch_related('books__publisher').first()
    # first_model_data = b.books.all().values_list('publisher')
    a = Store.objects.filter(books__name = 'republic')
    

    # queryset = Store.objects.select_related('Book_set__Publisher').filter(name='styen')

    # print(related_first_models)
    # stores = []

    # for book in queryset:
    #     print(f'store name : {book.book_set.all()} ')
        # books = [book.name for book in store.books.all()]
        # stores.append({'id': store.id, 'name': store.name, 'books': books})
    return HttpResponse(a)

# app = Flask(__name__)
# app.config.from_object(app_config)
# Session(app)


# @app.route("/")
# def index():
#     if not session.get("user"):
#         return redirect(url_for("login"))
#     return render_template('index.html', user=session["user"])

# @app.route("/login")
# def login():
#     session["state"] = str(uuid.uuid4())
#     auth_url = _build_msal_app().get_authorization_request_url(
#         app_config.SCOPE,  # Technically we can use empty list [] to just sign in,
#                            # here we choose to also collect end user consent upfront
#         state=session["state"],
#         redirect_uri=url_for("authorized", _external=True))
#     return "<a href='%s'>Login with Microsoft Identity</a>" % auth_url




def login(request):
    print('heee')
    return render(request, 'login.html')

# def authorize_response(request):

#     return HttpResponse(f'Returned response {request}') 

def callback(request):
    print('hello callback')
    return render(request, 'home.html')
    # print('Hi There')
    # myStr = str(request)
    # x = myStr.split("=")[1]
    # code = x.split('&client_info')[0]
    # client_info = myStr.split('client_info=')[1]
    # info = client_info.split('&')[0]
    # state_code = myStr.split('state=')[1]
    # state = state_code.split('&')[0]
    # session_state = myStr.split('session_state=')[1]
    # session_Sate = session_state.split('&')[0]
    # sessionState = session_Sate.split("'>")[0]


    # url = f'https://login.microsoftonline.com/ec0a1000-3407-4d2f-81f9-dfd1179718dc/oauth2/v2.0/authorize?response_type=code&client_id=5f2ad11c-54cd-4eb5-9e47-b238f25419cf&redirect_uri=http://localhost/callback&response_mode=query&scope=user.read&state={state}'
    # url = 'https://login.microsoftonline.com/ec0a1000-3407-4d2f-81f9-dfd1179718dc/oauth2/v2.0/authorize'
    

    # print(sessionState)
    # print(state)
    # print(info)
    # print(f'code : {code}')

    # headers = {
    #     'Content-Type' : 'application/x-www-form-urlencoded',
    #     'Content-Length' : '48142',
    #     'Host' : 'login.microsoftonline.com',
    #     'Accept' : '*/*',
    #     'Accept-Encoding' : 'gzip, deflate, br',
    #     'Connection' : 'keep-alive',
    # }
    # data = {
    #     'tenant':'ec0a1000-3407-4d2f-81f9-dfd1179718dc',
    #     'client_id' : '5f2ad11c-54cd-4eb5-9e47-b238f25419cf',
    #     'response' : 'code',
    #     'client_secret' : '4a577634-f62d-43c0-8424-24f93e3d717d',
    #     'redirect_uri' : 'http://localhost:8000/callback', 
    #     'scope' : 'user.read',
    # }


    # r = requests.post(url, data=json.dumps(data),headers=headers)
    # print(r.status_code)
    # print(r.headers['content-type'])
    # print(r.encoding)
    # print(r.text)
    # return render(request,'post.html',{'url':r})
    # answer = r.json()


    # r=requests.post(url, headers=headers, data=data)
    # request = Request(url,urlencode(data).encode())
    # json = urlopen(request).read().decode()
    # print(answer)
    
    # return HttpResponse(f'Get token auth request and data is as {r}')
 
    # return render(request,'post.html',{'url':json})


    # data = {
    #     'response_type' : code,
    #     'redirect_uri' : 'http://localhost:8000/callback',
    #     'response_mode' : 'query',
    #     'scope' : 'user.read',
    #     'state': 'rWCOhbBZVxiuDTNv'
    # }


# &response_mode=query



    # url = 'https://login.microsoftonline.com/ec0a1000-3407-4d2f-81f9-dfd1179718dc/oauth2/v2.0/authorize?client_id=fa06ec4c-8c8a-43ab-be71-0809322f2dd7'
    
    # url = 'https://login.microsoftonline.com/ec0a1000-3407-4d2f-81f9-dfd1179718dc/oauth2/v2.0/token HTTP/1.1'
    # url = 'https://login.microsoftonline.com/ec0a1000-3407-4d2f-81f9-dfd1179718dc/oauth2/authorize'
    # data = {'longUrl': 'http://www.google.com/'}
    # headers = {'Content-Type': 'application/json'}

    # r = requests.post(url, data=json.dumps(data), headers=headers)

    # url = 'https://login.microsoftonline.com/ec0a1000-3407-4d2f-81f9-dfd1179718dc/oauth2/v2.0/authorize?client_id=f03b5c74-f63f-4bbd-a920-70c91b201c97'

    # url = 'https://login.microsoftonline.com/ec0a1000-3407-4d2f-81f9-dfd1179718dc/oauth2/v2.0/token'
    # url = 'https://login.microsoftonline.com/ec0a1000-3407-4d2f-81f9-dfd1179718dc/oauth2/v2.0/token'
    # response = requests.post('https://login.microsoftonline.com/{ec0a1000-3407-4d2f-81f9-dfd1179718dc}/oauth2/v2.0/token', data=data)
    # content = response.content
    # print(url)


    # req = requests.Request('POST','https://login.microsoftonline.com/ec0a1000-3407-4d2f-81f9-dfd1179718dc/oauth2/v2.0/token',headers={'Content-Type':'application/x-www-form-urlencoded'},data=data)
    # prepared = req.prepare()
    # return prepared
    # post_url = 'https://www.googleapis.com/urlshortener/v1/url?key={API_KEY}'
    # params = json.dumps({'longUrl': url})
    # response = requests.post(url,params,headers={'Content-Type': headers})
    # print('sneddddddddd')
    # return HttpResponse('Get token auth request and data is as: {}'.format(response.text))

    # post_data = data
    # post_data.update({'user': request.user.pk})
    # payload = {'username': 'alishavaiz103@gmail.com', 'password': '786AliJutt'}
    # r = requests.post('https://login.microsoftonline.com/ec0a1000-3407-4d2f-81f9-dfd1179718dc/oauth2/v2.0/token', params=data)
    # return HttpResponse('Get token auth request and data is as: {}'.format(r.text))
    
    # r=requests.post(url, headers=headers, data=data)
    # r=requests.post(url, data=data)

    # print(url)
    # print(headers)/
    # print(data
    # return HttpResponse(f'Get token auth request and data is as {r}')
    
    # return json.loads(r.text)
    # return render(request, 'https://login.microsoftonline.com/ec0a1000-3407-4d2f-81f9-dfd1179718dc/oauth2/v2.0/token HTTP/1.1', {'data':data, 'url':url, 'header':headers})