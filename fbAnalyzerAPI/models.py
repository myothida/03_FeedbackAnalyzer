from django.db import models

class feedback(models.Model ):
    LANUGAGE_CHOICES = (('Eng','English'),('Burmese', 'Burmese') )
    language = models.CharField(max_length=6, choices=LANUGAGE_CHOICES)
    text = models.CharField()

    def __str__(self):
            return self.language
