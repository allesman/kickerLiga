from django.shortcuts import render
from django_object_actions import DjangoObjectActions
from League.lib import KickerLeague
from django.http import HttpResponse
from django.contrib import admin
from League.models import Elo, Game, Player
from django.db import models
from django.db.models import Max    
from django.contrib import admin

a = 0

def custom_titled_filter(title):
    class Wrapper(admin.FieldListFilter):
        def __new__(cls, *args, **kwargs):
            instance = admin.FieldListFilter.create(*args, **kwargs)
            instance.title = title
            return instance
    return Wrapper

class PlayerFilter(admin.SimpleListFilter):
    title = "Player"  # a label for our filter
    parameter_name = "games"  # you can put anything here

    def lookups(self, request, model_admin):
        # This is where you create filter options; we have two:
        return [list(x) for x in zip(Player.objects.values_list('id',flat=True),Player.objects.all())]

    def queryset(self, request, queryset):
        # return all games where the player is either player_1A, player_1B, player_2A or player_2B
        if self.value():
            return queryset.filter(models.Q(player_1A=self.value()) | models.Q(player_1B=self.value()) | models.Q(player_2A=self.value()) | models.Q(player_2B=self.value()))

def scoreboard(request):
    return render(request,"League/scoreboard.html",{})

@admin.register(Elo)
class Scoreboard(admin.ModelAdmin):
    list_display = ("get_rank","get_name",'get_elo','get_kebap_count')
    list_filter=(('player__is_active', custom_titled_filter('Activeness')),)
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
    
    @admin.display(description='elo')
    def get_elo(self, obj, **kwargs):
        return obj.value

    @admin.display(description='dönerschulden')
    def get_kebap_count(self, obj, **kwargs):
        return obj.player.kebap_count
    
    @admin.display(description='spielanzahl')
    def get_match_count(self, obj, **kwargs):
        return obj.player.match_count

@admin.register(Player)
class PlayerAdmin(DjangoObjectActions,admin.ModelAdmin):
    list_display = ('first_name','last_name','email','is_active','match_count')
    list_filter=(('is_active', custom_titled_filter('Activeness')),)
    @admin.action(description="Update Match Counts")
    def update_match_counts(self, request, queryset):
        # update match_count of players
        for player in queryset:
            player.match_count=Game.objects.filter(models.Q(player_1A=player) | models.Q(player_1B=player) | models.Q(player_2A=player) | models.Q(player_2B=player)).count()
            player.save()
    changelist_actions = ('update_match_counts',)

@admin.register(Game)
class GameAdmin(DjangoObjectActions,admin.ModelAdmin):
    # def toolfunc(self, request, obj):
    #     pass
    # list_filter=('player_1A','player_1B','player_2A','player_2B',)
    # Filter by matchday or by player, where player is one filter looking through all 4 player fields 1A, 1B, 2A, 2B
    list_filter=(('matchday', custom_titled_filter('Matchday')),PlayerFilter)

    @admin.action(description="Create new matchday")
    def new_match_day(self, request, queryset):
        KickerLeague.new_match_day()

    @admin.action(description="Delete all unplayed games that have surpassed their deadline")
    def delete_unplayed(self, request, queryset):
        KickerLeague.delete_unplayed()

    changelist_actions = ('new_match_day', 'delete_unplayed')

    list_display = ('matchday','get_team_1','get_score','get_team_2','deadline')
    # list_filter=('player_1A','player_1B','player_2A','player_2B','goal_diff','timestamp')
    def get_short_name(self, player):
        return player.first_name+" "+player.last_name[0]+"."
    @admin.display(description='team 1')
    def get_team_1(self, obj, **kwargs):
        return obj.player_1A.first_name+ " & "+obj.player_1B.first_name
    @admin.display(description='team 2')
    def get_team_2(self, obj, **kwargs):
        return obj.player_2A.first_name+ " & "+obj.player_2B.first_name
    @admin.display(description='score')
    def get_score(self, obj, **kwargs):
        return "" if obj.goal_diff==None else "9 - "+str(9-obj.goal_diff) if obj.goal_diff>0 else str(9+obj.goal_diff)+" - 9"
    def any_player(self, obj):
        return obj.player_1A