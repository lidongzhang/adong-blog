from django import forms

class PostCommentForm(forms.Form):

    content_w = forms.Textarea(attrs={'style': 'width:80%;' })
    content = forms.CharField(widget =content_w, max_length=1000 )
    userNickname_email = forms.EmailField(max_length = 200, label = '登录名(email)', required = False)
    userPassword = forms.CharField(widget = forms.PasswordInput, max_length = 200, label='密码',required = False)
    ismember = forms.BooleanField(label='记住', required = False)  


