from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View


from store.models.product import Product
from store.models.orders import Order

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


class CheckOut(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))
        print(address, phone, customer, cart, products)

        for product in products:
            print(cart.get(str(product.id)))
            order = Order(customer=Customer(id=customer),
                          product=product,
                          price=product.price,
                          address=address,
                          phone=phone,
                          quantity=cart.get(str(product.id)))
            order.save()
        request.session['cart'] = {}
        # email_user = ('eshopmart33@gmail.com')
        # email_password = ('swagmradesi')
        # print("Login Successfully")
        # email_send = ('asadattal58@gmail.com')

        # subject = ("E-Shop Mart")

        # msg = MIMEMultipart()
        # msg['From'] = email_user
        # msg['To'] = email_send
        # msg['Subject'] = subject

        # body = ('Bakra lab gaya ja bas ja ka hun order complete kero paji')
        # msg.attach(MIMEText(body,'plain'))

        # text = msg.as_string()
        # server = smtplib.SMTP('smtp.gmail.com',587)
        # server.starttls()
        # server.login(email_user,email_password)


        # server.sendmail(email_user,email_send,text)
        # server.quit()
        # print("Mail Send Success")

        return redirect('cart')
