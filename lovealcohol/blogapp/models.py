from django.db import models

def get_memo_image_path(instance, filename):
    return 'memo/%s/%s' % (instance.pk, filename)

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_data = models.DateTimeField('data published')
    # image = models.ImageField(upload_to='images/')
    body = models.TextField()
    username = models.CharField(max_length=200, null=True)
    nickname = models.TextField(max_length=15,null=True)
    image = models.ImageField(upload_to=get_memo_image_path, default='')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]
        
    def save(self, *args, **kwargs):
        if self.id is None:
            temp_image = self.image
            self.image = None
            super().save(*args, **kwargs)
            self.image = temp_image
        super().save(*args, **kwargs)