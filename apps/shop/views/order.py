from django.http import Http404
from django.shortcuts import render, get_object_or_404

from ..models import Order, ShopOrder, Item, Payment, Shop, ShopProduct, Product


def index(request):
    latest_order_list = Order.objects.order_by("-order_date")[:5]

    context = {"latest_order_list": latest_order_list}
    return render(request, "orders/index.html", context)


def add_to_cart(request):
    context = {}
    if request.method == "POST":
        latest_order_list = Order.objects.order_by("-order_date")[:5]
        context = {"latest_order_list": latest_order_list}
        template = "orders/index.html"

    elif request.method == "GET":
        template = "orders/order.html"

    return render(request, template, context)


def detail(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    return render(request, "orders/details.html", {"order": order})
    # return HttpResponse("You're looking at order %s." % order_id)


# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)


# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)
