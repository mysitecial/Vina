from clients.models import Client
from django import forms
from django.core.exceptions import ValidationError
from django.forms import modelformset_factory

from .models import Client, Package, Project, Shot


class PackageForm(forms.ModelForm):
    project = forms.ModelChoiceField(queryset=Project.objects.all(), required=False)

    class Meta:
        model = Package
        fields = ["package_name", "project"]

    def __init__(self, *args, **kwargs):
        client_id = kwargs.pop("client_id", None)
        super().__init__(*args, **kwargs)
        self.fields["project"].required = False
        if "project" in self.fields:
            self.fields["package_name"].required = False

        if client_id:
            self.fields["project"].queryset = Project.objects.filter(
                client_id=client_id
            )
        else:
            self.fields["project"].queryset = Project.objects.none()


class ShotForm(forms.ModelForm):
    class Meta:
        model = Shot
        fields = ["shot_name", "md", "word_ref", "delivery_date", "status"]
        widgets = {
            "delivery_date": forms.DateInput(attrs={"type": "date"}),
        }


ShotFormSet = modelformset_factory(
    Shot,
    form=ShotForm,
    extra=1,
    can_delete=True,
    max_num=None,  # Cho phép số lượng form không giới hạn
    validate_max=False,  # Không kiểm tra giới hạn tối đa
)


class ProjectForm(forms.ModelForm):
    project = forms.ModelChoiceField(queryset=Project.objects.all(), required=False)

    class Meta:
        model = Project
        fields = ["project_name", "client"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["project_name"].required = False
