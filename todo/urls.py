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
from django.contrib import admin
from django.urls import path
from task.views import AddtaskView, IndexView, LoginView, RegView,TasklistView,TaskDetailView,TaskDeleteView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("home/",IndexView.as_view()),
    path("login/",LoginView.as_view()),
    path("reg/",RegView.as_view()),
    path("addtask/",AddtaskView.as_view(),name="todo-add"),
    path("listtask/",TasklistView.as_view(),name="todo-list"),
    path("taskdetail/<int:id>",TaskDetailView.as_view(),name="todo-detail"),
    path("taskdelete/<int:id>",TaskDeleteView.as_view(),name="todo-delete"),



]
