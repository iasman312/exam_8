from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView

from webapp.forms import FeedbackForm
from webapp.models import Feedback, Product


class ProductFeedbackCreate(CreateView):
    template_name = 'feedbacks/create.html'
    form_class = FeedbackForm
    model = Feedback

    def get_success_url(self):
        return reverse(
            'article:view',
            kwargs={'pk': self.kwargs.get('pk')}
        )

    def form_valid(self, form):
        article = get_object_or_404(Product, id=self.kwargs.get('pk'))

        feedback = form.instance
        feedback.article = article
        feedback.author = self.request.user

        return super().form_valid(form)