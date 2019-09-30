from django.db import models
def get_memo_image_path(instance, filename):
    return 'memo/%s/%s' % (instance.pk, filename)

class post(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    username=models.CharField(max_length=200,null=True)
    nickname = models.TextField(max_length=15,null=True)
    image = models.ImageField(upload_to=get_memo_image_path, default='')
    
    def save(self, *args, **kwargs):
        if self.id is None:            # 이미지 제외하고 업로드
            temp_image = self.image
            self.image = None
            super().save(*args, **kwargs)
                
                # 이미지 추가
            self.image = temp_image
            # 이미지만 업로드 => 이때는 pk가 존재!
        super().save(*args, **kwargs)

class postComent(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    username=models.CharField(max_length=200,null=True)
    post = models.ForeignKey(post, on_delete=models.CASCADE)
