from django.shortcuts import render
from django.http import Http404, HttpResponse, response
from django.views import View

import logging

logger = logging.getLogger('request')


class Test(View):
    def get(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
            
        logger.debug('IP: ' + ip)
        logger.info('IP: ' + ip)
        logger.warning('IP: ' + ip)
        logger.error('IP: ' + ip)
        # print('Your log message... IP:' + ip)

        return HttpResponse(f"hello, You'r IP is {ip}")
