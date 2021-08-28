from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=15)
    password = forms.CharField(widget=forms.PasswordInput())
    '''
    def clean_message(self):
        username = self.cleaned_data.get("username")
        dbuser = User.objects.filter(username = username)
        
        if not dbuser:
            raise forms.ValidationError("User does not exist in our db!")
        return username
    '''

class CommentForm(forms.Form):
    text = forms.TextInput()