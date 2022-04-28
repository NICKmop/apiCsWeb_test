from django.db import models

# 모델 명 생성
class info(models.Model):
    site_name = models.CharField(max_length=100);

    # 해당 모델 데이터 정상 전달 되는지 확인 
    def __str__(self):
        return '사이트 이름 : ' + self.site_name;

class Testtable(models.Model):
    id = models.IntegerField(primary_key=True)
    test = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'testTable'

class Customer(models.Model):
    id = models.IntegerField(primary_key=True)
    customerid = models.CharField(db_column='CustomerID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    customername = models.CharField(db_column='CustomerName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    contactname = models.CharField(db_column='ContactName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=100, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=100, blank=True, null=True)  # Field name made lowercase.
    postalcode = models.IntegerField(db_column='PostalCode', blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Customer'