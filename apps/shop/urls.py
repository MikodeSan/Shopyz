from django.urls import path

from .views import order


app_name = "order"

urlpatterns = [
    path("", order.index, name="index"),
    path("cart/", order.add_to_cart, name="cart"),
    path("order/<int:order_id>/", order.detail, name="detail"),
    # # ex: /polls/5/results/
    # path("<int:question_id>/results/", views.results, name="results"),
    # # ex: /polls/5/vote/
    # path("<int:question_id>/vote/", views.vote, name="vote"),
]
