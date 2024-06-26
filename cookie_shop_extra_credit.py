"""
Functions necessary for running a virtual cookie shop.
See README.md for instructions.
Do not run this file directly.  Rather, run main.py instead.
"""
import csv


def bake_cookies(filepath):
    """
    Opens up the CSV data file from the path specified as an argument.
    - Each line in the file, except the first, is assumed to contain comma-separated information about one cookie.
    - Creates a dictionary with the data from each line.
    - Adds each dictionary to a list of all cookies that is returned.

    :param filepath: The path to the data file.
    :returns: A list of all cookie data, where each cookie is represented as a dictionary.
    """
    # write your code for this function below here.
    with open(filepath, mode='r') as file:
        reader = csv.reader(file)
        header = next(reader)
        rows = list(reader)
    result = []
    for row in rows:
        cookie_info = {}
        cookie_info['id'] = int(row[0])
        cookie_info['title'] = row[1]
        cookie_info['description'] = row[2]
        cookie_info['price'] = round(float(row[3][1:]), 2)

        # extar credit
        if row[4] == 'True':
            cookie_info['sugar_free'] = True
        elif row[4] == 'False':
            cookie_info['sugar_free'] = False
        if row[5] == 'True':
            cookie_info['gluten_free'] = True
        elif row[5] == 'False':
            cookie_info['gluten_free'] = False
        if row[6] == 'True':
            cookie_info['contains_nuts'] = True
        elif row[6] == 'False':
            cookie_info['contains_nuts'] = False    

        result.append(cookie_info)

    # print(result)
    return result



def welcome():
    """
    Prints a welcome message to the customer in the format:

      Welcome to the Python Cookie Shop!
      We feed each according to their need.

    """
    # write your code for this function below this line
    print("Welcome to the Python Cookie Shop!")
    print("We feed each according to their need.")

    # === extar credit
    print("We'd hate to trigger an allergic reaction in your body. So please answer the following questions:\n")
    user_needs = {}
    while True:
        allergic_to_nuts = input("Are you allergic to nuts? ")
        if allergic_to_nuts in ['yes', 'y']:
            user_needs['can_intake_nuts'] = False
            break
        elif allergic_to_nuts in ['no', 'n']:
            user_needs['can_intake_nuts'] = True
            break
        else:
            continue
    while True:
        allergic_to_gluten = input("Are you allergic to gluten? ")
        if allergic_to_gluten in ['yes', 'y']:
            user_needs['can_intake_gluten'] = False
            break
        elif allergic_to_gluten in ['no', 'n']:
            user_needs['can_intake_gluten'] = True
            break
        else:
            continue
    while True:
        allergic_to_sugar = input("Do you suffer from diabetes? ")
        if allergic_to_sugar in ['yes', 'y']:
            user_needs['can_intake_sugar'] = False
            break
        elif allergic_to_sugar in ['no', 'n']:
            user_needs['can_intake_sugar'] = True
            break
        else:
            continue

    return user_needs


def display_cookies(cookies, user_needs):
    """
    Prints a list of all cookies in the shop to the user.
    - Sample output - we show only two cookies here, but imagine the output continues for all cookiese:
        Here are the cookies we have in the shop for you:

          #1 - Basboosa Semolina Cake
          This is a This is a traditional Middle Eastern dessert made with semolina and yogurt then soaked in a rose water syrup.
          Price: $3.99

          #2 - Vanilla Chai Cookie
          Crisp with a smooth inside. Rich vanilla pairs perfectly with its Chai partner a combination of cinnamon ands ginger and cloves. Can you think of a better way to have your coffee AND your Vanilla Chai in the morning?
          Price: $5.50

    - If doing the extra credit version, ask the user for their dietary restrictions first, and only print those cookies that are suitable for the customer.

    :param cookies: a list of all cookies in the shop, where each cookie is represented as a dictionary.
    """
    # write your code for this function below this line
    print("Here are the cookies we have in the shop for you:\n")
    for cookie in cookies:
        if user_needs['can_intake_sugar'] == False and cookie['sugar_free'] == False:
            continue
        if user_needs['can_intake_gluten'] == False and cookie['gluten_free'] == False:
            continue
        if user_needs['can_intake_nuts'] == False and cookie['contains_nuts'] == True:
            continue
        print('#'+str(cookie['id'])+' - '+str(cookie['title']+''))
        print(cookie['description']+'')
        print('Price: $'+"{:.2f}".format(cookie['price'])+'\n')


