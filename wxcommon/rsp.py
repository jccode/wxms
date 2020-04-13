# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse


def success(data):
    return JsonResponse({"is_success": True, "data": data})


def fail(errcode, errmsg):
    return JsonResponse({"is_success": False, "error": {"code": errcode, "msg": errcode}})
