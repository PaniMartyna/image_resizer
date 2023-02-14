from django.contrib.auth import get_user_model
from django.db import models

from images.validators import validate_file_type


class Picture(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    url = models.FileField(upload_to="pictures", validators=[validate_file_type])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Size(models.Model):
    height = models.PositiveIntegerField()

    def __str__(self):
        return f"Picture height: {self.height}"


class Thumbnail(models.Model):
    picture = models.ForeignKey("Picture", related_name="thumbnails", on_delete=models.CASCADE)
    url = models.FileField(upload_to="thumbnails")
    size = models.ForeignKey("Size", on_delete=models.CASCADE)

    def __str__(self):
        return f"Thumbnail for picture: {self.picture.name}. Height: {self.size.height}px"
