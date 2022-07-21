from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate
from django.contrib.auth import login
from .forms import *
from .models import *

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

def userProfile(request, id):
    profile = get_object_or_404(Profile, id=id)

    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            prof = form.save(commit = False)
            prof.user = request.user
            prof.save()
            return redirect('profile', id=id)




    followers = profile.followers.all()
    no_of_followers = len(followers)



    if len(followers) == 0:
        is_following = False

    for follower in followers:
        if follower == request.user:
            is_following=True
            break
        else:
            is_following=False


    user = profile.user

    context = {
        'profile':profile,
        'user':user,
        'no_of_followers':no_of_followers,
        'is_following':is_following,
        'form':form,
    }
    return render(request, 'Posts/profile.html', context)      

def follow(request, id):

    profile = get_object_or_404(Profile, id=id)
    profile.followers.add(request.user)
    return redirect('profile', profile.id)
    

def unfollow(request, id):

    profile = get_object_or_404(Profile, id=id)
    profile.followers.remove(request.user)
    return redirect('profile', profile.id)

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