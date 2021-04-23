from app.models.match_model import MatchModel


def match_serializer(match):
    return {
        "game": match.game.game_name,
        "date": match.date,
        "team_1": match.team_1.team_name,
        "team_2": match.team_2.team_name,
    }
