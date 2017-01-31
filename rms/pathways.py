from pathway.pathways import PagePathway
from rms import models


class ReferralPathway(PagePathway):
    display_name = "Referral"
    slug = "referral_form"
    steps = (
        models.Demographics,
        models.Disability,
        models.MedicalIssues,
        models.MentalHealthIssues,
    )


class CheckAndFind(PagePathway):
    display_name = "Check and find"
    slug = "check_and_find"
    steps = (models.AllocatedClinic,)


class ApproveDecision(PagePathway):
    _is_singleton = True
    display_name = "Approve"
    slug = "approve"
    steps = (models.AllocatedClinic,)
