# import sys

# import dj_database_url
# import sentry_sdk
# from sentry_sdk.integrations.django import DjangoIntegration

from . import *  # noqa


# ALLOWED_HOSTS = ["app.qiiro.eu", "webapp-production-9j96q.ondigitalocean.app"]

# SMARTDOCS_API_BASE_PATH = "https://api.qiiro.eu"

# if (
#     len(sys.argv) > 0 and sys.argv[1] != "collectstatic"
# ):  # do not set cache and DB for static collection job
#     DATABASES = {
#         "default": dj_database_url.parse(env("DATABASE_URL")),
#     }

# if (
#     len(sys.argv) > 0 and sys.argv[1] != "migrate" and sys.argv[1] != "collectstatic"
# ):  # do not set cache for static collection and migration jobs
#     CACHES = {
#         "default": {
#             "BACKEND": "django_redis.cache.RedisCache",
#             "LOCATION": env("CACHE_URL"),
#             "OPTIONS": {
#                 "CLIENT_CLASS": "django_redis.client.DefaultClient",
#             },
#             "KEY_PREFIX": "production",
#         }
#     }


# # ERRORS LOGGING
# sentry_sdk.init(
#     dsn="https://73519869467d49c9b719cc3bca1309eb@o572238.ingest.sentry.io/5721358",
#     integrations=[DjangoIntegration()],
#     environment=DJANGO_ENV,
#     # Set traces_sample_rate to 1.0 to capture 100%
#     # of transactions for performance monitoring.
#     # We recommend adjusting this value in production.
#     traces_sample_rate=0.01,
#     # If you wish to associate users to errors (assuming you are using
#     # django.contrib.auth) you may enable sending PII data.
#     send_default_pii=True,
# )

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
#         "level": "INFO",
#     },
#     "loggers": {
#         "django": {
#             "handlers": ["console"],
#             "level": env("DJANGO_LOG_LEVEL", default="INFO"),
#             "propagate": False,
#         },
#     },
# }

# # Store files on Digital Ocean Spaces
# # AWS variable names are required by s3boto3. Digital Ocean is S3 compatible.
# DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
# AWS_S3_REGION_NAME = "fra1"
# AWS_S3_ENDPOINT_URL = f"https://{AWS_S3_REGION_NAME}.digitaloceanspaces.com"
# AWS_ACCESS_KEY_ID = "FDZ7H7J4YCSUM2FK4O4C"
# AWS_SECRET_ACCESS_KEY = env("DIGITAL_OCEAN_S3_SECRET_ACCESS_KEY")
# AWS_STORAGE_BUCKET_NAME = "qiiro-webapp"
