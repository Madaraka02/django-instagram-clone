from django.shortcuts import render, redirect
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

def like(request,pk):
    # get post by id

    # is_disliked =False
    # for dislike in post.dislikes.all():

    #   if is_disliked == request.user: -> user has already disliked post
    #       is_disliked =True
    #       break


    # is_liked =False
    # for like in post.likes.all():
    #   if like == request.user: 
    #       is_liked =True
    #       break
    # if not is_liked:
    #       post.likes.add(request.user)
    # if is_liked:
    #       post.likes.remove(request.user)

    pass

def dislike(request,pk):
    # get post by id
    # check if user has already liked the post if true remove the like
    # is_liked =False
    # for like in post.likes.all():
    #   if like == request.user: 
    #       is_liked =True
    #       break

    # if is_disliked:
    #       post.dislikes.remove(request.user)

    # if is_liked:
    #       post.likes.remove(request.user)

    # is_disliked =False
    # for dislike in post.dislikes.all():

    #   if is_disliked == request.user: -> user has already disliked post
    #       is_disliked =True
    #       break
    # if not is_disliked:
    #       post.dislikes.add(request.user)
    # if is_disliked:
    #       post.dislikes.remove(request.user)
    # next = request.POST.get('next','/)
    # return HttpResponseRedirect(next)


    pass
# create urls for like and dislike : post/<int:pk>/like
# template
# <form method=post action={url 'like' post.pk}> 
# csrf
# <input type=hidden name=next value={{request.path}}/>
# <btn submit>Like {{post.likes.all.count}}</btn>
# </form>