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


class ClinicLocation(lookuplists.LookupList):
    pass


class AllocatedClinic(models.EpisodeSubrecord):
    location = ForeignKeyOrFreeText(ClinicLocation)
    confirmed = fields.BooleanField(default=False)
    letter_sent = fields.BooleanField(default=False)


class Disability(models.EpisodeSubrecord):
    _is_singleton = True
    has_disability = fields.BooleanField(default=False)
    able_to_communicate = fields.BooleanField(default=False)
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
