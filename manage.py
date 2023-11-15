import os
import sys
import sentry_sdk
import logging

def main():
     
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oc_lettings_site.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
    sentry_sdk.init(...)  # same as above

    logging.debug("I am ignored")
    logging.info("I am a breadcrumb")
    logging.error("I am an event", extra=dict(bar=43))
    logging.exception("An exception happened")


if __name__ == '__main__':
    main()




