from django.conf import settings
from django.db import models
from django.db.models import JSONField
from django.core.exceptions import ValidationError

def validate_planned_calories(value):
    if not value:
        raise ValidationError('Planned calories cannot be empty')


# create a meal model
class Meal(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    selectedDate = models.CharField(max_length=8)
    plannedCalories = models.IntegerField(validators=[validate_planned_calories])
    breakfast = JSONField(default=list)
    lunch = JSONField(default=list)
    snack = JSONField(default=list)
    dinner = JSONField(default=list)

    # make a unique combination of user and selected date
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'selectedDate'], name='unique_user_selected_date')
        ]
