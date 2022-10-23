"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unicodedata import name
from django.contrib import admin
from django.urls import path
# from task.views import AddtaskView, IndexView, LoginView, RegView,TasklistView,TaskDetailView,TaskDeleteView,RegistrationView
from task import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("home/",views.IndexView.as_view()),
    path("login/",views.LoginView.as_view()),
    path("reg/",views.RegView.as_view()),
    path("addtask/",views.AddtaskView.as_view(),name="todo-add"),
    path("listtask/",views.TasklistView.as_view(),name="todo-list"),
    path("taskdetail/<int:id>",views.TaskDetailView.as_view(),name="todo-detail"),
    path("taskdelete/<int:id>",views.TaskDeleteView.as_view(),name="todo-delete"),
    path("accounts/Register",views.RegistrationView.as_view(),name="todo-register"),
    path("",views.LogView.as_view(),name="sign-in"),
    path("accounts/signout",views.sign_out,name="sign-out"),
    path("taskupdate/<int:id>",views.TaskUpdateView.as_view(),name="todo-update"),




]
