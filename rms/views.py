from django.views.generic import TemplateView
from opal.core.views import LoginRequiredMixin
from opal.core.subrecords import get_subrecord_from_api_name


class ImgTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'img_view.html'

    def get_context_data(self, **kwargs):
        model = get_subrecord_from_api_name(kwargs["model"])
        instance = model.objects.get(pk=kwargs["pk"])
        context = super(ImgTemplateView, self).get_context_data(**kwargs)
        context["title"] = instance.name
        return context
