def menu():
    welcome_menu = '''
    **************************************
    **    Welcome to the Snakes Cafe!   **
    **    Please see our menu below.    **
    **
    ** To quit at any time, type "quit" **
    **************************************

    Appetizers
    ----------
    Wings
    Cookies
    Spring Rolls

    Entrees
    -------
    Salmon
    Steak
    Meat Tornado
    A Literal Garden

    Desserts
    --------
    Ice Cream
    Cake
    Pie

    Drinks
    ------
    Coffee
    Tea
    Unicorn Tears

    ***********************************
    ** What would you like to order? **
    ***********************************
    '''
    
    print(f'{welcome_menu}')

foods = [
    {
        "name": "Appetizers",
        "Appetizers": [
            "Wings",
            "Cookies",
            "Spring Rolls",
        ],
    },
     {  "name":"Entrees",
        "Entrees": [
            "Salmon",
            "Steak",
            "Meat Tornado",
            "A Literal Garden",
        ],
    },
    {
        "name": "Desserts",
        "Desserts": [
            "Ice Cream",
            "Cake",
            "Pie",
        ],
    },
     {
         "name": "Drinks",
        "Drinks": [
            "Coffee",
            "Tea",
            "Unicorn Tears",
        ],
    },
]

def order_something(food_index):
    food = foods[food_index]
    order = False
    items = foods['Appetizers', 'Entrees', 'Desserts', 'Drinks']
    order_up = 










if __name__ == "__main__":
    menu()
    customer_order = input('type in your order> ')
    response = ""
    while response != "quit":
