from django.db import models
from django.utils import timezone
from django.utils.text import slugify

Months= ["Janvier", "Fevrier", "Mars", "Avril", "Mai", "Juin", "Juillet", "Aout", "Septembre",
         "Octobre", "Novembre", "Decembre"]


class Depenses(models.Model):
    date = models.DateTimeField( default=timezone.now)
    slug = models.SlugField( blank=True, null=True, db_index=True)
    Loyer = models.IntegerField(blank=True, null=True)
    Burnie_frais= models.FloatField(blank=True, null=True)
    Essence = models.FloatField(blank=True, null=True)
    Scolarite = models.FloatField(blank=True, null=True)
    Auto_Assurance = models.IntegerField(blank=True, null=True)
    Habitation_Assurance = models.IntegerField(blank=True, null=True)
    Fairstone = models.FloatField(blank=True, null=True)
    Internet = models.FloatField(blank=True, null=True)
    Electricite= models.FloatField(blank=True, null=True)
    Tel_Zaro = models.FloatField(blank=True, null=True)
    Tel_Juline= models.FloatField(blank=True, null=True)
    NetFlix = models.FloatField(blank=True, null=True)
    Zaro_mom  = models.FloatField(blank=True, null=True)
    Juline_family = models.FloatField(blank=True, null=True)
    Don = models.FloatField(blank=True, null=True)
    Nourriture= models.FloatField(blank=True, null=True)
    Loisir = models.FloatField(blank=True, null=True)
    Autres = models.FloatField(blank=True, null=True)
    Commentaires = models.TextField(
        blank=True,
        null=True
    )

    def save(self, *args, **kwargs):
        dt = self.date or timezone.now()
        currentMonth = dt.month
        currentMonth_string = Months[currentMonth - 1]
        currentYear = dt.year
        self.slug = slugify(f"{currentMonth_string}-{currentYear}")
        super().save(*args, **kwargs)

    
    def __str__(self):
        try:
            dt = self.date or timezone.now()
            return f"{dt.strftime('%d/%m/%Y')}  {self.Commentaires or ''}"

        
        except Exception:
            return f"Dépenses (invalid date)"
        

class AutresDepenses(models.Model):
    date = models.DateTimeField( auto_now_add=True)
    slug = models.SlugField( blank=True, null=True, db_index=True)
    Fairstone = models.FloatField(blank=True, null=True)
    REER_CELI= models.FloatField(blank=True, null=True)
    Sol_Juline = models.FloatField(blank=True, null=True)
    Assurance_Collective = models.FloatField(blank=True, null=True)
    Frais_utilisisation = models.FloatField(blank=True, null=True)

    def save(self, *args, **kwargs):
        dt = self.date or timezone.now()
        currentMonth = dt.month
        currentMonth_string = Months[currentMonth - 1]
        currentYear = dt.year
        self.slug = slugify(f"{currentMonth_string}-{currentYear}")
        super().save(*args, **kwargs)

     
    def __str__(self):
        try:
            dt = self.date or timezone.now()
            month_str = Months[dt.month - 1]
            year = dt.year
            return f"{dt.strftime('%d/%m/%Y')}  {self.Commentaires or ''}"
            # return f"Dépenses {month_str} {year}"
        
        except Exception:
            return f"Dépenses (invalid date)"


class Revenue(models.Model):
    date = models.DateTimeField( auto_now_add=True)
    slug = models.SlugField( blank=True, null=True, db_index=True)
    Zaro_Revenue = models.FloatField(blank=True, null=True)
    Juline_Revenue = models.FloatField(blank=True, null=True)
    Don = models.FloatField(blank=True, null=True)

    def save(self, *args, **kwargs):
        dt = self.date or timezone.now()
        currentMonth = dt.month
        currentMonth_string = Months[currentMonth - 1]
        currentYear = dt.year
        self.slug = slugify(f"{currentMonth_string}-{currentYear}")
        super().save(*args, **kwargs)

     
    def __str__(self):
        try:
            dt = self.date or timezone.now()
            month_str = Months[dt.month - 1]
            year = dt.year
            return f"Revenue {month_str} {year}"
        except Exception:
            return f"Revenue (invalid date)"

   



  

  









  

