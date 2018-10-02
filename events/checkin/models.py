from django.db import models


class Guest(models.Model):
    name = models.CharField(max_length=200)
    badge_number = models.CharField(max_length=5, primary_key=True)
    is_checked_in = models.BooleanField(default=False)

    def __str__(self):
        return self.badge_number

    def is_checked_in_str(self):
        if self.is_checked_in:
            return "True"
        else:
            return "False"

    def check_in(self):
        if self.is_checked_in:
            return False
        else:
            self.is_checked_in = True
            return True

