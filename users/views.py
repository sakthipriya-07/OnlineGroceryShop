from itertools import product

from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template.context_processors import csrf
from django.utils import timezone
from django.views.generic import ListView

from cart.forms import CartAddProductForm
from orders.models import Order
from products.filter import ProductFilter
from products.forms import CategoryForm
from products.models import Category, Product
from .models import *
from .forms import *


now = timezone.now()


def home(request):
    return render(request, 'onlinegrocery/onlinegrocery_homepage.html',
                  {'users': home})


def register_customer(request):
    if request.method == 'POST':
        form = CustomerSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            if request.user.is_superuser:
                return redirect('users:customer_list')
            else:
                return render(request, 'registration/registration_done.html')
    args = {}
    args.update(csrf(request))
    args['form'] = CustomerSignUpForm()
    return render(request, 'registration/customer_registration_form.html', args)


@login_required
def edit_customer(request, pk):
    customer = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        # update
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.save()
            return redirect('products:product_list')
    else:
        # edit
        form = CustomerForm(instance=customer)
    return render(request, 'registration/customer_edit.html', {'form': form})


def customer_list(request):
    customers = User.objects.filter(is_customer=True)
    return render(request, 'customer_list.html',
                  {'customers': customers})


def about(request):
    return render(request, 'onlinegrocery/about_page.html',
                  {'about': about})


def faq(request):
    return render(request, 'onlinegrocery/faq_page.html',
                  {'faq': faq})


def login(request):
    return render(request, 'registration/login.html',
                  {'login': login})







