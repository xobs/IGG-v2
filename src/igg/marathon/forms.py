from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.core import validators as valids

from registration.forms import RegistrationFormUniqueEmail
from igg.marathon.models import *

class NoUsernameRegistrationForm(RegistrationFormUniqueEmail):
  username = forms.CharField(required=False, widget=forms.HiddenInput())
  first_name = forms.CharField(widget=forms.TextInput(attrs=dict(maxlength=30)),
                               label=_("First Name"))
  last_name = forms.CharField(widget=forms.TextInput(attrs=dict(maxlength=30)),
                               label=_("Last Name"))

  def __init__(self, *args, **kwargs):
    super(NoUsernameRegistrationForm, self).__init__(*args, **kwargs)
    self.fields.keyOrder = ['first_name', 'last_name', 'email',
                            'password1', 'password2', 'username']

  def clean_username(self):
    return self.cleaned_data['username']

  def clean_first_name(self):
    return self.cleaned_data['first_name'].title()

  def clean_last_name(self):
    return self.cleaned_data['last_name'].title()


class DonateForm(forms.Form):
  amount = forms.DecimalField(min_value=1.00, decimal_places=2, max_digits=14)
  email = forms.EmailField(required=True)
  comment = forms.CharField(required=False, widget=forms.Textarea)
  name = forms.CharField(required=False,max_length=100)
  twitter = forms.CharField(required=False, max_length=16,
                            validators=[valids.RegexValidator(regex='^\w{0,15}$')],
                            error_messages={'invalid': _(u'Enter a valid Twitter handle (no need for the @ sign).')})
  url = forms.URLField(required=False,max_length=200)
  game = forms.ModelChoiceField(required=False,
                                queryset=Game.objects.filter(visible=True),
                                empty_label="Select a game...")
  raffle = forms.ModelChoiceField(required=False,
                                  queryset=Raffle.objects.filter(visible=True),
                                  empty_label="Select a raffle...")
  challenge = forms.ModelChoiceField(required=False,
                                     queryset=Challenge.objects.filter(accepted=True),
                                     empty_label="Select a challenge...")

class GameEditForm(forms.ModelForm):
  class Meta:
    model = Game

class GameAddForm(forms.ModelForm):
  name = forms.CharField(max_length=200)
  developer = forms.CharField(max_length=200, required=False)
  site = forms.CharField(max_length=200)
  description = forms.CharField(required=False, widget=forms.Textarea)

  class Meta:
    model = Game
    exclude = ('visible', 'points')

class ProfileEditForm(forms.Form):
  first_name = forms.CharField(required=False, max_length=30)
  last_name = forms.CharField(required=False, max_length=30)
  email = forms.EmailField(required=False)
  url = forms.URLField(required=False, max_length=200)
  twitter = forms.CharField(required=False, max_length=16,
                            validators=[valids.RegexValidator(regex='^\w{0,15}$')],
                            error_messages={'invalid': _(u'Enter a valid Twitter handle (no need for the @ sign).')})


  def __init__(self, user, *args, **kwargs):
    super(ProfileEditForm, self).__init__(*args, **kwargs)
    self.user = user







