from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


class CheckInForm(forms.Form):
    badge_number = forms.CharField(label='Badge Number', max_length=8,
                                  # help_text="Enter a 5 digit badge number",
                                   required=True,
                                   initial='',
                                   widget=forms.TextInput(attrs={'autofocus': 'autofocus'}))

    def clean_badge_number(self):
        badge_number = self.cleaned_data['badge_number']

        badge_number = badge_number.strip("0")

        if 5 < len(badge_number) > 5:
            raise ValidationError(_('Invalid badge number length, must be 5 digits'))

        return badge_number

