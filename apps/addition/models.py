from django.db import models


class addition_logs(models.Model):
    first_number = models.IntegerField(null=False, blank=False)
    second_number = models.IntegerField(null=False, blank=False)
    result = models.IntegerField(default=None)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.pk)
    
    def save(self, *args, **kwargs):
        self.result = self.first_number + self.second_number
        return super(addition_logs, self).save(*args, **kwargs)