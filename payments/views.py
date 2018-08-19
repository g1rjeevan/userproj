# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models import Sum

from payments.models import Service, Payment


def execmethod():
    ###----1
    services = Service.objects.all()
    service_total = services.values('b_id').annotate(sum_price=Sum('price'))
    paid_total = Payment.objects.all().values('b_id').annotate(paid_amount=Sum('amount'))
    print ("*****1.Solution**********")
    for service in services:
        service_total_item = next((item for item in service_total if item['b_id'] == service.b_id.id), None)
        paid_amount_item = next((paid_item for paid_item in paid_total if paid_item['b_id'] == service.b_id.id), None)
        print (service, " ", ((service.price * paid_amount_item['paid_amount']) / service_total_item['sum_price']))

    ####-----2

    all_pays = Payment.objects.all()
    payments = all_pays.dates('payment_date', 'month')
    print ("*****2.Solution**********")
    for payment in payments:
        sales = all_pays.filter(payment_date__month=payment.month).aggregate(total_amount=Sum('amount'))
        print (sales, payment.month)

    import datetime
    now = datetime.datetime.now()
    last_month = now.month - 1
    this_year = now.year
    if (now.month == 12):
        this_year = this_year - 1
    last_month_payments = Payment.objects.all().filter(payment_date__month=last_month,
                                                       payment_date__year=this_year).order_by('payment_date')
    print ("*****3.Solution**********, Length " + str(len(last_month_payments)))
    for last_mon_pay in last_month_payments:
        print (vars(last_mon_pay))

    last_month_service = Service.objects.filter(
        b_id__in=last_month_payments.values_list('b_id', flat=True).distinct()).order_by('service_name')

    print ("*****4.Solution**********, Length " + str(len(last_month_service)))
    for last_month_serv in last_month_service:
        print (vars(last_month_serv))
