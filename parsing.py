import os

import urllib.request
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', "corona.settings")
import django

django.setup()
from core.models import Patient


def parse_data():
    result = []

    corona_address = "https://api.coronas.info/patients/"

    req = urllib.request.urlopen(corona_address)
    res = req.readline()

    j = json.loads(res)

    for i in j:
        #확진된 환자만 보여줌
        try:
            Patient(patient_index=i['index'], status=i['status'], latitude=i['last_movement']['lat'], longitude = i['last_movement']['lng']).save()
        except:
            pass


if __name__ == '__main__':
    parse_data()

