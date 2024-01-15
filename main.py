# Importer le module datetime
from datetime import datetime

# Obtenir la date et l'heure actuelles
heure_actuelle = datetime.now()

# Formater l'heure au format "HH:MM:SS"
heure_formattee = heure_actuelle.strftime("%H:%M:%S")

# Afficher l'heure formatée dans la console
print(str(heure_formattee))
