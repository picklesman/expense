from django.shortcuts import render
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
# Create your views here.
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login')
