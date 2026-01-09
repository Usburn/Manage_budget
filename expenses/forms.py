from django import forms 

from .models import Depenses

from .models import Depenses, AutresDepenses

class DepensesForm(forms.ModelForm):
    class Meta:
        model = Depenses
        exclude= ["date", "slug"]
       
        widgets = {
            "Commentaires": forms.Textarea(attrs={"rows": 3, "placeholder": "Commentaires..."}),
        }



class AutresDepensesForm(forms.ModelForm):
    class Meta:
        model = AutresDepenses
        fields = [
            "Fairstone", 
            "REER_CELI",
            "Sol_Juline",
            "Assurance_Collective", 
            "Frais_utilisisation"
        ]


