"""
Pathways for the Odonto RMS
"""
import datetime

from opal.core.pathway import PagePathway, Step
from rms import models
from opal import models as omodels


class ReferralPathway(PagePathway):
    display_name = "Referral"
    slug = "referral_form"
    template = "pathways/odonto_pathway_base.html"

    steps = (
        Step(
            display_name = 'Patient Details',
            template = "pathways/steps/patient_detail.html",
            base_template = "pathways/step_wrappers/odonto_page_wrapper.html"
        ),
        Step(
            model = models.CarerDetails,
            base_template = "pathways/step_wrappers/odonto_page_wrapper.html"),
        Step(
            model = models.GPDetails,
            base_template = "pathways/step_wrappers/odonto_page_wrapper.html"),
        Step(
            model = models.ReferralReason,
            base_template = "pathways/step_wrappers/odonto_page_wrapper.html"),
        Step(
            model = models.Xray,
            base_template = "pathways/step_wrappers/odonto_page_wrapper.html"),
        Step(
            model = models.Disability,
            base_template = "pathways/step_wrappers/odonto_page_wrapper.html"),
        Step(
            model = models.MedicalIssues,
            base_template = "pathways/step_wrappers/odonto_page_wrapper.html"),
        Step(
            model = models.MentalHealthIssues,
            base_template = "pathways/step_wrappers/odonto_page_wrapper.html"),
    )

    def save(self, data, user, *args, **kwargs):
        data[models.Demographics.get_api_name()][0]["hospital_number"] = omodels.Patient.objects.count()
        patient, episode = super(ReferralPathway, self).save(data, user, *args, **kwargs)
        episode.active = True
        episode.save()
        referral = episode.referraldetails_set.first()
        referral.when = datetime.date.today()
        referral.who = user
        referral.save()
        return patient, episode


class CheckAndFind(PagePathway):
    display_name = "Check and find"
    slug = "check_and_find"
    steps = (models.AllocatedClinic,)


class ApproveDecision(PagePathway):
    _is_singleton = True
    display_name = "Approve"
    slug = "approve"
    steps = (models.AllocatedClinic,)
