from django.db import models


# Create your models here.

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Author(TimeStampedModel):
    name = models.CharField(max_length=212)
    image = models.ImageField(upload_to='authors')
    profession = models.CharField(max_length=212)
    description = models.TextField()

    def __str__(self):
        return self.name


class Tag(TimeStampedModel):
    name = models.CharField(max_length=212)

    def __str__(self):
        return self.name


class Post(TimeStampedModel):
    title = models.CharField(max_length=212)
    body = models.TextField()
    image = models.ImageField(upload_to='posts')
    second_title = models.CharField(max_length=212)
    second_body = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title


class Comment(TimeStampedModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=212)
    email = models.EmailField()
    website = models.URLField()
    message = models.TextField()

    def __str__(self):
        return self.name


class About(TimeStampedModel):
    title = models.CharField(max_length=212)
    body = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

