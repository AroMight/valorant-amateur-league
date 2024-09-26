from django.contrib import admin
from .models import Team
from stats.models import Stat


class PlayerInline(admin.StackedInline):

    model = Stat
    fields = [
        "player",
    ]

    def get_queryset(self, request):
        return super().get_queryset(request).select_related("player")

    def get_extra(self, request, obj=None, **kwargs):
        if obj:
            extra_fields = 5 - obj.players.count()
            return max(extra_fields, 0)
        return 5


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):

    list_display = [
        "uuid",
        "match",
    ]

    search_fields = [
        "players",
        "match",
    ]

    list_filter = [
        "players",
        "match",
    ]

    list_select_related = [
        "match__map",
    ]

    inlines = [
        PlayerInline,
    ]
