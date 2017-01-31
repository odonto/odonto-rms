"""
Pathways for the Odonto RMS
"""
import datetime


from pathway.pathways import PagePathway, Step
from rms import models


class ReferralPathway(PagePathway):
    display_name = "Referral"
    slug = "referral_form"
    step_wrapper_template_url = "/templates/pathways/step_wrappers/odonto_page_wrapper.html"
    template_url = "/templates/pathways/odonto_pathway_base.html"


    steps = (
        Step(
            model=models.Demographics, display_name="What are the personal details of the patient?", icon=None
        ),
        models.Disability,
        models.MedicalIssues,
        models.MentalHealthIssues,
    )

    def save(self, data, user):
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
        return '/#/list/check_and_find'


class CheckAndFind(PagePathway):
    display_name = "Check and find"
    slug = "check_and_find"
    steps = (models.AllocatedClinic,)


class ApproveDecision(PagePathway):
    _is_singleton = True
    display_name = "Approve"
    slug = "approve"
    steps = (models.AllocatedClinic,)
