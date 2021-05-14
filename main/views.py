from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'index.html')


def rip(request):
    movie_name = request.POST['movie_name']
    