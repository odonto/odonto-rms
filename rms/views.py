from django.views.generic import TemplateView
from opal.core.views import LoginRequiredMixin


class ImgTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'img_view.html'

    def get_context_data(self, **kwargs):
        context = super(ImgTemplateView, self).get_context_data(**kwargs)
        context["title"] = "X-ray"
        return context
