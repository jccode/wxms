# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging

from wxcommon import services, rsp

# Create your views here.

logger = logging.getLogger(__name__)


def access_token(request):
    return rsp.success(services.access_token())


def jsapi_ticket(request):
    return rsp.success(services.jsapi_ticket())

