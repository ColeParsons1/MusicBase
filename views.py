from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.template import loader
from django.conf.urls import url
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from .models import Artist
from .models import Album
from .models import Genre
from django.shortcuts import render




def blanket_genres(request):
    all_Genres = Genre.objects.all()
    template = loader.get_template('music/blanket_genres.html')
    context = {
        'all_Genres' : all_Genres, 
    }
    return HttpResponse(template.render(context, request))



def genre_History(request):
    genre_History = Genre.objects.all()
    template = loader.get_template('music/genre_History.html')
    context = {
        'Genre_History' : genre_History, 
    }
    return HttpResponse(template.render(context, request))

def genre_details(request):
    genre_details = Genre.objects.all()
    template = loader.get_template('music/genre_details.html')
    context = {
        'Genre_details' : genre_details, 
    }
    return HttpResponse(template.render(context, request))

def albums(request):
    all_Albums = Album.objects.all()
    template = loader.get_template('music/albums.html')
    context = {
        'all_Albums' : all_Albums, 
    }
    return HttpResponse(template.render(context, request))



def genres(request):
    all_Genres = Genre.objects.all()
    template = loader.get_template('music/genres.html')
    context = {
        'all_Genres' : all_Genres, 
    }
    return HttpResponse(template.render(context, request))

def index(request):
    all_Artists = Artist.objects.all()
    all_Genres = Genre.objects.all()
    template = loader.get_template('music/index.html')
    context = {
        'all_Artists' : all_Artists,
        'all_Genres' : all_Genres, 
    }
    
    return HttpResponse(template.render(context, request))
    
    
def detail(request, Stage_Name): 
    
    return HttpResponse("<h1>List of artists" + str(Stage_Name)+ "</h1>")
    
    
def artists(request):
    all_Artists = Artist.objects.all()
    template = loader.get_template('music/artists.html')
    context = {
        'all_Artists' : all_Artists, 
    }
 
    return HttpResponse(template.render(context, request))   
    
    
def Albums(request):
    all_Albums = Album.objects.all()
    template = loader.get_template('music/albums.html')
    context = {
        'all_Albums' : all_Albums, 
    }
 
    return HttpResponse(template.render(context, request))
   
    
def search(request, context):
  query = request.POST['usr_query']
  print "QUERY: "
  print query
  t = loader.get_template('gtr_site/test_search_results.html')
  c = context({ 'query': query,})
  return HttpResponse(t.render(c))
   
    
    
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                albums = Album.objects.filter(user=request.user)
                return render(request, 'music/login.html', {'albums': albums})
            else:
                return render(request, 'music/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'music/login.html', {'error_message': 'Invalid login'})
    return render(request, 'music/login.html')


# def register(request):
  #  form = UserForm(request.POST or None)
   # if form.is_valid():
      #  user = form.save(commit=False)
      #  username = form.cleaned_data['username']
      #  password = form.cleaned_data['password']
       # user.set_password(password)
       # user.save()
       # user = authenticate(username=username, password=password)
      #  if user is not None:
       #     if user.is_active:
          #      login(request, user)
            #    albums = Album.objects.filter(user=request.user)
             #   return render(request, 'music/index.html', {'albums': albums})
    #context = {
    #    "form": form,
    #}
   # return render(request, 'music/register.html', context) 
    



# class PersonFormView():
#    form_class = UserForm
 #   template_name = 'music/registration_form.html' 
    
 #   def get(self, request):
  #      form = self.form_class(None)
   #     return render(request, self.template_name, {'form' : form})
    #    pass
    
    # def post(self, request):
      #  form = self.form_class(request.POST)
      #  if form.is_valid():
            
         #   person = form.save(commit=False)
            
          #  username = form.cleaned_data['username']
           # password = form.cleaned_data['password']
          #  age = form.cleaned_data['age']
           # country = form.cleaned_data['country']
           # top_genres = form.cleaned_data['top genres']
          #  Spotify_Link = form.cleaned_data['spotify link']
           # SoundCloud_Link = form.cleaned_data['soundcloud link']
          #  Twitter_Link = form.cleaned_data['twitter link']
            
           # person.set_password(password)
           # person.save()
            
          #  user = authenticate(username=username, password=password) 
            
           # if user is not None:
             #   if user.is_active:
               #     login(request, user)
                 #   return redirect('music:index')
                    
                    
      #  return render(request, self.template_name, {'form' : form})   
       # pass 



















