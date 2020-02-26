from django.db import models

class Patient(models.Model):
    #확진자 수
    patient_index = models.IntegerField()
    #확진자 현재 상태
    status = models.CharField(max_length=50)

    #확진자 위치

    #위도
    latitude = models.FloatField()
    #경도
    longitude = models.FloatField()

    
