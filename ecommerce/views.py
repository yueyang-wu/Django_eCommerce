from django.shortcuts import render

shopping_cart = {}

products = [
    {
        'brand': 'Primal',
        'name': 'Freeze-Dried Nuggets Chicken',
        'size': '14oz',
        'price': '$33.99',
    },
    {
        'brand': 'Stella & Chewy\'s',
        'name': 'Meal Mixers Freeze-Dried Chicken',
        'size': '18oz',
        'price': '$39.99'
    },
    {
        'brand': 'Acana',
        'name': 'Freeze-Dried Patties Chicken',
        'size': '14oz',
        'price': '$30.49'
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
            shopping_cart[product_name] += 1
        else:
            shopping_cart[product_name] = 1

    return render(request, 'ecommerce/home.html', {
        'products': products,
    })

def shoppingcart(request):
    if request.method == 'POST':
        product_name = request.POST["product_name"]
        print(f"delete {product_name} from shopping cart")
        shopping_cart.pop(product_name)

    return render(request, 'ecommerce/shoppingcart.html', {'title': 'Shopping Cart', 'shopping_cart': shopping_cart})
