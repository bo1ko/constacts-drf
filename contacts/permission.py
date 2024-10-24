import os

import requests
from dotenv import load_dotenv
from rest_framework import permissions

load_dotenv()

COUNTRY_LIST = os.getenv('COUNTRY_LIST').strip().split(',')
GEO_URL = os.getenv('GEO_URL')
GEO_TOKEN = os.getenv('GEO_TOKEN')


class GeoPermission(permissions.BasePermission):
    """Allows access only from specific countries."""

    def has_permission(self, request, view):
        remote_addr = request.META['REMOTE_ADDR']
        res = requests.get(f"{GEO_URL}/{remote_addr}?token={GEO_TOKEN}")
        res_json = res.json()
        res_country = res_json.get('country')

        if res_country in COUNTRY_LIST:
            return True

        return False