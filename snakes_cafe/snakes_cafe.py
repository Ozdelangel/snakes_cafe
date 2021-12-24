food_items = [
    {
        "name": "Wings",
        "count": 0
    },
    {
        "name": "Cookies",
        "count": 0
    },
    {
        "name": "Spring Rolls",
        "count": 0
    },
    {  "name":"Salmon",
        "count": 0 
    },
    {
        "name": "Steak",
        "count": 0
    },
    {
        "name": "Meat Tornado",
        "count": 0
    },
    {
        "name": "A Literal Garden",
        "count": 0
    },
    {
        "name": "Ice Cream",
        "count": 0
    },
    {
        "name": "Cake",
        "count": 0
    },
    {
        "name": "Pie",
        "count": 0
    },
    {
        "name": "Coffee",
        "count": 0
    },
    {
        "name": "Tea",
        "count": 0
    },  
    {
        "name": "Unicorn Tears",
        "count": 0
    },
]


def menu():
        print(f'''
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
    ''')
  
   
    
    

def handle_order():
    for food in food_items:
        if food["name"] == order:
            food["count"] += 1
        if food["count"] > 1:
           food["count"] += 1
        else:
            menu()
        
        order_name = food["name"]
        food_count = food["count"]
        print(f"{food_count} of {order_name}  has been added")

if __name__ == "__main__":

    order = ""
    menu()
    handle_order()
    order = input("> ")
    while order != "quit" and order!= "q":
        print(order)
        menu()
        order = input("> ")
        

    
        

