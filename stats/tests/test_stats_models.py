from django.test import TestCase
from django.core.exceptions import ValidationError
from stats.models import Stat
from teams.models import Team
from players.models import Player


class TestStatModel(TestCase):

    def test_stats_get_kda_method(self):
        """Test the get_kda method of the Stat model."""

        # Test the case where the player has deaths
        stat = Stat(kills=10, deaths=5, assists=5)
        self.assertEqual(stat.get_kda(), 3.0)

        # Test the case where the player has no deaths
        stat = Stat(kills=10, deaths=0, assists=5)
        self.assertEqual(stat.get_kda(), 15.0)

        # Test the case where the player has no kills or assists
        stat = Stat()
        self.assertEqual(stat.get_kda(), None)

    def test_stats_clean_players_method_raises_error_if_it_has_too_many_players(self):

        # Create a team with 5 players
        team = Team.objects.create()
        for i in range(5):
            player = Player.objects.create_user(
                username=f"player{i}", password="password"
            )
            Stat.objects.create(player=player, team=team)

        # Test if a ValidationError is raised when trying to add a sixth player
        with self.assertRaises(ValidationError):
            player = Player.objects.create(username="new_player", password="password")
            stat = Stat(player=player, team=team)
            stat.full_clean()

    def test_stats_clean_players_methods_raises_error_if_player_is_already_in_team(
        self,
    ):

        # Create a team with 4 players
        team = Team.objects.create()
        for i in range(4):
            player = Player.objects.create_user(
                username=f"player{i}", password="password"
            )
            Stat.objects.create(player=player, team=team)

        # Test if a ValidationError is raised when trying
        # to add a player that is already in the team
        with self.assertRaises(ValidationError):
            stat = Stat(player=player, team=team)
            stat.full_clean()
