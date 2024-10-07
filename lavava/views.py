from django.db.models import Count, F, Q, Sum
from django.views.generic import TemplateView
from players.models import Player
from utils import calc_kda, calc_win_ratio


class LandingPageView(TemplateView):
    template_name = "lavava/landing_page.html"


class HomeView(TemplateView):
    template_name = "lavava/home.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        players = (
            Player.objects.prefetch_related("stats")
            .select_related("tier", "main_agent")
            .annotate(
                wins=Count(
                    "teams", filter=Q(teams__matches__winner__id=F("teams__id"))
                ),
                losses=Count(
                    "teams", filter=~Q(teams__matches__winner__id=F("teams__id"))
                ),
                mvp=Count("stats", filter=Q(stats__mvp=True)),
                ace=Count("stats", filter=Q(stats__ace=True)),
            )
            .annotate(
                total_kills=Sum("stats__kills"),
                total_deaths=Sum("stats__deaths"),
                total_assists=Sum("stats__assists"),
            )
        )

        for player in players:
            player.points = (player.mvp + player.ace) + player.wins * 3
            player.winratio = calc_win_ratio(
                wins=player.wins,
                losses=player.losses,
            )
            player.kda = calc_kda(
                kills=player.total_kills,
                assists=player.total_assists,
                deaths=player.total_deaths,
            )
        players = sorted(players, key=lambda p: (p.points, p.mvp, p.ace), reverse=True)
        ctx["players"] = players
        return ctx
