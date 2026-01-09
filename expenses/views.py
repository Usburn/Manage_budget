
from django.db.models.functions import ExtractMonth, ExtractYear
from django.db.models import Sum, FloatField
import datetime
from django.db.models.functions import Coalesce
from datetime import datetime, timezone
from django.utils import timezone as dj_timezone
from django.shortcuts import render, redirect
from django.db.models import Sum, FloatField
from .models import Depenses , AutresDepenses
from .forms import DepensesForm, AutresDepensesForm

# Create your views here.




Months= ["Janvier", "Fevrier", "Mars", "Avril", "Mai", "Juin", "Juillet", "Aout", "Septembre",
         "Octobre", "Novembre", "Decembre"]




# Liste et création des dépenses




def Home(request):
    # --- FORMULAIRES ---
    if request.method == "POST":

        # ===== FORMULAIRE DEPENSES =====
        if "submit_depenses" in request.POST:
            form_depenses = DepensesForm(request.POST)
            form_autres = AutresDepensesForm()

            if form_depenses.is_valid():
                form_depenses.save()
                return redirect("Home_page")

        # ===== FORMULAIRE AUTRES DEPENSES =====
        elif "submit_autres" in request.POST:
            form_autres = AutresDepensesForm(request.POST)
            form_depenses = DepensesForm()

            if form_autres.is_valid():
                form_autres.save()
                return redirect("Home_page")

    else:
        form_depenses = DepensesForm()
        form_autres = AutresDepensesForm()

    # --- DATE COURANTE ---
    today = dj_timezone.now()
    current_year = today.year
    current_month = today.month

    start_month = datetime(current_year, current_month, 1)
    end_month = (
        datetime(current_year + 1, 1, 1)
        if current_month == 12
        else datetime(current_year, current_month + 1, 1)
    )

    # --- DEPENSES MENSUELLES ---
    depenses_mensuelles = Depenses.objects.filter(
        date__gte=start_month,
        date__lt=end_month
    ).aggregate(
        M_loyer=Coalesce(Sum('Loyer', output_field=FloatField()), 0.0),
        M_Burnie_frais=Coalesce(Sum('Burnie_frais', output_field=FloatField()), 0.0),
        M_Essence=Coalesce(Sum('Essence', output_field=FloatField()), 0.0),
        M_Scolarite=Coalesce(Sum('Scolarite', output_field=FloatField()), 0.0),
        M_auto_assurance=Coalesce(Sum('Auto_Assurance', output_field=FloatField()), 0.0),
        M_habitation_assurance=Coalesce(Sum('Habitation_Assurance', output_field=FloatField()), 0.0),
        M_Fairstone=Coalesce(Sum('Fairstone', output_field=FloatField()), 0.0),
        M_Internet=Coalesce(Sum('Internet', output_field=FloatField()), 0.0),
        M_Electricite=Coalesce(Sum('Electricite', output_field=FloatField()), 0.0),
        M_Tel_Zaro=Coalesce(Sum('Tel_Zaro', output_field=FloatField()), 0.0),
        M_Tel_Juline=Coalesce(Sum('Tel_Juline', output_field=FloatField()), 0.0),
        M_NetFlix=Coalesce(Sum('NetFlix', output_field=FloatField()), 0.0),
        M_Zaro_mom=Coalesce(Sum('Zaro_mom', output_field=FloatField()), 0.0),
        M_Juline_family=Coalesce(Sum('Juline_family', output_field=FloatField()), 0.0),
        M_Don=Coalesce(Sum('Don', output_field=FloatField()), 0.0),
        M_Loisir=Coalesce(Sum('Loisir', output_field=FloatField()), 0.0),
        M_Nourriture=Coalesce(Sum('Nourriture', output_field=FloatField()), 0.0),   
      
    )

  # ---Autres  DEPENSES MENSUELLES ---

    autres_depenses_mensuelles = AutresDepenses.objects.filter(
    date__gte=start_month,
    date__lt=end_month
).aggregate(
    fairstone=Coalesce(Sum('Fairstone', output_field=FloatField()), 0.0),
         reer_celi=Coalesce(Sum('REER_CELI', output_field=FloatField()), 0.0),
         sol_juline=Coalesce(Sum('Sol_Juline', output_field=FloatField()), 0.0),
         assurance_collective=Coalesce(Sum('Assurance_Collective', output_field=FloatField()), 0.0),
         frais_utilisation=Coalesce(Sum('Frais_utilisisation', output_field=FloatField()), 0.0),
)
    


    autres_depenses_annuelles = AutresDepenses.objects.filter( date__year=current_year
).aggregate(
    fairstone=Coalesce(Sum('Fairstone', output_field=FloatField()), 0.0),
         reer_celi=Coalesce(Sum('REER_CELI', output_field=FloatField()), 0.0),
         sol_juline=Coalesce(Sum('Sol_Juline', output_field=FloatField()), 0.0),
         assurance_collective=Coalesce(Sum('Assurance_Collective', output_field=FloatField()), 0.0),
         frais_utilisation=Coalesce(Sum('Frais_utilisisation', output_field=FloatField()), 0.0),
)


    # --- TOTAL ANNUEL ---
    total_annuel = Depenses.objects.filter(date__year=current_year).aggregate(
        T_loyer=Coalesce(Sum('Loyer', output_field=FloatField()), 0.0),
        T_Burnie_frais=Coalesce(Sum('Burnie_frais', output_field=FloatField()), 0.0),
        T_Essence=Coalesce(Sum('Essence', output_field=FloatField()), 0.0),
        T_Scolarite=Coalesce(Sum('Scolarite', output_field=FloatField()), 0.0),
        T_auto_assurance=Coalesce(Sum('Auto_Assurance', output_field=FloatField()), 0.0),
        T_habitation_assurance=Coalesce(Sum('Habitation_Assurance', output_field=FloatField()), 0.0),
        T_Fairstone=Coalesce(Sum('Fairstone', output_field=FloatField()), 0.0),
        T_Internet=Coalesce(Sum('Internet', output_field=FloatField()), 0.0),
        T_Electricite=Coalesce(Sum('Electricite', output_field=FloatField()), 0.0),
        T_Tel_Zaro=Coalesce(Sum('Tel_Zaro', output_field=FloatField()), 0.0),
        T_Tel_Juline=Coalesce(Sum('Tel_Juline', output_field=FloatField()), 0.0),
        T_NetFlix=Coalesce(Sum('NetFlix', output_field=FloatField()), 0.0),
        T_Zaro_mom=Coalesce(Sum('Zaro_mom', output_field=FloatField()), 0.0),
        T_Juline_family=Coalesce(Sum('Juline_family', output_field=FloatField()), 0.0),
        T_Don=Coalesce(Sum('Don', output_field=FloatField()), 0.0),
        T_Loisir=Coalesce(Sum('Loisir', output_field=FloatField()), 0.0),
        T_Nourriture=Coalesce(Sum('Nourriture', output_field=FloatField()), 0.0), 
    )

    total_depenses_mensuelles = (
        sum(depenses_mensuelles.values()) +
        sum(autres_depenses_mensuelles.values())
    )

    Annuel_general = (
        sum(total_annuel.values()) +
        sum(autres_depenses_annuelles.values())
    )

    

    month = Months[current_month-1]

    # --- CONTEXTE ---
    context = {
        "form_depenses": form_depenses,
        "form_autres": form_autres,
        "total_annuel":total_annuel,
        "autres_depenses_annuelles":autres_depenses_annuelles,
        "Annuel_general":Annuel_general,
        "depenses_mensuelles": depenses_mensuelles,
        "autres_depenses_mensuelles":autres_depenses_mensuelles,
        "total_depenses_mensuelles":   total_depenses_mensuelles,
        "month": month,
        "year": current_year,
    }

    return render(request, "expenses/Home.html", context)








