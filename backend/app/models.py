from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.subject}"

class Registration(models.Model):
    COURSE_CHOICES = [
        ('web', 'Web Development'),
        ('data', 'Data Science'),
        ('ai', 'Artificial Intelligence'),
        ('mobile', 'Mobile Development'),
        ('cloud', 'Cloud Computing'),
    ]

    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    course = models.CharField(max_length=20, choices=COURSE_CHOICES)
    experience = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.full_name} - {self.get_course_display()}"
