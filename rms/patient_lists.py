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


class AllReferrals(core.patient_lists.PatientList):
    display_name = "All Referrals"
    slug = "all_referrals"
    schema = [
        models.Demographics,
        models.Diagnosis,
        models.Treatment,
        Column(
            name="stage",
            title="Stage",
            template_path="columns/stage.html",
        )
    ]

    def get_queryset(self, **kw):
        return Episode.objects.all()


class NewReferralsList(core.patient_lists.PatientList):
    display_name = 'New Referrals'
    slug = "new_referrals"
    template_name = 'referral_table_list.html'

    schema = [
        Column(
            name="date",
            title="Date of Referral",
            template_path="columns/date_of_referral.html",
        ),
        Column(
            name="referrer",
            title="Referred from",
            template_path="columns/referrer.html",
        ),
        Column(
            name="name",
            title="Patient",
            template_path="columns/name.html",
        ),
        Column(
            name="urgency",
            title="Urgency",
            template_path="columns/urgency.html",
        )
    ]

    def get_queryset(self, **k):
        return Episode.objects.filter(
            allocatedclinic__location__isnull=True,
        )


class ApprovalList(core.patient_lists.PatientList):
    display_name = 'Approval List'

    schema = [
        models.Demographics,
        models.Diagnosis,
        models.AllocatedClinic,
        Column(
            name="check_and_find",
            title="",
            template_path="columns/check_and_find.html",
        )
    ]

    def get_queryset(self, **kw):
        return Episode.objects.filter(
            allocatedclinic__confirmed=False,
            allocatedclinic__letter_sent=False,
        )

    @transaction.atomic
    def save(self, data, user):
        models.ReferralDetails.objects.create(when=datetime.now(), who=user)
        return super(ApprovalList, self).save(data, user)


class MyReferrals(core.patient_lists.PatientList):
    display_name = "My Referrals"
    slug = 'my_referrals'
    template_name = 'referral_table_list.html'

    schema = [
        Column(
            name="date",
            title="Date of Referral",
            template_path="columns/date_of_referral.html",
        ),
        Column(
            name="name",
            title="Patient",
            template_path="columns/name.html",
        ),
        Column(
            name="urgency",
            title="Urgency",
            template_path="columns/urgency.html",
        ),
        Column(
            name="status",
            title="Status",
            template_path="columns/status.html",
        )

    ]

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
