from django.db import models
from django.utils import timezone
from django.conf import settings
import readtime 
from django.utils.text import slugify
from django.db.models import Q
from django.core.exceptions import ValidationError
import re 


class PublishedManager(models.Manager): 
    def get_queryset(self):
        return (
            super().get_queryset().filter(status=Post.Status.PUBLISHED)
        )


class Post(models.Model):
    class Status(models.TextChoices): 
        DRAFT = "DF", "Draft"
        PUBLISHED = 'PB', "Published"
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)

    author =  models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='blog_posts'
    )
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created =  models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=2,
        choices=Status, 
        default=Status.DRAFT
    )
    objects = models.Manager()
    published = PublishedManager() 

    class Meta: 
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]
        unique_together = [['slug', 'publish']]
    def __str__(self):

        return self.title
    image = models.ImageField(upload_to='posts/', blank=True, null=True)
    excerpt = models.CharField(max_length=300, blank=True)
    
    @property
    def read_time(self):
        result = readtime.of_text(self.body)
        return result.minutes
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while Post.objects.filter(slug=slug).exclude(id=self.id).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        
        if not self.excerpt and self.body:
            self.excerpt = self.body[:300] + '...'
        
        super().save(*args, **kwargs)
    def clean(self):
        if not re.match(r'^[a-z0-9-]+$', self.slug):
            raise ValidationError(
                "Slug can only contain lowercase letters, numbers, and hyphens."
            )
    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.publish.year,
                                              self.publish.month,
                                              self.publish.day,
                                              self.slug])
