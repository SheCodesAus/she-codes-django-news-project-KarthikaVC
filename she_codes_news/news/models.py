from django.contrib.auth import get_user_model
from django.db import models
# Added by Karthika V
from django.urls import reverse


class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
        )
    pub_date = models.DateTimeField()
    content = models.TextField()
    # Added by Karthika V
    image_url = models.URLField(blank=True)

    def get_absolute_url(self):
        return reverse('news:story', kwargs={'pk':self.pk})
