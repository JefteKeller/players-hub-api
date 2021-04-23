from flask import Flask


def init_app(app: Flask):
    from app.views.user_view import bp_user, bp_register, bp_login

    app.register_blueprint(bp_user)
    app.register_blueprint(bp_register)
    app.register_blueprint(bp_login)

    from app.views.team_view import bp_team

    app.register_blueprint(bp_team)

    from app.views.invite_user_view import bp_invite_user

    app.register_blueprint(bp_invite_user)

    from app.views.match_view import bp_match

    app.register_blueprint(bp_match)

    from app.views.location_view import bp_location

    app.register_blueprint(bp_location)

    from app.views.game_view import bp_game

    app.register_blueprint(bp_game)

    from app.views.comment_view import bp_comment

    app.register_blueprint(bp_comment)
