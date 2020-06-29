#from celery import task
from django.core.mail import send_mail
from .models import Order, OrderItem
from shop.models import Product
#@task
def order_created(order_id):
    """Задача отправки email-уведомлений при успешном оформлении заказа."""
    reg=Order.objects.get(id=order_id)
    ord = OrderItem.objects.filter(order_id=order_id)
    con='От {}\n телефон {}\n\n'.format(reg.first_name,reg.phone)
    mes=''
    for sss in ord:
        message = '"{}" {} шт  по {} грн.\n'.format(sss.product, sss.quantity, sss.price)
        mes = mes + message
    subject = 'Новый заказ № {}'.format(order_id)
    mail_sent = send_mail( subject ,con+mes,'svidin.zp@gmail.com',['svidin.zp@gmail.com'])
    mail_sent2=send_mail( subject , mes,'svidin.zp@gmail.com',[reg.email])
    return mail_sent, mail_sent2