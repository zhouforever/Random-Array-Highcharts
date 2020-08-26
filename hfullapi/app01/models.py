from django.db import models


class TableOne(models.Model):
    val1 = models.IntegerField(null=True, blank=True)
    val2 = models.IntegerField(null=True, blank=True)
    val3 = models.IntegerField(null=True, blank=True)
    val4 = models.IntegerField(null=True, blank=True)
    val5 = models.IntegerField(null=True, blank=True)
    val6 = models.IntegerField(null=True, blank=True)


class TableTwo(models.Model):
    val1 = models.IntegerField(null=True, blank=True)
    val2 = models.IntegerField(null=True, blank=True)
    val3 = models.IntegerField(null=True, blank=True)
    val4 = models.IntegerField(null=True, blank=True)
    val5 = models.IntegerField(null=True, blank=True)
    val6 = models.IntegerField(null=True, blank=True)

    # def __repr__(self):
    #     return [self.val1, self.val2, self.val3, self.val4, self.val5, self.val6]