"""
A virtual cookie shop.
Do not modify this file.
"""

from pathlib import Path
import cookie_shop

# get data from the CSV file into a list
filepath = Path(
    "data/cookies.csv"
)  # create a file path in a way that is both Mac- and Windows- compatible
list_of_cookies = cookie_shop.bake_cookies(filepath)

# open the cookie shop with the cookies read from the file
# this must run the rest of the program as documented
cookie_shop.run_shop(list_of_cookies)




# ======= extra credit =========
# from pathlib import Path
# import cookie_shop_extra_credit

# # get data from the CSV file into a list
# filepath = Path(
#     "data/cookies_extra_credit.csv"
# )  # create a file path in a way that is both Mac- and Windows- compatible
# list_of_cookies = cookie_shop_extra_credit.bake_cookies(filepath)

# # open the cookie shop with the cookies read from the file
# # this must run the rest of the program as documented
# cookie_shop_extra_credit.run_shop(list_of_cookies)