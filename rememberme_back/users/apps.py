import contextlib

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "rememberme_back.users"
    verbose_name = _("Users")

    def ready(self):
        with contextlib.suppress(ImportError):
            import rememberme_back.users.signals  # noqa: F401
