from django.shortcuts import render
from League.lib import KickerLeague
from django.http import HttpResponse
from django.contrib import admin
from League.models import Elo, Player
from django.db import models
from django.db.models import Max
a = 0

def scoreboard(request):
    return render(request,"League/scoreboard.html",{})

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','email','is_active','preffered_position')

@admin.register(Elo)
class Scoreboard(admin.ModelAdmin):
    list_display = ("get_rank","get_name",'value','timestamp')
    # list_filter=('player',)
    def get_queryset(self, request):
        global a
        a=0
        # elos = [Elo.objects.filter(player=player).order_by('-timestamp').first() for player in Player.objects.all()]
        #elos = {k:v for k,v in zip([elo.player.first_name for elo in elos], [elo.value for elo in elos])}
        #elos = {k:v for k, v in sorted(elos.items(), key=lambda item: item[1],reverse=True)

        # return Elo.objects.filter(timestamp__in=Elo.objects.values('player').annotate(max_id=models.Max('id')).values('max_id'))
        # return Elo.objects.filter(value=1000)
        # return the latest elo for each player
        # return Elo.objects.annotate(test=Max('value')).order_by('-test')
        return Elo.objects.filter(id__in=Elo.objects.values('player').annotate(max_id=models.Max('id')).values('max_id')).order_by('-value')
    
    @admin.display(description='name')
    def get_name(self, obj, **kwargs):
        return obj.player.first_name+" "+obj.player.last_name
    
    @admin.display(description="rank")
    def get_rank(self, obj, **kwargs):
        global a
        a+=1
        return a