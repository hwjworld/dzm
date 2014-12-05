from django.db import models

# P = preach
class P_Volunteer(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class P_Map(models.Model):
    level1 = models.CharField(max_length=2)
    level2 = models.CharField(max_length=2)
    # 起始点,当地图切换的时候显示到这个点位置
    mapx = models.CharField(max_length=20)
    mapy = models.CharField(max_length=20)
    # 折线区域
    mappolyline = models.CharField(max_length=500, null=True)
    zoom = models.IntegerField(default=17)
    def __str__(self):
        return self.level1 + '--' + self.level2 + '--' + self.mapx

# visit target
class P_householder(models.Model):
    name = models.CharField(max_length=20)
    SEX_CHOICE = (
        ('1','Male'),
        ('0','Female'),
        ('2','Other'),
    )
    sex = models.CharField(
        max_length = 2,
        choices = SEX_CHOICE
    )
    street = models.CharField(max_length=100)
    num = models.CharField(max_length=20)
    RESPONSE_CHOICE = (
        ('1','Accept'),
        ('0','Refuse'),
    )
    response = models.CharField(
        max_length = 2,
        choices = RESPONSE_CHOICE
    )
    map_x = models.CharField(max_length=20,null=True)
    map_y = models.CharField(max_length=20,null=True)

class P_Record(models.Model):
    visit_date = models.DateTimeField()
    volunteer = models.ForeignKey(P_Volunteer)
    map = models.ForeignKey(P_Map)
    householder = models.ForeignKey(P_householder)