from django.shortcuts import render
from django.db.models import Sum, FloatField
from django.db.models.functions import Coalesce, ExtractMonth
from django.utils import timezone as dj_timezone
from .models import Depenses, AutresDepenses

Months = ["Janvier", "Fevrier", "Mars", "Avril", "Mai", "Juin", "Juillet", "Aout", "Septembre",
          "Octobre", "Novembre", "Decembre"]

from django.shortcuts import render
from django.db.models import Sum, FloatField
from django.db.models.functions import Coalesce, ExtractMonth
from django.utils import timezone as dj_timezone
from .models import Depenses, AutresDepenses

Months = ["Janvier", "Fevrier", "Mars", "Avril", "Mai", "Juin", "Juillet", "Aout",
          "Septembre", "Octobre", "Novembre", "Decembre"]

from django.shortcuts import render
from django.db.models import Sum, FloatField
from django.db.models.functions import Coalesce, ExtractMonth
from django.utils import timezone as dj_timezone

# Liste des mois en français
Months = [
    "Janvier", "Fevrier", "Mars", "Avril", "Mai", "Juin",
    "Juillet", "Aout", "Septembre", "Octobre", "Novembre", "Decembre"
]
import calendar
def all_months(request):

    # --- DATE COURANTE ---
    today = dj_timezone.now()
    current_year = today.year
    current_month = today.month

    months_data = []

    # --- BOUCLE SUR LES 12 MOIS ---
    for month in range(1, 13):

        # --- BORNES DU MOIS ---
        start_month = datetime(current_year, month, 1)

        if month == 12:
            end_month = datetime(current_year + 1, 1, 1)
        else:
            end_month = datetime(current_year, month + 1, 1)

        # --- DEPENSES PRINCIPALES ---
        depenses = Depenses.objects.filter(
            date__gte=start_month,
            date__lt=end_month
        ).aggregate(
            M_loyer=Coalesce(Sum('Loyer', output_field=FloatField()), 0.0),
            M_Burnie_frais=Coalesce(Sum('Burnie_frais', output_field=FloatField()), 0.0),
            M_Essence=Coalesce(Sum('Essence', output_field=FloatField()), 0.0),
            M_Scolarite=Coalesce(Sum('Scolarite', output_field=FloatField()), 0.0),
            M_auto_assurance=Coalesce(Sum('Auto_Assurance', output_field=FloatField()), 0.0),
            M_habitation_assurance=Coalesce(Sum('Habitation_Assurance', output_field=FloatField()), 0.0),
            M_Fairstone=Coalesce(Sum('Fairstone', output_field=FloatField()), 0.0),
            M_Internet=Coalesce(Sum('Internet', output_field=FloatField()), 0.0),
            M_Electricite=Coalesce(Sum('Electricite', output_field=FloatField()), 0.0),
            M_Tel_Zaro=Coalesce(Sum('Tel_Zaro', output_field=FloatField()), 0.0),
            M_Tel_Juline=Coalesce(Sum('Tel_Juline', output_field=FloatField()), 0.0),
            M_NetFlix=Coalesce(Sum('NetFlix', output_field=FloatField()), 0.0),
            M_Zaro_mom=Coalesce(Sum('Zaro_mom', output_field=FloatField()), 0.0),
            M_Juline_family=Coalesce(Sum('Juline_family', output_field=FloatField()), 0.0),
            M_Don=Coalesce(Sum('Don', output_field=FloatField()), 0.0),
            M_Loisir=Coalesce(Sum('Loisir', output_field=FloatField()), 0.0),
            M_Nourriture=Coalesce(Sum('Nourriture', output_field=FloatField()), 0.0),
        )

        # --- AUTRES DEPENSES ---
        autres = AutresDepenses.objects.filter(
            date__gte=start_month,
            date__lt=end_month
        ).aggregate(
            fairstone=Coalesce(Sum('Fairstone', output_field=FloatField()), 0.0),
            reer_celi=Coalesce(Sum('REER_CELI', output_field=FloatField()), 0.0),
            sol_juline=Coalesce(Sum('Sol_Juline', output_field=FloatField()), 0.0),
            assurance_collective=Coalesce(Sum('Assurance_Collective', output_field=FloatField()), 0.0),
            frais_utilisation=Coalesce(Sum('Frais_utilisisation', output_field=FloatField()), 0.0),
        )

        # --- TOTAL DU MOIS ---
        total_mois = sum(depenses.values()) + sum(autres.values())

        # --- STRUCTURE POUR LE TEMPLATE ---
        months_data.append({
            "name": calendar.month_name[month],  # Janvier, Février, etc.
            "depenses": depenses,
            "autres": autres,
            "total": total_mois,
        })

    months_data = months_data[:current_month][::-1]

    return render(request, "expenses/all_months.html", {
        "year": current_year,
        "months_data": months_data,
    })





def monthly_expenses(request, slug):
    return render(request, "expenses/single_month.html")