from django import forms

class ContactAdminForm(forms.Form):
    from_email = forms.EmailField(required=True, label="Email")
    subject = forms.CharField(required=True, label="Asunto")
    message = forms.CharField(widget=forms.Textarea, required=True, label="Mensaje")
   # company = forms.ModelChoiceField(queryset=Organization.objects.all(), required=True, help_text="Organización")
