from django.contrib import admin

from League.models import Player
from League.views import PlayerAdmin

# Register your models here.
# admin.site.register(Player, PlayerAdmin)
from django_object_actions import DjangoObjectActions, action

# class GameAdmin(DjangoObjectActions, admin.ModelAdmin):
#     @action(label="Publish", description="Submit this article") # optional
#     def publish_this(self, request, obj):
#         obj.create_match_day()
#     change_actions = ('publish_this', )
