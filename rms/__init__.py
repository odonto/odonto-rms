"""
rms - Our OPAL Application
"""
import copy
from opal.core import menus
from opal.core import application


class Application(application.OpalApplication):
    javascripts = [
        'js/rms/routes.js',
        'js/rms/controllers/directives.js',
        'js/rms/controllers/allocated_clinic_location_helper.js',
        'js/opal/controllers/discharge.js',
        # Uncomment this if you want to implement custom dynamic flows.
        # 'js/rms/flow.js',
    ]
    default_episode_category = 'Referral'

    menuitems = [
        # dict(href="/#/overview", display="Region Overview",
        #      icon="fa fa-dashboard", activepattern="overview"),
        menus.MenuItem(
            href="/#/myclinic",
            display="Morpeth Clinic",
            icon="fa fa-dashboard",
            activepattern="myclinic"),
    ]

    @classmethod
    def get_menu_items(cls, user=None):
        menu_items = []

        if user.is_superuser or user.has_perm('rms.can_refer'):
            menu_items.append(
                menus.MenuItem(
                    href="/pathway/#/referral_form/",
                    display="Make a referral",
                    icon="fa fa-plus",
                    activepattern="pathway/#/referral_form/"),
            )
            menu_items.append(
                menus.MenuItem(
                    href="/#/list/my_referrals",
                    display="My Referrals",
                    icon="fa fa-user",
                    activepattern="my_referrals",
                    template_name="menu_items/my_referrals.html"
                )
            )

        if user.is_superuser or user.has_perm('rms.can_assign_location'):
            menu_items.append(
                menus.MenuItem(
                    href="/#/list/new_referrals",
                    display="Triage Inbox",
                    icon="fa fa-inbox",
                    activepattern="new_referrals"
                )
            )

        if user.is_superuser or user.has_perm('rms.can_confirm_location'):
            menu_items.append(
                menus.MenuItem(
                    href="/#/list/approval_inbox",
                    display="Approval Inbox",
                    icon="fa fa-inbox",
                    activepattern="approval_inbox"
                ),
            )

        menu_items += copy.copy(cls.menuitems)
        return menu_items
