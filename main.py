# Importer le module datetime
from datetime import datetime
import pytz

# Obtenir la date et l'heure actuelles
heure_actuelle = datetime.now()

# Formater l'heure au format "HH:MM:SS"
heure_formattee = heure_actuelle.strftime("%H:%M:%S")

# Afficher l'heure formatée dans la console
print(str(heure_formattee))
 

# Obtenir la date et l'heure actuelles au fuseau horaire UTC
heure_utc = datetime.now(pytz.utc)

# Définir les fuseaux horaires pour La Réunion et Paris
zone_reunion = pytz.timezone('Indian/Reunion')
zone_paris = pytz.timezone('Europe/Paris')

# Convertir l'heure UTC aux heures de La Réunion et de Paris
heure_reunion = heure_utc.astimezone(zone_reunion)
heure_paris = heure_utc.astimezone(zone_paris)

# Formater les heures au format "HH:MM:SS"
heure_reunion_formattee = heure_reunion.strftime("%H:%M:%S")
heure_paris_formattee = heure_paris.strftime("%H:%M:%S")

# Afficher les heures formatées dans la console
print("Heure à La Réunion:", str(heure_reunion_formattee))
print("Heure à Paris:", str(heure_paris_formattee))
