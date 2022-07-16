from django.shortcuts import render , redirect , HttpResponseRedirect


from django.views import  View


class home(View):
    return_url = None
    def get(self , request):
        
        return render(request , 'first.html')


        