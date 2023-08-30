from django.db import models

class Chat(models.Model):
    # id = models.AutoField(primary_key=True)
    symptoms = models.CharField(max_length=999)
    remedy = models.CharField(max_length=999)

    class Meta:
        db_table = 'chat'
    def __str__(self):
        return '' + self.symptoms + ' - ' + self.remedy
class Contact(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=900)
    email= models.CharField(max_length=900)
    message= models.TextField()
    time = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        db_table = 'contact'
    
    def __str__(self):
        return '' + self.name + ' - ' + self.time.strftime('%Y-%m-%d %H:%M:%S')