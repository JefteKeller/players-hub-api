def get_user_update_data(data: dict[str, str]) -> dict[str, str]:
    """Takes a dict with data from a request to the API that does not need validations,
    and returns a dict with only the valid keys.

    Args:
        data (dict): data from a request JSON.

    Returns:
        dict: data to update user.
    """

    new_nickname = data.get("nickname")
    new_first_name = data.get("first_name")
    new_last_name = data.get("last_name")
    new_biography = data.get("biography")

    new_data = dict(
        nickname=new_nickname,
        first_name=new_first_name,
        last_name=new_last_name,
        biography=new_biography,
    )
    return {key: value for key, value in new_data.items() if value}
