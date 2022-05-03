from django.db import models

# Create your models here.


class BookInfo(models.Model):
    name = models.CharField(max_length=10,unique=True)
    pub_data = models.DateField(null=True)
    read_count = models.IntegerField(default=0)
    commit_count = models.IntegerField(default=0)
    is_delete = models.BooleanField(default=False)

    class Meta:
        db_table = "bookinfo"
        verbose_name = "书籍管理"
