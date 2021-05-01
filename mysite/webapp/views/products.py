from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy, reverse
from django.utils.http import urlencode
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import SearchForm, ProductForm
from webapp.models import Product
from django.db.models import Q


class IndexView(ListView):
    template_name = 'products/index.html'
    model = Product
    context_object_name = 'products'
    paginate_by = 5
    paginate_orphans = 1

    def get(self, request, **kwargs):
        self.form = SearchForm(request.GET)
        self.search_data = self.get_search_data()
        return super(IndexView, self).get(request, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()

        if self.search_data:
            queryset = queryset.filter(
                Q(name__icontains=self.search_data) |
                Q(category__icontains=self.search_data)
            )
        return queryset

    def get_search_data(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search_value']
        return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = self.form

        if self.search_data:
            context['query'] = urlencode({'search_value': self.search_data})
        return context


class ProductView(DetailView):
    model = Product
    template_name = 'products/view.html'

    def get_context_data(self, **kwargs):
        product = self.get_object()
        total = 0
        count = 0
        user = get_user_model()
        if product.feedbacks:
            for feedback in product.feedbacks.all():
                if feedback.moderated == True:
                    total += feedback.rating
                    count += 1
            if count == 0:
                average = 0
            else:
                average = total / count
        else:
            average = 0
        kwargs['average'] = average
        return super().get_context_data(**kwargs)


class CreateProductView(PermissionRequiredMixin, CreateView):
    template_name = 'products/create.html'
    form_class = ProductForm
    model = Product
    success_url = reverse_lazy('webapp:list')
    permission_required = 'webapp.add_product'


class ProductUpdateView(PermissionRequiredMixin, UpdateView):
    form_class = ProductForm
    model = Product
    template_name = 'products/update.html'
    context_object_name = 'product'
    permission_required = 'webapp.change_product'

    def get_success_url(self):
        return reverse('webapp:view', kwargs={'pk': self.kwargs.get('pk')})


class ProductDeleteView(PermissionRequiredMixin, DeleteView):
    model = Product
    template_name = 'products/delete.html'
    context_object_name = 'product'
    success_url = reverse_lazy('webapp:list')
    permission_required = 'webapp.delete_product'