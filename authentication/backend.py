# -*- encoding: utf-8 -*-

from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import authenticate

class AuthBakend(BaseBackend):

	def authenticate(self, username=None, password=None):
    	user = authenticate(username=username, password=password)
        return user