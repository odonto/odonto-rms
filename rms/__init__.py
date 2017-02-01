"""
rms - Our OPAL Application
"""
from opal.core import application

class Application(application.OpalApplication):
    flow_module   = 'rms.flow'
    javascripts   = [
        'js/rms/routes.js',
        'js/opal/controllers/discharge.js',
        # Uncomment this if you want to implement custom dynamic flows.
        # 'js/rms/flow.js',
    ]
    styles = [
        "css/odonto.css"
    ]
    default_episode_category = 'Referral'

    menuitems = [
        dict(href="/pathway/#/referral_form/", display="Make a referral", activepattern="pathway/#/referral_form/"),
        dict(href="/#/list/new_referrals", display="New Referrals", activepattern="new_referrals"),
        dict(href="/#/list/my_referrals", display="My Referrals", activepattern="my_referrals")
    ]
