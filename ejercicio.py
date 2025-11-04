

import re


correos = [
    "alejandro@example.com",
    "olayaaa@dominio.co",
    "diegoooo@dominio",
    "urueñaaa@dominio..com",
    "@hermanaaaaa.com",
    "malllllllll@dominio.com"
]


patron = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

# Lambda para validar el correo con regex
validar = lambda c: re.match(patron, c)

# Filtrar solo los correos válidos
correos_validos = list(filter(validar, correos))
print("Correos válidos:", correos_validos)

# Filtrar los inválidos
correos_invalidos = list(filter(lambda c: not re.match(patron, c), correos))
print("Correos inválidos:", correos_invalidos)

# Obtener el usuario (parte antes del @) solo de los válidos
usuarios = list(map(lambda c: c.split('@')[0], correos_validos))
print("Usuarios válidos extraídos:", usuarios)

