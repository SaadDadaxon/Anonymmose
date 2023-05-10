from django.db import models


class Dashboard(models.Model):
    title = models.CharField(max_length=228)
    image = models.ImageField(upload_to='dash_board/')
    text = models.TextField()

    def __str__(self):
        return self.title
