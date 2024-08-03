from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(min_length=2, max_length=50)
    email = forms.EmailField()
    subject = forms.CharField(widget=forms.Textarea())
    message = forms.CharField(min_length=2, max_length=255)


    def send_mail(self):
        pass
