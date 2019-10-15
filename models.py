from django.db import models

# Create your models here.
class Department(models.Model):
    dname=models.CharField('部门名',max_length=20)
    level=models.CharField('级别',max_length=2,default='2')
class user(models.Model):
    uname=models.CharField('用户名',max_length=32)
    did=models.ForeignKey(to=Department,on_delete='cascade')
    readfile=models.CharField('读取文件',max_length=1,default='0')
    writefile=models.CharField('写入文件',max_length=1,default='0')
    deletefile=models.CharField('删除文件',max_length=1,default='0')
    # super=models.CharField('超级用户',max_length=1,default='0')
class File(models.Model):
    dz=models.CharField('地址',max_length=32)
    uid=models.ManyToManyField(to='User',on_delete='cascade')
    did=models.ManyToManyField(to='Department',on_delete='cascade')