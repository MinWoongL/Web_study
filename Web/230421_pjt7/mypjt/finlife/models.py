from django.db import models

# Create your models here.

class DepositProducts(models.Model):
    # 금융상품코드
    fin_prdt_cd = models.TextField(unique=True)
    # 금융회사명
    kor_co_nm = models.TextField()
    # 금융 상품명
    fin_prdt_nm = models.TextField()
    # 금융상품설명
    etc_note = models.TextField()
    # 가입제한(1: 제한없음, 2:서민전용, 3:일부제한)
    join_deny = models.IntegerField()
    # 가입대상
    join_member = models.TextField()
    # 가입방법
    join_way = models.TextField()
    # 우대조건
    spcl_cnd = models.TextField()
    

class DepositOptions(models.Model):
    # 외래 키
    fin_prdt_cd = models.ForeignKey(DepositProducts, on_delete=models.CASCADE, related_name='options')
    # 저축금리 유형명
    intr_rate_type_nm = models.CharField(max_length=100)
    # 저축금리
    intr_rate = models.FloatField()
    # 최고우대금리
    intr_rate2 = models.FloatField()
    # 저축기간(단위: 개월)
    save_trm = models.IntegerField()
    