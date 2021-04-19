from app.models.match_model import MatchModel
from app.models.team_model import TeamModel
from app.models.game_model import GameModel


def match_serializer(match_id):
    match: MatchModel = MatchModel.query.get(match_id)
    team_1: TeamModel = TeamModel.query.filter_by(id=match.team_id_1).first()
    team_2: TeamModel = TeamModel.query.filter_by(id=match.team_id_2).first()
    match_winner: TeamModel = TeamModel.query.filter_by(
        id=match.match_winner_id
    ).first()
    game: GameModel = GameModel.query.filter_by(id=match.game_id).first()

    return {
        "game": game.game_name,
        "match_winner": match_winner.team_name,
        "date": match.date,
        "team_1": team_1.team_name,
        "team_2": team_2.team_name,
    }
