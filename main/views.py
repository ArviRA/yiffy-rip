from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.
def home(request):
    return render(request,'index.html')


def rip(request):
    movie_name = request.POST['movie_name']
    details  = requests.get("https://yts.unblockit.onl/api/v2/list_movies.json?query_term={}".format(movie_name))
    send_dict ={}
    send_list = [] 
    details = details.json()
    data = details['data']['movies']
    for i in data:
        send_dict = {}
        send_dict['id'] = i['id']
        send_dict['title']=i['title']
        send_dict['long_title'] = i['title_long']
        send_dict['year'] = i['year']
        send_dict['large_cover_image'] = i['large_cover_image']
        send_list.append(send_dict)
    #print(send_list)
    return render(request,'searchResults.html',{'data':send_list,'name':movie_name})
    

    