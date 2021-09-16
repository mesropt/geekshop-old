from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'mainapp/index.html')

def products(request):
    return render(request, 'mainapp/products.html')

# def test(request):
#     context = {
#         'title': 'geekshop',
#         'header': 'Добро пожаловать на сайт!',
#         'user': 'Николай',
#         'products': [{'name': 'Худи черного цвета с монограммами adidas Originals', 'price': '6 090,00', },
#                     {'name': 'Синяя куртка The North Face', 'price': 'Синяя куртка The North Face', },
#                     {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': '3 390,00', },
#     ],
#         'products_promo': [{'name': 'Черный рюкзак Nike Heritage', 'price': '1000', },
#     ]
#     }
#     return render(request, 'mainapp/test.html', context)