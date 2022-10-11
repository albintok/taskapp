from django.shortcuts import render
from django.views.generic import View

# Create your views here.
class IndexView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"index.html")

class LoginView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"login.html")

class RegView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"reg.html")

class AddtaskView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"addtask.html")




