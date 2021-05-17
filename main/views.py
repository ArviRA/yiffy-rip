from django.shortcuts import redirect, render
from django.http import HttpResponse,JsonResponse
import requests
from requests.sessions import RequestsCookieJar

# Create your views here.
def home(request):
    return render(request,'index.html')

def final_res(request):
    if request.method == "POST":
        print(request.POST['movie_Id'])
        id = request.POST['movie_Id']
        #https://yts.mx/api/v2/movie_details.json?movie_id=10
        details = requests.get("https://yts.unblockninja.com/api/v2/movie_details.json?movie_id={}".format(id))
        print(details)
        send_list = []
        torrent_list = []
        details = details.json()
    #print(details)
        data = details['data']['movie']
    #print(data)
        send_dict = {}
        add = ""
        send_dict['rating'] = data['rating']
        send_dict['trailer'] = "https://www.youtube.com/watch?v="+data['yt_trailer_code']
        send_dict['id'] = data['id']
        send_dict['title']=data['title']
        send_dict['long_title'] = data['title_long']
        send_dict['year'] = data['year']
        send_dict['large_cover_image'] = 'https://yst.mx/movies/poster/'+data['slug']+'.jpg'
        genre = data['genres']
        for j in genre:
            if add == "":
                add  = add + j
            else:
                add  = add + ',' + j
        send_dict['genre'] = add
    #print(i['torrents'])
        torrent_files = data['torrents']
        for link in torrent_files:
            torrent = {}
            torrent['url'] = link['url']
            torrent['clarity'] = link['quality']
            torrent['size'] = link['size']
            torrent['type'] = link['type']
            torrent_list.append(torrent)
        send_dict['torrents'] = torrent_list
        send_dict['story'] = data['description_full']
        #print(data['description_full'])
        send_list.append(send_dict)
        return render(request,'details.html',{'data':send_list})
    else:
        return redirect("/")




def rip(request):
    if request.method == 'POST':
        movie_name = request.POST['movie_name']
        details  = requests.get("https://yts.unblockninja.com/api/v2/list_movies.json?query_term={}".format(movie_name))
        send_dict ={}
        send_list = [] 
        details = details.json()
        try:
            data = details['data']['movies']
            for i in data:
                send_dict = {}
                send_dict['id'] = i['id']
                send_dict['title']=i['title']
                send_dict['long_title'] = i['title_long']
                send_dict['year'] = i['year']
                send_dict['large_cover_image'] = "https://yst.mx/movies/poster/"+i['slug']+'.jpg'
                send_list.append(send_dict)
        #print(send_list)
            return render(request,'searchResults.html',{'data':send_list,'name':movie_name,'status':True})
        except:
            return render(request,'searchResults.html',{"status":False})
    else:
        return redirect("/")
    