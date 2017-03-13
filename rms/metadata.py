from opal.core.metadata import Metadata
from rms.models import ClinicLocation


class AllocatedClinicMetadata(Metadata):
    slug = 'allocated_clinics'

    @classmethod
    def to_dict(klass, **kw):
        return {
            ClinicLocation.get_api_name(): list(ClinicLocation.objects.values())
        }
