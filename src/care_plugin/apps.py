from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

PLUGIN_NAME = "care_plugin"


class CarePluginConfig(AppConfig):
    name = PLUGIN_NAME
    verbose_name = _("Care plugin")

    def ready(self):
        import care_plugin.signals  # noqa F401
