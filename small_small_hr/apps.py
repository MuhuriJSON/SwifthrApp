from django.apps import AppConfig


class SmallSmallHrConfig(AppConfig):
    name = 'small_small_hr'
    app_label = 'small_small_hr'

    def ready(self):
        # pylint: disable=unused-import
        import small_small_hr.signals  # noqa

        # set up app settings
        from django.conf import settings
        import small_small_hr.settings as defaults
        for name in dir(defaults):
            if name.isupper() and not hasattr(settings, name):
                setattr(settings, name, getattr(defaults, name))



class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        import users.signals