def get_cookie_from_dict(id, cookies):
    """
    Finds the cookie that matches the given id from the full list of cookies.

    :param id: the id of the cookie to look for
    :param cookies: a list of all cookies in the shop, where each cookie is represented as a dictionary.
    :returns: the matching cookie, as a dictionary
    """
    # write your code for this function below this line
    for cookie in cookies:
        if cookie['id'] == id:
            return cookie
    # not find the cookie
    return None


def solicit_quantity(id, cookies):
    """
    Asks the user how many of the given cookie they would like to order.
    - Validates the response.
    - Uses the get_cookie_from_dict function to get the full information about the cookie whose id is passed as an argument, including its title and price.
    - Displays the subtotal for the given quantity of this cookie, formatted to two decimal places.
    - Follows the format (with sample responses from the user):

        My favorite! How many Animal Cupcakes would you like? 5
        Your subtotal for 5 Animal Cupcake is $4.95.

    :param id: the id of the cookie to ask about
    :param cookies: a list of all cookies in the shop, where each cookie is represented as a dictionary.
    :returns: The quantity the user entered, as an integer.
    """
    # write your code for this function below this line
    cookie = get_cookie_from_dict(id, cookies)
    while True:
        quantity = input("My favorite! How many " +
                         cookie['title'] + ' would you like? ')
        if is_val_integer(quantity):
            break
    quantity = int(quantity)
    subtotal = quantity * cookie['price']
    print("Your subtotal for " + str(quantity) + ' ' +
          cookie['title'] + ' is $' + "{:.2f}".format(subtotal))
    return quantity


def is_val_integer(input):
    try:
        int(input)
        return int(input) > 0
    except ValueError:
        return False


def solicit_order(cookies):
    """
    Takes the complete order from the customer.
    - Asks over-and-over again for the user to enter the id of a cookie they want to order until they enter 'finished', 'done', 'quit', or 'exit'.
    - Validates the id the user enters.
    - For every id the user enters, determines the quantity they want by calling the solicit_quantity function.
    - Places the id and quantity of each cookie the user wants into a dictionary with the format
        {'id': 5, 'quantity': 10}
    - Returns a list of all sub-orders, in the format:
        [
          {'id': 5, 'quantity': 10},
          {'id': 1, 'quantity': 3}
        ]

    :returns: A list of the ids and quantities of each cookies the user wants to order.
    """
    # write your code for this function below this line
    result = []
    while True:
        cookie_id = input(
            'Please enter the number of any cookie you would like to purchase: ')
        if cookie_id in ['finished', 'done', 'quit', 'exit']:
            break
        if not is_val_integer(cookie_id):
            continue
        cookie_id = int(cookie_id)
        if get_cookie_from_dict(cookie_id, cookies) is None:
            continue
        quantity = solicit_quantity(cookie_id, cookies)
        result.append({'id': cookie_id, 'quantity': quantity})

    return result


def display_order_total(order, cookies):
    """
    Prints a summary of the user's complete order.
    - Includes a breakdown of the title and quantity of each cookie the user ordereed.
    - Includes the total cost of the complete order, formatted to two decimal places.
    - Follows the format:

        Thank you for your order. You have ordered:

        -8 Animal Cupcake
        -1 Basboosa Semolina Cake

        Your total is $11.91.
        Please pay with Bitcoin before picking-up.

        Thank you!
        -The Python Cookie Shop Robot.

    """
    # write your code for this function below this line
    print('')
    print('Thank you for your order. You have ordered:\n')
    total = 0
    for item in order:
        id = item['id']
        quantity = item['quantity']
        cookie = get_cookie_from_dict(id, cookies)
        title = cookie['title']
        print('-'+str(quantity)+' '+title)
        total = total + quantity * cookie['price']
    print('')
    print('Your total is $'+"{:.2f}".format(total)+'.')
    print('Please pay with Bitcoin before picking-up.\n')
    print('Thank you!')
    print('-The Python Cookie Shop Robot.\n')


def run_shop(cookies):
    """
    Executes the cookie shop program, following requirements in the README.md file.
    - This function definition is given to you.
    - Do not modify it!

    :param cookies: A list of all cookies in the shop, where each cookie is represented as a dictionary.
    """
    # write your code for this function below here.
    user_needs = welcome()
    display_cookies(cookies, user_needs)
    order = solicit_order(cookies)
    display_order_total(order, cookies)
