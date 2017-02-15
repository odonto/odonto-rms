"""
Defining OPAL PatientLists
"""
import datetime
from functools import partial
from django.db import transaction
from opal import core
from opal.models import Episode
from rms import models


Column = partial(
    core.patient_lists.Column,
    limit=None,
    singleton=True,
    detail_template_path=None
)
Stage = Column(
    name="stage",
    title="Stage",
    template_path="columns/stage.html",
)
Date = Column(
    name="date",
    title="Date of Referral",
    template_path="columns/date_of_referral.html",
)
Referrer = Column(
    name="referrer",
    title="Referred from",
    template_path="columns/referrer.html",
)
Patient = Column(
    name="name",
    title="Patient",
    template_path="columns/name.html",
)
Urgency = Column(
    name="urgency",
    title="Urgency",
    template_path="columns/urgency.html",
)
Status = Column(
    name="status",
    title="Status",
    template_path="columns/status.html"
)


class NewReferralsList(core.patient_lists.PatientList):
    display_name = 'Triage Inbox'
    slug = "new_referrals"
    template_name = 'referral_table_list.html'

    schema = [Date, Referrer, Patient, Urgency]

    def get_queryset(self, **k):
        return Episode.objects.filter(
            allocatedclinic__location__isnull=True,
        )


class ApprovalList(core.patient_lists.PatientList):
    display_name = 'Approval Inbox'
    slug = 'approval_inbox'
    template_name = 'referral_table_list.html'

    schema = [Date, Referrer, Patient, Urgency]

    def get_queryset(self, **kw):
        return Episode.objects.filter(
            allocatedclinic__confirmed=False,
            allocatedclinic__letter_sent=False,
        ).order_by("referralreason__urgency")

    @transaction.atomic
    def save(self, data, user):
        models.ReferralDetails.objects.create(when=datetime.now(), who=user)
        return super(ApprovalList, self).save(data, user)


class MyReferrals(core.patient_lists.PatientList):
    display_name = "My Referrals"
    slug = 'my_referrals'
    template_name = 'referral_table_list.html'

    schema = [Date, Patient, Urgency, Status]

    def get_queryset(self, user=None):
        return Episode.objects.filter(
            referraldetails__who=user
        )


class BeckyClinic(core.patient_lists.PatientList):
    display_name = "Becky's Clinic"
    slug = "beckys_clinic"

    schema = [
        models.Demographics,
        models.Diagnosis,
        models.Treatment,
        models.ReferralDetails
    ]

    def get_queryset(self, user=None):
        return Episode.objects.filter(
            allocatedclinic__confirmed=True,
        )
