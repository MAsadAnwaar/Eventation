from django.shortcuts import render , redirect , HttpResponseRedirect


from django.views import  View


class sec(View):
    return_url = None
    def get(self , request):
        
        return redirect('home')