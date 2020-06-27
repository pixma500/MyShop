from django.shortcuts import render, get_object_or_404
from .models import Category, Product, Tag
from cart.forms import CartAddProductForm


# Create your views here.
# def home(request):
# return render(request, 'shop/home.html')

def product_list(request, category_slug=None, ):
    tags = Tag.objects.all()
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products,
                   'tags': tags,
                   })

def product_sale(request):
    prod_sale= Product.objects.all().exclude(sale=0)
    return render(request, 'shop/product/sale.html',
                  { 'prod_sale': prod_sale,})

def tag_list(request, tags_slug=None, ):
    tags_all = Tag.objects.all()
    tag = None
    products = Product.objects.filter(available=True)
    prod_sale = Product.objects.all().exclude(sale=0)
    if tags_slug:
        tag = get_object_or_404(Tag, slug=tags_slug)
        products = products.filter(tags=tag)
    return render(request, 'shop/home.html',
                  {'tags_all': tags_all,
                   'products': products,
                   'tag': tag,
                   'prod_sale': prod_sale,})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})
