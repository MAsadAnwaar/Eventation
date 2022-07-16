from django.shortcuts import render , redirect , HttpResponseRedirect

from django.contrib.auth.hashers import  check_password
from store.models.customer import Customer
from django.views import  View


class about(View):
    return_url = None
    def get(self , request):
        
        return render(request , 'about.html')