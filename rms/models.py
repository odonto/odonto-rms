"""
rms models.
"""
from django.db import models as fields
from django.contrib.auth.models import User

from opal import models
from opal.core.fields import ForeignKeyOrFreeText
from opal.core import lookuplists

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
    relationship_to_patient = ForeignKeyOrFreeText(RelationshipToPatient)
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


class ReferralReason(models.EpisodeSubrecord):
    _title = "Referral Reason"

    dental_treatment_needed = fields.TextField()
    dental_treatment_already_provided = fields.TextField()
    difficulties_encountered = fields.TextField()


class ClinicLocation(lookuplists.LookupList):
    pass


class AllocatedClinic(models.EpisodeSubrecord):
    location = ForeignKeyOrFreeText(ClinicLocation)
    confirmed = fields.BooleanField(default=False)
    letter_sent = fields.BooleanField(default=False)


class Disability(models.EpisodeSubrecord):
    _is_singleton = True
    UNIMPAIRED = "Unimpaired"
    PARTIALLY_IMPARED = "partially impaired"
    SEVERLY_IMPARED = "severly impaired"
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
        default=UNIMPAIRED
    )
    able_to_leave_home = fields.BooleanField(default=False)
    able_to_stand_for_transfer = fields.BooleanField(default=False)
    has_capacity_to_consent = fields.BooleanField(default=False)


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

    when = fields.DateTimeField(blank=True, null=True)
    who = fields.ForeignKey(User, blank=True, null=True)
