from django.db import models

class video(models.Model):
    title = models.CharField("Title",max_length=200)
    embed_code = models.TextField("enbade")