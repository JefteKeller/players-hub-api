from app.models.match_model import MatchModel


def match_serializer(match_id):
    match: MatchModel = MatchModel.query.get(match_id)

    return {
        "game": match.game.game_name,
        "match_winner": match.match_winner.team_name,
        "date": match.date,
        "team_1": match.team_1.team_name,
        "team_2": match.team_2.team_name,
    }
