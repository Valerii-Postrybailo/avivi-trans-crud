import os

from django.core.paginator import Paginator
from django.http import JsonResponse
from django.views import View
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404

from .models import Product
from .forms import StoreProductForm


class StoreItemsView(View):
    template_products_list = 'store.html'
    products_per_page = 5

    def get(self, request):
        products_list = Product.objects.all().order_by('created_at')
        paginator = Paginator(products_list, self.products_per_page)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, self.template_products_list, {'store_product_list': page_obj})


class ProductCreateView(View):
    def get(self, request):
        return render(request, 'create_store_item.html', {})

    def post(self, request):
        form = StoreProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('products_list_page'))

        return render(request, 'create_store_item.html', {'form': form})


class ProductDeleteView(View):
    def delete(self, request, *args, **kwargs):
        product_id = kwargs.get('pk')
        product = get_object_or_404(Product, id=product_id)
        if product.image:
            if os.path.isfile(product.image.path):
                os.remove(product.image.path)
        product.delete()

        return JsonResponse({}, status=204)


class ProductUpdateView(View):
    template_product_update = 'update_store_item.html'

    def get(self, request, *args, **kwargs):
        product_id = kwargs.get('pk')
        product = get_object_or_404(Product, id=product_id)
        form = StoreProductForm(instance=product)
        return render(request, self.template_product_update, {'form': form, 'product': product})

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)

        if product.image:
            if os.path.isfile(product.image.path):
                os.remove(product.image.path)

        form = StoreProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('products_list_page'))

        return render(request, self.template_product_update, {'form': form})
