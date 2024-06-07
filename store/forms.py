from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm
from django import forms
from .models import Customer, ProductCustomization


class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=True, label='Search')
    
class ChangePasswordForm(SetPasswordForm):
    class Meta:
        model = Customer
        fields = ['new_password1', 'new_password2']

    def __init__(self, *args, **kwargs):
        super(ChangePasswordForm, self).__init__(*args, **kwargs)

        self.fields['new_password1'].widget.attrs['class'] = 'form-control'
        self.fields['new_password1'].widget.attrs['placeholder'] = 'New Password'
        self.fields['new_password1'].label = ''
        self.fields['new_password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password or a previously used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['new_password2'].widget.attrs['class'] = 'form-control'
        self.fields['new_password2'].widget.attrs['placeholder'] = 'Confirm New Password'
        self.fields['new_password2'].label = ''
        self.fields['new_password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'


class UpdateUserForm(UserChangeForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    company_name = forms.CharField(label="", max_length=70, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Company Name'}))
    #Hide password text at bottom of for
    password = None

    class Meta:
        model = Customer
        fields = ('company_name', 'first_name', 'last_name', 'email')




# SignUpForm for Customer model
class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    company_name = forms.CharField(label="", max_length=70, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Company Name'}))
    phone = forms.CharField(label="", max_length=11, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}))

    class Meta:
        model = Customer
        fields = ('company_name', 'first_name', 'last_name', 'email', 'phone', 'password1', 'password2')

# ProductCustomizationForm for ProductCustomization model
class CombinedForm(forms.Form):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    company_name = forms.CharField(label="", max_length=70, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Company Name'}))
    phone = forms.CharField(label="", max_length=11, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}))
    password1 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))
    logo_image = forms.ImageField(label="Upload Company Logo", required=False, widget=forms.FileInput(attrs={'class': 'form-control'}))
    use_default_font = forms.BooleanField(label="Use Company Name as Logo", required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    industry = forms.CharField(label="Industry", max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Industry'}))
    services = forms.CharField(label="Services", max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Services'}))
    company_established = forms.DateField(label="Company Established", required=False, widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'placeholder': 'Company Established'}))
    about_company = forms.CharField(label="About Your Company", required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'About Your Company'}))
    target_market = forms.CharField(label="Target Market", required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Target Market'}))
    areas_covered = forms.CharField(label="Areas Your Business Covers", required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Areas Your Business Covers'}))
    reference_website = forms.URLField(label="Reference Website (Website You Like)", required=False, widget=forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Reference Website'}))

    class Meta:
        fields = ('company_name', 'first_name', 'last_name', 'email', 'phone', 'password1', 'password2', 'logo_image', 'use_default_font', 'industry', 'services', 'company_established', 'about_company', 'target_market', 'areas_covered', 'reference_website', 'additional_preference')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['email'].label = ''

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'

        self.fields['logo_image'].widget.attrs['class'] = 'form-control'
        self.fields['use_default_font'].widget.attrs['class'] = 'form-check-input'