from itertools import product
from unicodedata import category

from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from django.utils import timezone
from django.views.generic import ListView

from .filter import ProductFilter
from .models import Category, Product
from users.models import Customer, User
from orders.models import Order
from cart.forms import CartAddProductForm
from .forms import ProductForm, CategoryForm, VisitorForm


def home(request):
    if request.user.is_staff:
        return redirect('products:employee_home')
    elif request.user.username:
        return redirect('products:product_list')
    else:
        return redirect('users:home')


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    productFilter = ProductFilter(request.GET, queryset=products)
    products = productFilter.qs
    return render(request,
                  'onlinegrocery/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products,
                   'productFilter': productFilter})


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    user = request.user
    cart_product_form = CartAddProductForm()
    return render(request,
                  'onlinegrocery/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form,
                   'user': user})


@staff_member_required
def product_new(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.created = timezone.now()
            product.save()
            products = Product.objects.filter(created__lte=timezone.now())
            return redirect('products:product_list')
    else:
        form = ProductForm()
    return render(request, 'onlinegrocery/product_new.html', {'form': form})


@staff_member_required
def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            product = form.save()
            product.updated = timezone.now()
            product.save()
            products = Product.objects.filter(created__lte=timezone.now())
            return redirect('products:product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'onlinegrocery/product_edit.html', {'form': form})


@staff_member_required
def category_list_emp(request):
    categories = Category.objects.all()
    return render(request, 'onlinegrocery/categories_list.html',
                  {'categories': categories})


@staff_member_required
def category_new(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            return redirect('products:category_list_emp')
    else:
        form = CategoryForm()
    return render(request, 'onlinegrocery/category_new.html', {'form': form})


@staff_member_required
def category_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            category = form.save()
            category.save()
            return redirect('products:category_list_emp')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'onlinegrocery/category_edit.html', {'form': form,
                                                                'pk': pk})


@staff_member_required
def employee_home(request):
    categoryCount = str(Category.objects.all().count())
    productsCount = str(Product.objects.all().count())
    customerCount = str(Customer.objects.all().count())
    orderCount = str(Order.objects.all().count())
    context = {"categoryCount": categoryCount,
               "productsCount": productsCount,
               "customerCount": customerCount,
               "orderCount": orderCount}

    return render(request, 'onlinegrocery/employee_home.html', {'context': context})


def category_list(request):
    categories = Category.objects.all()
    context = {

        "categories": categories,
    }
    return context


@staff_member_required
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        category.delete()
        return redirect('products:category_list_emp')
    return render(request, 'onlinegrocery/category_delete.html', {'category': category})


@staff_member_required
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        product.delete()

        return redirect('products:category_list_emp')
    return render(request, 'onlinegrocery/product_delete.html', {'product': product})


def visitor_new(request):
    if request.method == "POST":
        form = VisitorForm(request.POST)
        if form.is_valid():
            visitors = form.save(commit=False)
            visitors.created_date = timezone.now()
            visitors.save()
            return render(request, 'onlinegrocery/feedback_done.html')

    else:
        form = VisitorForm()
        # print("Else")
    return render(request, 'onlinegrocery/contact_page.html', {'form': form})


