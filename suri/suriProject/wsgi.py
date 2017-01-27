"""
WSGI config for suriProject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/

이 프로젝트가 WSGI 호환 웹서버로 동작하기 위한 진입점을 설정
WSGI에 대해서는 상단의 주소에서 확인
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "suriProject.settings")

application = get_wsgi_application()
