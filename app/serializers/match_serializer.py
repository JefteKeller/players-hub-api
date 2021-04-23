def match_serializer(match):
    return {
        "id": match.id,
        "game": match.game.game_name,
        "team_1": match.team_1.team_name,
        "team_2": match.team_2.team_name,
        "date": match.date,
        "created_at": match.match_register_date,
        "location_id": match.location_id or "",
        "match_winner_id": match.match_winner_id or "",
    }
