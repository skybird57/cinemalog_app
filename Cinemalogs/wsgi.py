"""
WSGI config for Cinemalogs project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Cinemalogs.settings')

application = get_wsgi_application()

#import time
#from threading import Thread
#from cinemalog.Modules import news_crawler
#th=Thread(target=news_crawler.test)
#th.start()