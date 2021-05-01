from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView, UpdateView

from webapp.forms import FeedbackForm
from webapp.models import Feedback, Product


class ProductFeedbackCreate(CreateView):
    template_name = 'feedbacks/create.html'
    form_class = FeedbackForm
    model = Feedback

    def get_success_url(self):
        return reverse(
            'webapp:view',
            kwargs={'pk': self.kwargs.get('pk')}
        )

    def form_valid(self, form):
        product = get_object_or_404(Product, id=self.kwargs.get('pk'))
        feedback = form.instance
        feedback.product = product
        feedback.author = self.request.user
        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    form_class = FeedbackForm
    model = Product
    template_name = 'feedbacks/update.html'
    context_object_name = 'feedback'

    def get_success_url(self):
        return reverse('webapp:view', kwargs={'pk': self.kwargs.get('pk')})

    def form_valid(self, form):
        feedback = form.instance
        feedback.moderated = False
        return super().form_valid(form)
