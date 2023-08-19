from django.db import models

class NavApps(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Apps(models.Model):
    CHOICES = (
        ('Folder', 'Folder'),
        ('File', 'File'),
        ('App', 'App'),
    )
    app = models.ForeignKey(NavApps, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100, choices=CHOICES)
    img = models.ImageField(upload_to='images/', null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.name
