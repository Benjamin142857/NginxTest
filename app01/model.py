# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Course(models.Model):
    c_id = models.CharField(primary_key=True, max_length=20)
    c_name = models.CharField(max_length=20)
    t_id = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'course'


class Score(models.Model):
    s_id = models.CharField(primary_key=True, max_length=20)
    c_id = models.CharField(max_length=20)
    s_score = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'score'
        unique_together = (('s_id', 'c_id'),)


class Student(models.Model):
    s_id = models.CharField(primary_key=True, max_length=20)
    s_name = models.CharField(max_length=20)
    s_birth = models.CharField(max_length=20)
    s_sex = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'student'


class Teacher(models.Model):
    t_id = models.CharField(primary_key=True, max_length=20)
    t_name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'teacher'
