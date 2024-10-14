import datastorage

#########################################################################
def prompt_for_action():
    """
    Prompts the user to select an action to perform on the inventory.

    The user is given a list of options and is asked to select one by
    entering the corresponding letter. The selected action is then
    returned.

    Returns:
        str: The selected action.
    """
    while True:
        print()
        print("What would you like to do?")
        print()
        print("  A = Add an item to the Inventory.")
        print("  R = Remove an item from the Inventory.")
        print("  C = Generate a report of the current Inventory Levels.")
        print("  O = Generate a report of the inventory items to Re-Order.")
        print("  Q = Quit.")
        print()

        action = input("> ").strip().upper()
        if action == "A": return "ADD"
        if action == "R": return "REMOVE"
        if action == "C": return "INVENTORY_REPORT"
        if action == "O": return "REORDER_REPORT"
        if action == "Q": return "QUIT"

#######################################################################################

def prompt_for_location():
    """
    Prompts the user to select a location.

    The user is given a numbered list of locations to select from and
    is asked to enter the corresponding identifier for the location. The selected location
    code is then returned.

    Returns:
        str: The location code of the selected location.
    """
    while True:
        print()
        print("Select a location:")
        print()
        n = 1
        for code, description in datastorage.locations():
            print("  {}.{} - {}".format(n, code, description))
            n = n + 1

        s = input("> ").strip()
        if s == "": return None

        try:
            n = int(s)
        except ValueError:
            n = -1

        if (n < 1 or n> len(datastorage.locations())):
            print("Invalid Option: {}".format(s))
            continue

        location_code = datastorage.locations()[n-1][0]
        return location_code     


def prompt_for_product():
    """
    Prompts the user to select a product.

    The user is given a numbered list of products to select from and
    is asked to enter the corresponding identifier for the product. The selected product
    code is then returned.

    Returns:
        str: The product code of the selected product.
    """
    while True:
        print()
        print("Select a Product:")
        print()
        n = 1
        for code, description, desired_number in datastorage.products():
            print("  {}.{} - {}".format(n, code, description))
            n = n + 1

        s = input("> ").strip()
        if s == "": return None

        try:
            n = int(s)
        except ValueError:
            n = -1

        if (n < 1 or n > len(datastorage.products())):
            print("Invalid Option: {}".format(s))
            continue

        product_code = datastorage.products()[n-1][0]
        return product_code          


###########################################################################################

def show_report(report):
    print()
    for line in report:
        print(line)
        print()

############################################################################################

def show_error(err_msg):
    print()
    print(err_msg)
    print()
