from django.db import models
from django.contrib.auth.models  import User
# Create your models here.
class Aim (models.Model):
  user_id = models.IntegerField(db_column = 'user_id')
  time_begin = models.DateTimeField(auto_now_add=True, blank=True)
  time_end = models.DateTimeField(auto_now_add=True, blank=True)
  aim_bet = models.IntegerField(db_column='aim_bet')
  aim_name = models.CharField(max_length=450,db_column='aim_name')
  aim_description = models.CharField(max_length=450)
  type_id =  models.ForeignKey('AimType', db_column='type_id')
  status_id = models.ForeignKey('AimStatus', db_column = 'status_id')
  class Meta:
    managed = True

class AimType (models.Model):
  type_id = models.IntegerField(primary_key=True, db_column='type_id')
  type_name = models.CharField(max_length=45)
  class Meta:
    managed = True

class AimStatus (models.Model):
  status_id = models.IntegerField(primary_key=True, db_column='status_id')
  status_name = models.CharField(max_length=45)
  class Meta:
    managed = True