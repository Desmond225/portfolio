from django.db import models


# create a blog model

class Blog(models.Model):
    title = models.CharField(max_length=200)
    p_date = models.DateTimeField('Date published')
    body = models.TextField(max_length=200)
    image = models.ImageField(upload_to='images/')



#add blog app to settings

#create migration

#migrate

#add to the admin
