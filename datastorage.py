import json
import os.path

def init():
    """Used to initialize the data storage module"""
    _load_items()

def items():
    """
    Returns a list of all stored items

    Returns:
        list: All stored items, where each item is a tuple (product_code, location_code)
    """
    
    global _items
    return _items

def products():
    """Returns a list of all products.

    Returns:
        list: All products, where each product is a tuple (product_code, product_name)
    """
    global _products
    return _products

def locations():
    """
    Returns a list of all locations.

    Returns:
        list: A list of locations, where each location is a tuple (location_code, location_name)
    """
    global _locations
    return _locations
 

def add_item(product_code, location_code):
    global _items
    _items.append((product_code, location_code))
    _save_items()


def remove_item(product_code, location_code):
    global _items
    for i in range(len(_items)):
        prod_code, loc_code = _items[i]
        if prod_code == product_code and loc_code == location_code:
            del _items[i]
            _save_items()
            return True
        
    return False    

def set_products(products):
    """
    Sets the list of products.

    Args:
        products (list): A list of products, where each product is a tuple (product_code, product_name)
    """
    global _products
    _products = products  

def set_locations(locations):

    global _locations
    _locations = locations

def _save_items():
    """Saves the items to the file."""
    
    global _items
    """The list of items to save."""
    
    f = open("items.json", "w")
    """The file to save the items to."""
    
    f.write(json.dumps(_items))
    """Convert the list of items to a JSON string and write it to the file."""
    
    f.close()
    """Close the file."""

def _load_items():
    """
    Loads the items from the file.

    If the file does not exist, an empty list is used.
    """
    global _items
    if os.path.exists("items.json"):
        f = open("items.json", "r")
        # Read the JSON string from the file and convert it to a list of items
        _items = json.loads(f.read())
        f.close()

    else:
        # The file does not exist, so use an empty list
        _items = []


      

