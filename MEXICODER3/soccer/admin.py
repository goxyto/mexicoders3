from django.contrib import admin
from models import League, Club, Coach, Player

class LeagueAdmin(admin.ModelAdmin):
    pass
    #TODO: add code

class ClubAdmin(admin.ModelAdmin):
    pass
    #TODO: add code

class CoachAdmin(admin.ModelAdmin):
    pass
    #TODO: add code

class PlayerAdmin(admin.ModelAdmin):
    pass
    #TODO: add code

admin.site.register(League, LeagueAdmin)
admin.site.register(Club, ClubAdmin)
admin.site.register(Coach, CoachAdmin)
admin.site.register(Player, PlayerAdmin)
