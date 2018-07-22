#comando
#python manage.py runscript script_bda.py --verbosity 0

import csv
from proyecto.models import *

# with open('victima.csv') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         victima = Victima.objects.create(nombres=row['nombres'],apellidos=row['apellidos'],edad=row['edad'],nacionalidad=row['nacionalidad'],ocupacion=row['ocupacion'],causa=row['causa'])
#         victima.save()
#
# with open('agresor.csv') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         agresor = Agresor.objects.create(nombres=row['nombres'],apellidos=row['apellidos'],edad=row['edad'],nacionalidad=row['nacionalidad'],ocupacion=row['ocupacion'])
#         agresor.save()
#
# with open('relacion.csv') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         relacion = Relacion.objects.create(tipo=row['tipo'],tiempo=row['tiempo'],agresion_previa=row['agresion_previa'],agresor_id=row['agresor_id'],victima_id=row['victima_id'])
#         relacion.save()

with open('femicidio.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        femicidio = Femicidio.objects.create(fecha=row['fecha'],hora=row['hora'],circunstancia=row['circunstancia'],tipo_arma=row['tipo_arma'],testigo=row['testigo'],agresor_id=row['agresor_id'],victima_id=row['victima_id'])
        femicidio.save()
