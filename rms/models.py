"""
rms models.
"""
from django.db import models as fields
from django.contrib.auth.models import User

from opal import models
from opal.core.fields import ForeignKeyOrFreeText
from opal.core import lookuplists
from opal.utils import camelcase_to_underscore

class Demographics(models.Demographics): pass
class Location(models.Location): pass
class Allergies(models.Allergies): pass
class Diagnosis(models.Diagnosis): pass
class PastMedicalHistory(models.PastMedicalHistory): pass
class Treatment(models.Treatment): pass
class Investigation(models.Investigation): pass
class SymptomComplex(models.Investigation): pass
class PatientConsultation(models.Investigation): pass


class ContactDetails(models.PatientSubrecord):
    _is_singleton = True
    _advanced_searchable = False
    _icon = 'fa fa-phone'
    address = fields.TextField(blank=True, null=True)
    address_line1 = fields.CharField(
        "Address line 1", max_length=45, blank=True, null=True
    )
    address_line2 = fields.CharField(
        "Address line 2", max_length=45, blank=True, null=True
    )
    city = fields.CharField(max_length=50, blank=True)
    county = fields.CharField(
        "County", max_length=40, blank=True, null=True
    )
    post_code = fields.CharField(
        "Post Code", max_length=10, blank=True, null=True
    )
    tel1 = fields.CharField(
        verbose_name="Telephone No.", blank=True, null=True, max_length=50
    )
    tel2 = fields.CharField(blank=True, null=True, max_length=50)

    class Meta:
        verbose_name_plural = "Contact details"


class RelationshipToPatient(lookuplists.LookupList):
    pass


class CarerDetails(models.PatientSubrecord):
    _title = "Carer Details"

    relationship_to_patient = ForeignKeyOrFreeText(RelationshipToPatient)
    address = fields.TextField(blank=True, null=True)
    surname = fields.CharField(max_length=255, blank=True)
    first_name = fields.CharField(max_length=255, blank=True)
    address_line1 = fields.CharField(
        "Address line 1", max_length=45, blank=True, null=True
    )
    address_line2 = fields.CharField(
        "Address line 2", max_length=45, blank=True, null=True
    )
    post_code = fields.CharField(
        "Post Code", max_length=10, blank=True, null=True
    )
    tel = fields.CharField(blank=True, null=True, max_length=50)


class GPDetails(models.PatientSubrecord):
    _title = "GMP"
    _is_singleton = True

    name = fields.CharField(max_length=255, blank=True, null=True)
    address = fields.TextField(blank=True, null=True)
    tel = fields.CharField(blank=True, null=True, max_length=50)


class ReferralReason(models.EpisodeSubrecord):
    _title = "Referral Reason"
    _is_singleton = True

    URGENT = "Urgent"
    ROUTINE = "Routine"
    URGENCY_CHOICES = (
        (ROUTINE, ROUTINE),
        (URGENT, URGENT),
    )

    urgency = fields.CharField(
        max_length=256,
        choices=URGENCY_CHOICES,
        null=True,
        blank=True,
        default=ROUTINE
    )
    dental_treatment_needed = fields.TextField()
    dental_treatment_already_provided = fields.TextField()
    difficulties_encountered = fields.TextField()


class ClinicLocation(models.ToDictMixin, fields.Model):
    TIER_CHOICES = (("2", "2",), ("3", "3"),)
    # either 1 or 2
    tier = fields.CharField(
        max_length="1", blank=True, null=True
    )
    address_line1 = fields.CharField(
        "Address line 1", max_length=45, blank=True, null=True
    )
    address_line2 = fields.CharField(
        "Address line 2", max_length=45, blank=True, null=True
    )
    post_code = fields.CharField(
        "Post Code", max_length=10, blank=True, null=True
    )
    tel = fields.CharField(max_length=50, blank=True, null=True)
    name = fields.CharField(max_length=255, blank=True, null=True)

    def __unicode__(self):
        return "{0} {1}".format(self.name, self.tier)

    @classmethod
    def get_display_name(cls):
        return cls._meta.object_name

    @classmethod
    def get_api_name(cls):
        return camelcase_to_underscore(cls._meta.object_name)


class AllocatedClinic(models.EpisodeSubrecord):
    _is_singleton = True
    location = fields.ForeignKey(ClinicLocation, blank=True, null=True)
    confirmed = fields.BooleanField(default=False)
    letter_sent = fields.BooleanField(default=False)


class Disability(models.EpisodeSubrecord):
    _is_singleton = True
    UNIMPAIRED = "Unimpaired"
    PARTIALLY_IMPARED = "Partially impaired"
    SEVERLY_IMPARED = "Severly impaired"
    COMMUNICATE_CHOICES = (
        (UNIMPAIRED, UNIMPAIRED),
        (PARTIALLY_IMPARED, PARTIALLY_IMPARED),
        (SEVERLY_IMPARED, SEVERLY_IMPARED),
    )

    has_disability = fields.BooleanField(default=False)
    able_to_communicate = fields.CharField(
        max_length=256,
        choices=COMMUNICATE_CHOICES,
        null=True,
        blank=True,
        default=UNIMPAIRED,
        verbose_name="Unable to communicate"
    )
    able_to_leave_home = fields.BooleanField(
        default=False,
        verbose_name="Unable to leave home")
    able_to_stand_for_transfer = fields.BooleanField(
        default=False,
        verbose_name="Unable to stand for transfer")
    has_capacity_to_consent = fields.BooleanField(
        default=False, verbose_name="Doubts over capacity to consent")


class MedicalIssues(models.EpisodeSubrecord):
    _is_singleton = True
    _title = "Medical Issues"
    has_medical_issues = fields.BooleanField(default=False)
    main_medical_conditions = fields.TextField(blank=True)
    medications_taken = fields.TextField(blank=True)


class MentalHealthIssues(models.EpisodeSubrecord):
    _is_singleton = True
    _title = "Mental Health Issues"

    has_mental_health_issues = fields.BooleanField(default=False)
    diagnosis = fields.TextField(blank=True)
    extreme_dental_phobia = fields.BooleanField(default=False)
    details_of_dental_phobia = fields.TextField(blank=True)


class ReferralDetails(models.EpisodeSubrecord):
    _is_singleton = True
    _title = "Referral Details"
    _editable =False

    when = fields.DateTimeField(blank=True, null=True)
    who = fields.ForeignKey(User, blank=True, null=True)

    def to_dict(self, user):
        d = super(ReferralDetails, self).to_dict(user)

        d['username'] = self.who.username
        d['email'] = self.who.email
        d['name'] = "{0} {1}".format(self.who.first_name, self.who.last_name)
        return d


class Xray(models.EpisodeSubrecord):
    _title ="Radiography"

    name = fields.CharField(max_length=256, blank=True, null=True)
    img = fields.FileField(blank=True, null=True)
    notes = fields.TextField(null=True, blank=True)

    @classmethod
    def _get_fieldnames_to_serialize(cls):
        fields = set(super(Xray, cls)._get_fieldnames_to_serialize())
        fields.remove("img")
        return fields
