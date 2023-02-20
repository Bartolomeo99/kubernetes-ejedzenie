from django.shortcuts import render, redirect
from django.views import View
from store.models.product import Products


class CheckOut(View):
    def post(self, request):
        request.session['cart'] = {}

        return redirect('cart')
