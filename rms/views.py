from django.views.generic import TemplateView, RedirectView
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
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


class ChangeUser(RedirectView):
    def dispatch(self, *args, **kwargs):
        self.user = User.objects.get(username=kwargs.pop("user"))
        logout(self.request)
        authenticated = authenticate(
            username=self.user.username,
            password="{}1".format(self.user.username)
        )
        login(self.request, authenticated)
        return super(ChangeUser, self).dispatch(*args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        if self.user.username == "linda":
            return "/#/list/my_referrals"
        if self.user.username == "mary":
            return "/#/list/new_referrals"
        elif self.user.username == "matt":
            return "/#/list/approval_inbox"
        return self.request.get_full_path()
