"""
Episode cagtegory for Odonto RMS
"""
from opal.core.episodes import EpisodeCategory

class ReferralEpisode(EpisodeCategory):
    slug = 'referral'
    display_name = "Referral"
    detail_template = 'detail/referral.html'
