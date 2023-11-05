from django.shortcuts import render
from songsphere.models import Song
from django.contrib.auth.models import  User
from django.contrib.auth import authenticate,login
from django.shortcuts import redirect
def index(request):
    song=Song.objects.all()
    return render(request,'index.html',{'song':song})

def English(request):
    song = Song.objects.all()
    return render(request,'songsphere/english.html',{'song':song})
def Hindi(request):
    song = Song.objects.all()
    return render(request,'songsphere/hindi.html',{'song':song})
def Telugu(request):
    song = Song.objects.all()
    return render(request,'songsphere/telugu.html',{'song':song})
def Pop(request):
    song = Song.objects.all()
    return render(request,'songsphere/pop.html',{'song':song})
def Melody(request):
    song = Song.objects.all()
    return render(request,'songsphere/melody.html',{'song':song})
def Rock(request):
    song = Song.objects.all()
    return render(request,'songsphere/rock.html',{'song':song})


def songpost(request,id):
    song=Song.objects.filter(song_id=id).first()
    return render(request,'songsphere/songpost.html',{'song':song})



def login(request):
    if request.method == "POST":

        username = request.POST['username']

        password = request.POST['password']
        user = authenticate(username=username, password=password)
        from django.contrib.auth import login
        login(request, user)
        return redirect('/')

    return render(request, 'songsphere/login.html')


def register(request):
    if request.method == "POST":
        email = request.POST['email']
        username = request.POST['username']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name=first_name
        myuser.first_name = last_name
        myuser.save()
        user = authenticate(username=username,password=pass1)
        from django.contrib.auth import login
        login(request,user)
        return redirect('/')
    return render(request, 'songsphere/register.html')