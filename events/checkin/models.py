from django.db import models


class Guest(models.Model):
    name = models.CharField(max_length=200)
    badge_number = models.CharField(max_length=6, primary_key=True)
    department = models.CharField(max_length=30, default="None")
    number_check_ins = models.IntegerField(default=0)
    is_checked_in = models.BooleanField(default=False)

    def __str__(self):
        return self.badge_number

    @classmethod
    def create(cls, name, badge_number, department):
        guest = cls(name=name, badge_number=badge_number, department=department)
        return guest

    def is_checked_in_str(self):
        if self.is_checked_in:
            return "True"
        else:
            return "False"

    def check_in(self):
        if self.is_checked_in:
            return False
        else:
            if self.number_check_ins < 2:
                self.number_check_ins = self.number_check_ins + 1
            if self.number_check_ins >= 2:
                self.is_checked_in = True
            return True

