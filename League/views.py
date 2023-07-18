from django.shortcuts import render
from League.lib import KickerLeague
from django.http import HttpResponse

def scoreboard(request):
    return render(request,"League/scoreboard.html",{})