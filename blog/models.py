from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    number_of_positive_comments = models.IntegerField(default=0)
    number_of_negative_comments = models.IntegerField(default=0)
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
    def getPercentageOfPositiveComments(self):
        p = self.number_of_positive_comments / (self.number_of_positive_comments + self.number_of_negative_comments) * 100
        return p

    def getPercentageOfNegativeComments(self):
        p = self.number_of_negative_comments / (self.number_of_positive_comments + self.number_of_negative_comments) * 100
        return p

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)
    POSITIVE = 'P'
    NEGATIVE = 'N'
    COMMENT_TYPE = [
        (POSITIVE, 'positive'),
        (NEGATIVE, 'negative'),
    ]
    comment_type = models.CharField(
        max_length=2,
        choices=COMMENT_TYPE,
        default=POSITIVE,
    )
    
    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)
