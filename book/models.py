from django.db import models

# Create your models here.


class BookInfo(models.Model):
    name = models.CharField(max_length=10,unique=True)
    pub_data = models.DateField(null=True)
    read_count = models.IntegerField(default=0)
    commit_count = models.IntegerField(default=0)
    is_delete = models.BooleanField(default=False)
    def __str__(self):
        return self.name
    class Meta:
        db_table = "bookinfo"
        verbose_name = "书籍管理"
#     1对多模型中
#       系统自动创建一个多的peopleinfo_set
#       people_set = [PeopleInfo,PeopleInfo...]



class PeopleInfo(models.Model):
    gender_choice = (
        (1,'male'),
        (2,'female')
    )

    name = models.CharField(max_length=10,unique=True)
    gender = models.SmallIntegerField(choices=gender_choice,default=1)
    description = models.CharField(max_length=100,null=True)
    is_delete = models.BooleanField(default=False)

    book = models.ForeignKey(BookInfo,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    class Meta:
        db_table = "peopleinfo"