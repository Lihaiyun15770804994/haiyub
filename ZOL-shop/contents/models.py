from django.db import models

# Create your models here.
class Goods(models.Model):
    productid = models.IntegerField(verbose_name="商品id")
    productimg = models.CharField(max_length=100, verbose_name='商品图片')
    productname = models.CharField(max_length=100, verbose_name='商品短名称')
    # productlongname = models.CharField(max_length=255, verbose_name="商品长名称")
    # specifics = models.CharField(max_length=100, verbose_name="商品规格")
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="售价")
    marketprice = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="市场售价")
    # categoryid = models.IntegerField(verbose_name='所属分类id')
    # childcid = models.IntegerField(verbose_name="所属自分类id")
    # childcidname = models.CharField(max_length=100, verbose_name="自分类名称")
    storenums = models.IntegerField(verbose_name="库存")
    productnum = models.IntegerField(verbose_name="销量")

    class Meta:
        db_table = 'zol-goods'