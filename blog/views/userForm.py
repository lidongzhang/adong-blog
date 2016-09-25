from django import forms

class UserForm(forms.Form):

    #content_w = forms.Textarea(attrs={'style': 'width:80%;' })
    name = forms.CharField(max_length=50, label='姓名' )
    nickname_email = forms.EmailField(max_length = 200, label = '登录名(email)', required = True    )
    password = forms.CharField(widget = forms.PasswordInput, max_length = 200, label='密码',required = True )
    password1 = forms.CharField(widget = forms.PasswordInput, max_length = 200, label='密码确认',required = True )
    
    ismember = forms.BooleanField(label='记住', required = False)  


