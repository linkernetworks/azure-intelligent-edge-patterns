# -*- coding: utf-8 -*-
"""App Exceptions.
"""

from rest_framework.exceptions import APIException

class IsTrainingError(APIException):
    status_code = 400
    default_detail = 'Has unfinished iteration.'
    default_code = 'bad_request'

class TooManyIterationError(APIException):
    status_code = 400
    default_detail = 'Too many iterations. Pop some.'
    default_code = 'bad_request'
