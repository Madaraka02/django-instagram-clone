from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login
from .forms import *

# Create your views here.

# register view
	# user_form = UserForm(instance=request.user)
	# profile_form = ProfileForm(instance=request.user.profile)
def registerView(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request, user)
            return redirect('home')



            # username = form.cleaned_data.get('username')
            # password = form.cleaned_data.get('password')
            # user = authenticate(request, username=username, password=password)

            # if user is not None:
            #     login(request, user)
            #     return redirect('home')

    context={
        'form':form,
    }   
    return render(request, 'registration/registration.html', context)     

def follow(request, pk):
    # get profile using id
    # profile.followers.add(request.user)
    # redirect
    pass

def unfollow(request, pk):
    # get profile using id
    # profile.followers.remove(request.user)
    # redirect
    pass

def profile(request, pk):
    # get profile of current using pk
    # user = profile.user
    # followers = profile.followers.all()
    # no_of_followers = len(followers)-pass to context
    # if len(follower) == 0:
    #       is_following = False
    # for follower in followers:
    #     if follower == request.user:
    #         is_following=True
    #         break
    #     else:
    #         is_following=False    
    # pass is_following to context
    # redirect
    # template
    # profile/<int:pk>/follow/-url
    # {% if user is request.user %}
    # <p>{{no_of_followers}}</p>
    # else : 
    # {% if is_following %} 
    # <form meth=post action={url 'unfollow' profile.pk}> 
    # {% csrf_token %} <btn t=submit>unfollow</btn></form>
    # {% else %}
    # <form meth=post action={url 'follow' profile.pk}> 
    pass