try:
    numero = int(input('Ingresa un numero: '))
    resultado = 100 / numero
    print(f'Resultado: {resultado}')
# Excepcion especifica
except ValueError:
    print('Error: El valor ingresado no es valido.')
except ZeroDivisionError:
    print('Error: No hay division entre cero.')
# Excepcion general
except Exception as e:
    print(f'Error Inesperado: {str(e)}')
finally:
    print('Programa finalizado')