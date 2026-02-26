# chat/utils.py
def format_user_display(user):
    first_name = user.first_name
    year = "IBDP1" if getattr(user, "dp_year", None) == 1 else "IBDP2"
    return f"{first_name} ({year})"