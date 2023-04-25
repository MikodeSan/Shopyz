from . import *  # noqa

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# CACHES = {
#     "default": {
#         "BACKEND": "django.core.cache.backends.dummy.DummyCache",
#     }
# }

# INSTALLED_APPS += ["django_extensions", "debug_toolbar", "pympler"]  # noqa F405
INSTALLED_APPS += ["django_extensions"]  # noqa F405

MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    # "whitenoise.middleware.WhiteNoiseMiddleware",
]  # noqa F405

# LOGGING = {
#     "version": 1,
#     "disable_existing_loggers": False,
#     "formatters": {
#         "standard": {"format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s"},
#     },
#     "handlers": {
#         "console": {
#             "class": "logging.StreamHandler",
#         },
#     },
#     "root": {
#         "handlers": ["console"],
#         "level": "DEBUG",
#     },
#     "loggers": {
#         "django": {
#             "handlers": ["console"],
#             "level": env("DJANGO_LOG_LEVEL", default="INFO"),
#             "propagate": False,
#         },
#         "asyncio": {
#             "level": "WARNING",
#         },
#     },
# }


# # dirty way of making work debug toolbar config
# def show_toolbar(request):
#     return True


# DEBUG_TOOLBAR_CONFIG = {
#     "DISABLE_PANELS": ["debug_toolbar.panels.redirects.RedirectsPanel"],
#     "SHOW_TEMPLATE_CONTEXT": True,
#     # "SHOW_TOOLBAR_CALLBACK": show_toolbar,  # comment this line to disable debug toolbar
# }

# # Panels present in django debug toolbar
# DEBUG_TOOLBAR_PANELS = (
#     "debug_toolbar.panels.history.HistoryPanel",
#     "debug_toolbar.panels.versions.VersionsPanel",
#     "debug_toolbar.panels.timer.TimerPanel",
#     "debug_toolbar.panels.settings.SettingsPanel",
#     "debug_toolbar.panels.headers.HeadersPanel",
#     "debug_toolbar.panels.request.RequestPanel",
#     "debug_toolbar.panels.sql.SQLPanel",
#     "debug_toolbar.panels.staticfiles.StaticFilesPanel",
#     "debug_toolbar.panels.templates.TemplatesPanel",
#     "debug_toolbar.panels.cache.CachePanel",
#     "debug_toolbar.panels.signals.SignalsPanel",
#     "debug_toolbar.panels.logging.LoggingPanel",
#     "debug_toolbar.panels.redirects.RedirectsPanel",
#     "debug_toolbar.panels.profiling.ProfilingPanel",
#     "pympler.panels.MemoryPanel",
# )

# MEDIA_URL = "/media/"
# MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
# INTERNAL_IPS = [ip[:-1] + "1" for ip in ips]
