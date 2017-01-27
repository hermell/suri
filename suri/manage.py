#!/usr/bin/env python
import os
import sys


# django 프로젝트에 대해 여러가지 작업을 수행하는 명령 라인 유틸리티
# 더 자세한 사항이 궁금하면 djnago-admin.py and manage.py 를 읽어본다.

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "suriProject.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
