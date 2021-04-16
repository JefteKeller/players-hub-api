# // Disabling errors of ORM type due to how SQLAlchemy works
# type: ignore

from app.configurations.database import db

from .user_model import UserModel
from .team_model import TeamModel
from .game_model import GameModel
from .match_model import MatchModel
from .location_model import LocationModel
from .team_user_model import TeamUserModel
