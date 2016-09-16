from django import forms

class EmailForm(forms.Form):
    fromEmail = forms.EmailField(max_length=100, label='您的邮件地址')
    title = forms.CharField(max_length=200, label='标题')
    message = forms.CharField(widget=forms.Textarea, label='内容')
    
