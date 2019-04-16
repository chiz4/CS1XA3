from django.db import models


# Create your models here.

class GameUser(models.Model):
    '''User table'''
    sexchoice=(
        ('m','male'),
        ('f','famale'),
    )
    u_id = models.AutoField(primary_key=True)
    user_name=models.CharField(max_length=64, unique=True)
    password = models.CharField(max_length=256)
    register_email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32, choices=sexchoice, default='male')
    register_time = models.DateTimeField(auto_now_add=True)
    REQUIRED_FIELDS = ['password']
    USERNAME_FIELD='user_name'

    def __str__(self):
        return self.user_name

    class Meta:
        ordering = ['register_time']
        db_table = "user"
    __repr__ = __str__
class ScoreRecord(models.Model):
    '''score record table'''
    s_id=models.AutoField(primary_key=True)
    u_id=models.ForeignKey('GameUser',to_field='u_id',on_delete='CASCADE')
    max_score=models.IntegerField()
    get_time=models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "score"
