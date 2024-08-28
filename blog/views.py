from django.shortcuts import render , get_object_or_404 , redirect
from .models import Post , Comment , Category
from django.core.paginator import Paginator , EmptyPage , PageNotAnInteger
from blog.forms import CommentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.db.models import Count

 
def blog_home (request , **kwargs):    
    posts = Post.objects.filter(status = 1)
    categories = categories = (
        Category.objects.annotate(num_posts=Count('post'))
        .filter(num_posts__gt=0)  
        .order_by('-num_posts')[:4]  
    )
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name=kwargs ['cat_name'])
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username = kwargs['author_username'])
    if kwargs.get('tag_name') != None:
        posts = posts.filter(tags__name__in= [kwargs['tag_name']])
    posts = Paginator(posts , 3)
    try:
        
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
        
    except PageNotAnInteger: 
        posts = posts.get_page(1)    
    except EmptyPage: 
        posts = posts.get_page(1)    
    context = {'posts' : posts , 'categories' : categories}
    return render (request , 'blog/blog_home.html' , context)
 


def blog_single(request , pk):

    if request.method == 'POST' :
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request , messages.SUCCESS,' Comment Done')       
        else:
            messages.add_message(request , messages.ERROR,' Your Comment didnt submiter ')
            
    post = Post.objects.get(id = pk , status = 1 )
    categories = Category.objects.annotate(num_posts=Count('post'))
    if not post.login_require:
                comments = Comment.objects.filter(post=post.id , approveh=True)
                posts = get_object_or_404(Post,id=pk) 
                form = CommentForm()
                context = {'posts' : posts , 'comments':comments , 'form':form , 'categories' : categories}
                return render (request , 'blog/blog-single.html' , context)
    else:
        if request.user.is_authenticated:
                comments = Comment.objects.filter(post=post.id , approveh=True)
                posts = get_object_or_404(Post,id=pk)
                form = CommentForm()
                context = {'posts' : posts , 'comments':comments , 'form':form , 'categories' : categories}
                return render (request , 'blog/blog-single.html' , context)
        else:
                return HttpResponseRedirect(reverse('accounts:login'))

def blog_category(request , cat_name):
    posts = Post.objects.filter(status = 1)
    posts = posts.filter(category__name=cat_name)
    context = {'posts' : posts}
    return render (request , 'blog/blog-home.html' , context)

def blog_search(request):
    posts = Post.objects.filter(status = 1)  
    
    if request.method == "GET":
        if s :=  request.GET.get('s'):       
            posts = posts.filter(content__contains = s ) 
    context = {'posts' : posts}
    return render (request , 'blog/blog-home.html' , context)

