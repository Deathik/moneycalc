from django.db import models


class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    feedback = models.TextField()
    reviewed = models.BooleanField(default=False)

    def __str__(self):
        return "'{}' response".format(self.email)