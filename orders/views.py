from django.contrib import messages
from django.shortcuts import render, redirect
from .models import OrderItem
from .forms import OrderCreateForm, ContactForm
from cart.cart import Cart
from .tasks import order_created
from django.core.mail import send_mail

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # очистка корзины
            cart.clear()
            order_created(order.id)
            return render(request, 'orders/order/created.html',
                          {'order': order})
    else:
        form = OrderCreateForm
    return render(request, 'orders/order/create.html',
                  {'cart': cart, 'form': form})

def mail(request):
    if request.method == 'POST':
        form1 = ContactForm(request.POST)
        if form1.is_valid():
            email_subject = 'Сообщение с DHC '
            email_body = "Новое сообщение\n\n" \
                         "Имя отпр.: %s \n" \
                         "E-mail отпр.: %s \n\n" \
                         "Текст: \n" \
                         "%s " % \
                         (form1.cleaned_data['name'], form1.cleaned_data['email'], form1.cleaned_data['message'])
            mal=send_mail(email_subject,email_body,
                      'svidin.zp@gmail.com',['svidin.zp@gmail.com',],fail_silently=True)
            form1 = ContactForm


            return render(request,'shop/base.html',
                  {'form1': form1})
            #else:
                #messages.error(request,"Ошибка отправки")
    else:
        form1 = ContactForm
    return render(request, 'shop/home.html',
                  {'form1': form1})