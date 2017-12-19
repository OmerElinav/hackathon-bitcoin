import requests

SECRET_KEY = "NE4CbeaYN0X4CKFF95Sm62HwXEF6cypP"


def user_stats(user):
    return requests.get("https://api.coinhive.com/user/balance", params={"secret": SECRET_KEY, "name": user}).content.\
               split(":")[-1][:-1]
