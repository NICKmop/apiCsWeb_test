from pyexpat import model
from django.db import models

# 모델 명 생성
class info(models.Model):
    site_name = models.CharField(max_length=100);

    # 해당 모델 데이터 정상 전달 되는지 확인 
    def __str__(self):
        return '사이트 이름 : ' + self.site_name;