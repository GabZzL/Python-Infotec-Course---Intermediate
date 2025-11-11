from collections import ChainMap

# ChainMap
# Fusionar configuraciones por niveles (default → usuario → sistema).
# Gestionar entornos variables en programas.
# Simplificar búsquedas jerárquicas en múltiples diccionarios.

config_default = {'tema': 'claro', 'idioma': 'ingles'}
config_usuario = {'tema': 'oscuro'}

config = ChainMap(config_usuario, config_default)

print(config)
print(config['tema'])
print(config['idioma'])

print('-' * 40)

globales = {'x': 1, 'y': 2}
locales = {'y': 99, 'z': 3}

ambiente = ChainMap(locales, globales)

print(ambiente)
print(ambiente['y'])
print(ambiente['z'])