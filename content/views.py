from django.shortcuts import render , HttpResponse 
from django.http import HttpResponseRedirect
from .forms import *
from django.contrib import messages



def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid:
            form.save()
            messages.add_message(request , messages.SUCCESS,'Wellcome Yo My Site ')
            
        else:
            messages.add_message(request , messages.ERROR,'The information entered is incorrect')
            
    form =  ContactForm()   
    return render (request , 'content/contact.html' , {'form': form })

def newslette_view(request):
    if request.method == 'POST':
        form = NewsLetteForm(request.POST)
        if form.is_valid(): 
            form.save()
            return HttpResponseRedirect('/') 
        else:    
            return HttpResponseRedirect('/')



def test_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('DONE')
        else:
             return HttpResponse('NOT VALID')           
    form = ContactForm()
    return render(request , 'test.html' , {'form' : form})
    