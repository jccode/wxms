# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import urllib
import logging

from django.conf import settings
from django.core.cache import cache

# Create your views here.

logger = logging.getLogger(__name__)

ACCESS_TOKEN_KEY = 'access_token'
JSAPI_TICKET_KEY = 'jsapi_ticket'


def get_real_access_token(app_id, app_secret):
    post_url = ("https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s" % (app_id, app_secret))
    url_resp = urllib.urlopen(post_url)
    url_resp = json.loads(url_resp.read())
    logger.info('fetch access token|%s', url_resp)
    return url_resp['access_token'], url_resp['expires_in']


def access_token():
    token = cache.get(ACCESS_TOKEN_KEY)
    if token is None:
        ret = get_real_access_token(settings.WX_APP_ID, settings.WX_APP_SECRET)
        token = ret[0]
        expire = ret[1]
        cache.set(ACCESS_TOKEN_KEY, token, expire)
    return token


def get_real_jsapi_ticket(access_token):
    url = "https://api.weixin.qq.com/cgi-bin/ticket/getticket?access_token=%s&type=jsapi" % access_token
    url_resp = urllib.urlopen(url)
    url_resp = json.loads(url_resp.read())
    logger.info('fetch jsapi ticket|%s', url_resp)
    return url_resp['ticket'], url_resp['expires_in']


def jsapi_ticket():
    ticket = cache.get(JSAPI_TICKET_KEY)
    if ticket is None:
        ret = get_real_jsapi_ticket(access_token())
        ticket = ret[0]
        expire = ret[1]
        cache.set(JSAPI_TICKET_KEY, ticket, expire)
    return ticket

