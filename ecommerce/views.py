from django.shortcuts import render

shopping_cart = {}

products = [
    {
        'brand': 'Primal',
        'name': 'Freeze-Dried Nuggets Chicken',
        'size': '14oz',
        'price': '$33.99',
        'image': 'static/images/PPF-FD-Canine-FD-Chicken14-Front_800x.png',
    },
    {
        'brand': 'Stella & Chewy\'s',
        'name': 'Meal Mixers Freeze-Dried Chicken',
        'size': '18oz',
        'price': '$39.99',
        'image': 'static/images/nmzsmhmlercpmdllwnte.png',
    },
    {
        'brand': 'Acana',
        'name': 'Freeze-Dried Patties Chicken',
        'size': '14oz',
        'price': '$30.49',
        'image': 'static/images/DS_ACANA_FDF_Free-Run_Chicken_Front_Right_14oz_NEW_556x800.png',
    }
]

'''
    handle the traffic from the home page
    take in a request argument
    return what we want the user to see when they are sent to this route
'''


def home(request):
    if request.method == 'POST':
        product_name = request.POST["product_name"]
        print("add {} to shopping cart".format(product_name))
        if product_name in shopping_cart:
            print(f"in: {product_name}")
            shopping_cart[product_name] += 1
        else:
            print(f"not in: {product_name}")
            shopping_cart[product_name] = 1

    return render(request, 'ecommerce/home.html', {
        'products': products,
    })


def shoppingcart(request):
    if request.method == 'POST':
        product_name = request.POST["product_name"]
        amount = request.POST["amount"]
        operation = request.POST["operation"]
        if operation == "update":
            print(f"update {product_name} to {amount}")
            shopping_cart[product_name] = int(amount)
        elif operation == "delete":
            print(f"delete {product_name} from shopping cart")
            shopping_cart.pop(product_name)
        else:
            print(f"error: unknown operation {operation}")

    print(shopping_cart)
    return render(request, 'ecommerce/shoppingcart.html', {'title': 'Shopping Cart', 'shopping_cart': shopping_cart})
