# main.py
from arriendo_local_comercial import ArriendoLocalComercial
from arriendo_local_comida import ArriendoLocalComida

local_comercial = ArriendoLocalComercial("Juan Perez", 500)
local_comercial.establecer_valor_adicional_fijo(100)
local_comercial.establecer_arriendo_mensual()
print(local_comercial)

local_comida = ArriendoLocalComida("Maria Lopez", 300, 50, 30, 12)
local_comida.establecer_arriendo_mensual()
print(local_comida)
