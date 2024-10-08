from django.conf import settings
from django.utils.translation import gettext_lazy

from . import __version__

try:
    from pretix.base.plugins import PluginConfig
except ImportError:
    raise RuntimeError("Please use pretix 2.7 or above to run this plugin!")


class PluginApp(PluginConfig):
    default = True
    name = "pretix_seekink"
    verbose_name = "SeekInk eInk Badges"

    class PretixPluginMeta:
        name = gettext_lazy("SeekInk eInk Badges")
        author = "Martin Gross"
        description = gettext_lazy("Use SeekInk eInk Badges for your events")
        visible = True
        version = __version__
        category = "INTEGRATION"
        compatibility = "pretix>=2.7.0"
        picture = "pretix_seekink/logo.png"
        experimental = True

        @property
        def restricted(self):
            if any(
                domain in settings.SITE_URL for domain in ["pretix.eu", "pretix.dev"]
            ):
                return True
            return False

    def ready(self):
        from . import signals  # NOQA
