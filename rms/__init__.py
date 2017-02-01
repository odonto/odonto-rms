"""
rms - Our OPAL Application
"""
from opal.core import application


class Application(application.OpalApplication):
    flow_module   = 'rms.flow'
    javascripts   = [
        'js/rms/routes.js',
        'js/rms/controllers/allocated_clinic_location_helper.js',
        'js/opal/controllers/discharge.js',
        # Uncomment this if you want to implement custom dynamic flows.
        # 'js/rms/flow.js',
    ]
    styles = [
        "css/odonto.css"
    ]
    default_episode_category = 'Referral'
