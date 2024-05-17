from django.db import models

TRIM_LIMIT = 50


class Tag(models.Model):
    tag_name = models.CharField(max_length=50)

    def __str__(self):
        return self.tag_name


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag, related_name="posts")

    def __str__(self):
        return f"{self.title}: {self.body[:TRIM_LIMIT]}" + (
            "..." if len(self.body) > TRIM_LIMIT else ""
        )


class SideNote(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}: {self.body[:TRIM_LIMIT]}" + (
            "..." if len(self.body) > TRIM_LIMIT else ""
        )
