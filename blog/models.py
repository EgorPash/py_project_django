from django.db import models
from django.utils.text import slugify


class BlogPost(models.Model):
    objects = None
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)  # Убираем уникальность
    content = models.TextField()
    preview_image = models.ImageField(upload_to='blog/')
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)
    views_count = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title