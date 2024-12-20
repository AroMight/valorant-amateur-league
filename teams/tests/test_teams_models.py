from django.forms import ValidationError
from django.test import TestCase
from teams.models import Team
from matches.models import Match


class TeamsModelTest(TestCase):
    def test_teams_models_raises_an_error_if_three_teams_are_associated(self):

        # Create a Match instance
        match = Match.objects.create()

        # Create two Team instances and associate them with the Match instance
        for _ in range(2):
            Team.objects.create(match=match)

        # Create a third Team instance and associate it with the Match instance
        with self.assertRaises(ValidationError) as cm:
            third_team = Team(match=match)
            third_team.full_clean()

        error = cm.exception

        self.assertIn(f"You can not add this teams to match {match}. This match already has 5 players.", error.messages)

    def test_team_model_str_method(self):
        team = Team.objects.create()
        self.assertEqual(str(team), str(team.uuid))
