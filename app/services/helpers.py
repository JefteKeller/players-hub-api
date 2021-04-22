from faker import Faker

fake = Faker()

populate_users = [
    {
        "nickname": "ZezinhoGameplays23",
        "first_name": "Alberto",
        "last_name": "Neves",
        "email": "bebeto@gmail.com",
        "password": "senh@123",
        "biography": fake.text()[:100],
    },
    {
        "nickname": "AlbertoRoberto",
        "first_name": "José",
        "last_name": "de Abreu",
        "email": "zezedeabreu@hotmail.com",
        "password": "senh@123",
        "biography": fake.text()[:100],
    },
    {
        "nickname": "OMamaGanso",
        "first_name": "Patrick",
        "last_name": "Junior",
        "email": "juninho@gmail.com",
        "password": "senh@123",
        "biography": fake.text()[:100],
    },
    {
        "nickname": "PrincessDuMal",
        "first_name": "Isabela",
        "last_name": "Almeida",
        "email": "belaalmeida@yahoo.com",
        "password": "senh@123",
        "biography": fake.text()[:100],
    },
    {
        "nickname": "TheFlash",
        "first_name": "João",
        "last_name": "Zika",
        "email": "JZika@yahoo.com",
        "password": "senh@123",
        "biography": fake.text()[:100],
    },
]

populate_teams = [
    {
        "team_name": "Os Brabíssimos",
        "team_description": fake.text()[:50],
        "owner_id": 1,
    },
    {
        "team_name": "Chama no dale",
        "team_description": fake.text()[:50],
        "owner_id": 2,
    },
    {
        "team_name": "Xesquedele",
        "team_description": fake.text()[:50],
        "owner_id": 3,
    },
    {
        "team_name": "Fogo no Parquinho",
        "team_description": fake.text()[:50],
        "owner_id": 4,
    },
    {
        "team_name": "Heroes of Marvel",
        "team_description": fake.text()[:50],
        "owner_id": 5,
    },
]

populate_games = [
    {
        "game_name": "League of Legends",
        "game_type": "Online",
        "game_description": fake.text()[:50],
    },
    {
        "game_name": "Futebol",
        "game_type": "Físico",
        "game_description": fake.text()[:50],
    },
    {
        "game_name": "Xadrez",
        "game_type": "Físico",
        "game_description": fake.text()[:50],
    },
]

populate_matches = [
    {
        "match_winner_id": 1,
        "team_id_1": 1,
        "team_id_2": 2,
        "date": "06/06/21",
        "game_id": 1,
        "location_id": 1,
    },
    {
        "match_winner_id": 3,
        "team_id_1": 1,
        "team_id_2": 3,
        "date": "25/04/21",
        "game_id": 3,
        "location_id": 2,
    },
    {
        "match_winner_id": 1,
        "team_id_1": 1,
        "team_id_2": 4,
        "date": "30/03/21",
        "game_id": 3,
        "location_id": 3,
    },
    {
        "match_winner_id": 3,
        "team_id_1": 2,
        "team_id_2": 3,
        "date": "24/10/21",
        "game_id": 1,
        "location_id": 1,
    },
    {
        "match_winner_id": 4,
        "team_id_1": 2,
        "team_id_2": 4,
        "date": "12/01/21",
        "game_id": 2,
        "location_id": 2,
    },
    {
        "match_winner_id": 4,
        "team_id_1": 3,
        "team_id_2": 4,
        "date": "05/04/21",
        "game_id": 1,
        "location_id": 3,
    },
    {
        "match_winner_id": 5,
        "team_id_1": 1,
        "team_id_2": 5,
        "date": "05/09/21",
        "game_id": 1,
        "location_id": 3,
    },
]

populate_locations = [
    {
        "location_name": "Sua casa",
        "location_phone": "Seu Telefone",
    },
    {
        "location_name": "Campo do Joquinha",
        "location_phone": "(41) 3558-4178",
    },
    {
        "location_name": "Clube de Xadrez do Jefte",
        "location_phone": "(41) 98514-1317",
    },
]

populate_teams_users = [
    {
        "user_id": 1,
        "team_id": 2,
    },
    {
        "user_id": 1,
        "team_id": 5,
    },
    {
        "user_id": 3,
        "team_id": 3,
    },
    {
        "user_id": 3,
        "team_id": 1,
    },
    {
        "user_id": 4,
        "team_id": 4,
    },
]
