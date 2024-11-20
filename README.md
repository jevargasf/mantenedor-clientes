- Menú login:
	- Encriptación de contraseña con Fernet
	- Enmascarado de contraseña con maskpass
	
- Menu administrador
		- Gestión cliente: Agregar, Ver, Modificar, Deshabilitar
		- Gestión sucursal: Agregar, Ver, Modificar, Deshabilitar
		- Recuperar JSON: Pedir datos de ofertas laborales
			link: https://elprofemiguel.com/APIS_JSON/requisitos_formacion_api.json
		- Cerrar sesión
	- Menu comercial
		- Gestión asignaciones: Agregar, Ver, Modificar
		- Cerrar sesión

- Detalles:
	Perfil Administrador:
		Usuario: 18.038.889-3
		Contraseña: inacap123
	Perfil Comercial:
		Usuario: 10.113.060-6
		Contraseña: inacap321

- Features adicionales:
	- Módulo validadores: validador de datos enteros, strings y contraseña
	- Módulo validador de rut usando algoritmo módulo 11
	- Módulo funciones consola para controlar pausa y borrar consola en distintos sistemas operativos
    - no se rompe el programa cuando se ingresa un rut que ya fue registrado en la bbdd pero fue deshabilitado
	- si cliente ya existe: dos casos
    - el rut se encuentra, pero el estado = 0, ¿desea volver a habilitarlo en la base de datos?
    - comprueba si cliente ya está asignado a sucursal
	- asginaciones cuando el cliente ya fue eliminado
	- reconoce y reestablece cuando los registros ya fueron eliminados
