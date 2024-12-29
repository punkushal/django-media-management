from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.
class MediaFile(models.Model):
    CATEGORY_CHOICES = [
        ('Audio','Audio'),
        ('Video','Video'),
        ('Image','Image'),
    ]
    file = models.FileField(upload_to='uploads/', validators=[FileExtensionValidator(allowed_extensions=['mp3','mp4','jpeg','gif','png'],),],)
    file_name = models.CharField(max_length=150)
    file_size = models.IntegerField()
    file_type = models.CharField(max_length=50)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    uploaded_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.filename

    def delete(self, *args, **kwargs):
        # Delete the file from filesystem when model is deleted
        self.file.delete()
        super().delete(*args, **kwargs)
