from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect

from users.models import *
from .forms import *
from .models import *

# Create your views here.
def home(request):
    profiles = Profile.objects.all().order_by('-id')[:10]
    posts = Post.objects.all().order_by('-id')


    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            post.author = request.user
            post.save()
            return redirect('home')


    context ={
        'profiles':profiles,
        'form':form,
        'posts':posts,
    }
    return render(request, 'Posts/index.html', context)


def postdetail(request, id):
    # get post
    
    # post model add likes and dislikes manytomanyrelated_name=likes/dislike
    # 
    pass    

def like(request,id):
    # get post by id
    post = get_object_or_404(Post, id=id)

    is_disliked =False
    for dislike in post.dislikes.all():

        if dislike == request.user: # user has already disliked post
            is_disliked =True
            break


    is_liked =False
    for like in post.likes.all():
        if like == request.user: 
            is_liked =True
            break
    if not is_liked:
        post.likes.add(request.user)
    if is_liked:
        post.likes.remove(request.user)

    next = request.POST.get('next','/')

    return redirect('home')
    

def dislike(request,id):
    # get post by id
    post = get_object_or_404(Post, id=id)
    # check if user has already liked the post if true remove the like
    is_liked =False
    for like in post.likes.all():
        if like == request.user: 
            is_liked =True
            break

    # if is_disliked:
    #     post.dislikes.remove(request.user)

    if is_liked:
        post.likes.remove(request.user)

    is_disliked =False
    for dislike in post.dislikes.all():

        if dislike == request.user: # user has already disliked post
            is_disliked =True
            break
    if not is_disliked:
        post.dislikes.add(request.user)
    if is_disliked:
        post.dislikes.remove(request.user)
    next = request.POST.get('next','/')

    return redirect('home')


# create urls for like and dislike : post/<int:pk>/like
    # <!-- action={% url 'dislike' post.pk %} -->
