def validar_datos(nombre: str, edad: int, correo: str):
    print('-' * 50)
    # validar nombre
    if not nombre.strip():
        print('El nombre ingresado es invalido')
        return
    # Validar edad
    if not isinstance(edad, int) or edad <= 0:
        print('El numero ingresado es invalido')
        return
    # Validad correo
    if not correo.count('@') == 1:
        print('El correo ingresado es invalido')
        return
     
    print('Los datos se han registrado')
    print(f'Nombre: {nombre}')
    print(f'Edad: {edad}')
    print(f'Correo: {correo}')
    
def probar_validaciones():
    print('Validando datos...')
    
    validar_datos('Armando', 24, 'armando@gmail.com')
    validar_datos('Gabriel', 9.9, 'gabriel@gmail.com')
    validar_datos('Ivan', 25, 'ivangmail.com')
    
try: 
    probar_validaciones()
except ValueError:
    print('Error: Alguno de los datos ingresados es invalido')
except KeyboardInterrupt:
    print('Error: Programa cancelado por el usuario')
except Exception as e:
    print(f'Error: {e}')
finally:
    print('-' * 50)
    print('Programa finalizado.')
    
