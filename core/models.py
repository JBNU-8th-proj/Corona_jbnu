from django.db import models

class Patient(models.Model):
    #확진자 수
    patient_index = models.IntegerField(default=0)
    #확진자 현재 상태
    status = models.CharField(max_length=50)

    #확진자 위치

    #위도
    latitude = models.FloatField(default=0)
    #경도
    longitude = models.FloatField(default=0)

    def __str__(self):
        return str(self.patient_index)
