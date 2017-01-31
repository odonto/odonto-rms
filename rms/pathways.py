"""
Pathways for the Odonto RMS
"""
import datetime


from pathway.pathways import PagePathway, Step
from rms import models
from opal import models as omodels


class ReferralPathway(PagePathway):
    display_name = "Referral"
    slug = "referral_form"
    step_wrapper_template_url = "/templates/pathways/step_wrappers/odonto_page_wrapper.html"
    template_url = "/templates/pathways/odonto_pathway_base.html"


    steps = (
        models.Demographics,
        models.ContactDetails,
        models.CarerDetails,
        models.ReferralReason,
        models.Disability,
        models.MedicalIssues,
        models.MentalHealthIssues,
    )

    def save(self, data, user):
        data[models.Demographics.get_api_name()][0]["hospital_number"] = omodels.Patient.objects.count()
        patient = super(ReferralPathway, self).save(data, user)
        episode = patient.episode_set.last()
        episode.active = True
        episode.save()
        referral = episode.referraldetails_set.first()
        referral.when = datetime.date.today()
        referral.who = user
        referral.save()
        return patient

    def redirect_url(self, patient):
        return '/#/list/new_referrals'


class CheckAndFind(PagePathway):
    display_name = "Check and find"
    slug = "check_and_find"
    steps = (models.AllocatedClinic,)


class ApproveDecision(PagePathway):
    _is_singleton = True
    display_name = "Approve"
    slug = "approve"
    steps = (models.AllocatedClinic,)
