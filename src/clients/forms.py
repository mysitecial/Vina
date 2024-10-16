from django import forms

from .models import Client


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ["name", "country", "area"]  # Thêm các trường khác nếu cần
