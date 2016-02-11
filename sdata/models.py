from django.conf import settings
from django.db import models


class Stock2(models.Model):
    s_name = models.CharField(max_length=20)
    s_code = models.CharField(max_length=10, primary_key=True)
    # s_open = models.CharField(max_length=20, null=True)
    # s_close = models.CharField(max_length=20, null=True)
    # s_date = models.CharField(max_length=20, null=True)
    # created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.s_name

class Stock_current(models.Model):
    hname = models.CharField(max_length=20)
    price = models.CharField(max_length=8)
    sign = models.CharField(max_length=1)
    change = models.CharField(max_length=8)
    diff = models.CharField(max_length=7)
    volume = models.CharField(max_length=12)
    recprice = models.CharField(max_length=8)
    avgp = models.CharField(max_length=8)
    uplmtprice = models.CharField(max_length=8)
    dnlmtprice = models.CharField(max_length=8)
    jnilvolume = models.CharField(max_length=12)
    volumediff = models.CharField(max_length=12)
    openp = models.CharField(max_length=8)
    opentime = models.CharField(max_length=6)
    high = models.CharField(max_length=8)
    hightime = models.CharField(max_length=6)
    low = models.CharField(max_length=8)
    lowtime = models.CharField(max_length=6)
    high52w = models.CharField(max_length=8)
    high52wdate = models.CharField(max_length=8)
    low52w = models.CharField(max_length=8)
    low52wdate = models.CharField(max_length=8)
    exhratio = models.CharField(max_length=7)
    flmtvol = models.CharField(max_length=12)
    per = models.CharField(max_length=7)
    listing = models.CharField(max_length=12)
    jkrate = models.CharField(max_length=8)
    vol = models.CharField(max_length=7)
    shcode = models.CharField(max_length=8, primary_key=True)
    valuep = models.CharField(max_length=12)
    highyear = models.CharField(max_length=8)
    highyeardate = models.CharField(max_length=8)
    lowyear = models.CharField(max_length=8)
    lowyeardate = models.CharField(max_length=8)
    upname = models.CharField(max_length=20)
    upcode = models.CharField(max_length=3)
    upprice = models.CharField(max_length=8)
    upsign = models.CharField(max_length=1)
    upchange = models.CharField(max_length=7)
    updiff = models.CharField(max_length=7)

    def __str__(self):
        return self.hname
