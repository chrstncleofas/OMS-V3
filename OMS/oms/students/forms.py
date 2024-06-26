from django import forms
from app.models import CustomUser
from students.models import Tablestudents, TimeLog

COURSE_CHOICES = [
    ('', '--- Select Course ---'),
    ('BS Computer Science', 'BS Computer Science'),
    ('BS Information Technology', 'BS Information Technology'),
]

PREFIX_CHOICES = [
    ('', '--- Select Prefix ---'),
    ('Jr', 'Jr'),
    ('III', 'III'),
    ('Senior', 'Senior'),
]

YEAR_CHOICES = [
    ('', '--- Select Year ---'),
    ('4th', '4th'),
    ('3rd', '3rd'),
    ('2nd', '2nd'),
    ('1st', '1st'),
]

class UserForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control'}
        )
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control'}
        )
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        email = cleaned_data.get("email")

        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', "Password and Confirm Password do not match")

        if CustomUser.objects.filter(email=email).exists():
            self.add_error('email', "Email already exists. Please use a different email address.")
        
        return cleaned_data

class StudentRegistrationForm(forms.ModelForm):
    StudentID = forms.CharField(
        max_length=10, 
        label='Student ID',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex. 18-0000'})
    )

    Course = forms.ChoiceField(
        choices=COURSE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    Prefix = forms.ChoiceField(
        choices=PREFIX_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=False
    )

    Year = forms.ChoiceField(
        choices=YEAR_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=False
    )

    class Meta:
        model = Tablestudents
        fields = ['StudentID', 'Firstname', 'Middlename', 'Lastname', 'Prefix', 'Number' ,'Course', 'Year']
        widgets = {
            'Firstname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter First Name'}),
            'Middlename': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Middle Name'}),
            'Lastname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Last Name'}),
            'Number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex. 09610090120'}),
        }

    def __init__(self, *args, **kwargs):
        super(StudentRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['Firstname'].required = True
        self.fields['Middlename'].required = True
        self.fields['Lastname'].required = True
        self.fields['Course'].required = True
        self.fields['Year'].required = True

class ChangePasswordForm(forms.Form):
    current_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Current password'})
    )
    new_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'New password'})
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm new password'})
    )

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get("new_password")
        confirm_password = cleaned_data.get("confirm_password")

        if new_password and confirm_password and new_password != confirm_password:
            self.add_error('confirm_password', "New password and confirm password do not match")

        return cleaned_data

class TimeLogForm(forms.ModelForm):
    class Meta:
        model = TimeLog
        fields = ['image', 'action']

    def __init__(self, *args, **kwargs):
        super(TimeLogForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = True
        self.fields['image'].widget.attrs.update({'accept': 'image/*'})
        self.fields['action'].widget = forms.HiddenInput()