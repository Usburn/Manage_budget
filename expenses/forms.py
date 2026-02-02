from django import forms 

from .models import Depenses

from .models import Depenses, AutresDepenses

class DepensesForm(forms.ModelForm):
    class Meta:
        model = Depenses
        exclude= ["slug"]
       
        widgets = {
            "Commentaires": forms.Textarea(attrs={"rows": 3, "placeholder": "Commentaires..."}),
        }



class AutresDepensesForm(forms.ModelForm):
    class Meta:
        model = Depenses
        exclude= ["slug"]
       
        widgets = {
            "Commentaires": forms.Textarea(attrs={"rows": 3, "placeholder": "Commentaires..."}),
        }


