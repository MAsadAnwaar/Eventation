from operator import concat
from django.shortcuts import render, redirect
from django.views import  View


from store.forms import contactForm
class submit(View):
    return_url = None
    def get(self , request):
        form = contactForm(request.GET)
        print("Hi! I'm Here")
        form.save()
        return render(request,"first.html")
        
        
# def submit(request):
    