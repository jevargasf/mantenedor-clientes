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
	- Mostrar los registros como tabla

P4:
- CRUD de usuarios, perfil administrador
	✓ Agregar usuario con contraseña encriptada*
	- Listar usuarios
	- Modificar usuario
	- Dar de baja usuario
	✓ No es necesario agregar otro perfil adicional, con los dos perfiles que existen es suficiente.

- Debug antes de entregar:
	✓ revisar si todas las funciones donde pide el RUT se quiebran cuando se ingresa un rut no
	válido (si no continúa la ejecución de la función con un rut vacío)
	- revisar si el programa corre en un nuevo entorno y con una bbdd nueva desde cero
	- se puede mejorar el programa almacenando todos los string como mayúsculas y comparando
	con los inputs también como mayúsculas, porque también es posible quebrar el programa
	si no ingreso un nombre EXACTAMENTE igual
	¿y con los ruts puede pasar? no, porque ya tengo el validador de rut y los clientes
	los identifico con rut. Entonces esta validación es crítica SOLO EN EL CASO DE LAS
	SUCURSALES
	- además, si quedo metido en un bucle while, no puedo salir con ctrl+c, el programa
	se puede mejorar dando la posibilidad de salir con algún comando. De hecho, cuando
	ejecuto con F5, el programa se puede interrumpir, pero si ejecuto directamente desde
	la consola, el programa no es posible interrumpirlo ya que no escribí esa funcionalidad
	✓ algo que mejorar, es que cuando se elimine una sucursal, también se eliminen sus
	asignaciones, si es que la sucursal está involucrada en una
	✓ otra cosa que mejorar, es que cuando se elimine un cliente, también se elimine
	su asignación
	✓ y si le vuelvo a asignar una sucursal a un cliente y repongo la sucursal eliminada,
	¿se repone la asignación? No debería. Toda sucursal eliminada pasa a tener asignación
	eliminada. Si la persona quiere reponer la asignación, debe hacerlo manualmente.

Pruebas:
	Clientes:
		✓ Crear un nuevo registro, equivocarse en crear un nuevo registro
		✓ Ver nuevo registro, equivocarse en pedir
		✓ Modificar registro, equivocarse en modificar
		✓ Buscar nuevo registro, equivocarse en buscar
		✓ Eliminar nuevo registro, equivocarse en eliminar
		✓ Pedir agregar cilente eliminado
		✓ Pedir modificar cilente eliminado
	Sucursales:
		✓ Crear nueva sucursal, equivocarse en crear un nuevo registro
		✓ Ver nueva sucursal, equivocarse en pedir
		✓ Buscar sucursal, equivocarse en buscar
		✓ Modificar nueva sucursal, equivocarse en modificar
		✓ Eliminar nueva sucursal, equivocarse en eliminar
		✓ Pedir agregar sucursal eliminada
		✓ Pedir modificar sucursal eliminada
	Asignaciones:
		✓ Crear nueva asginación, equivocarse en crear nueva asginación
		primero, ¿hay clientes para asignar? (len(todos los clientes) distinto de cero)
			si no, salir
		segundo, ¿el rut ingresado es correcto?
			si no, salir
		tercero, ¿el cliente ingresado existe? ¿el cliente coincide con un rut de la bbdd?
			si no, salir
		cuarto, el cliente coincide con un rut de la bbdd, ¿pero está habilitado? (est=1)
			si no, salir
		quinto, ¿hay sucursales para asignar?
			si no, salir
		sexto, ¿el nombre de la sucursal es válido para ir a buscarlo?
			si no, loop
		séptimo, ¿la sucursal ingresada existe?
			si no, salir
		octavo, ¿el cliente ya tiene una sucursal asignada?
			si es así, imprimir y salir
			si no, pedir datos para asignar
		✓ Ver asginaciones
		✓ Modificar asginación, equivocarse en modificar
		primero, ¿existen asignaciones para modificar?
			si no, salir
		segundo, ¿el rut ingresado es correcto?
			si no, salir
		tercero, ¿el cliente ingresado existe? ¿el cliente coincide con un rut de la bbdd?
			si no, salir
		cuarto, el cliente coincide con un rut de la bbdd, ¿pero está habilitado?
			si no, salir
		quinto, ¿el cliente tiene asignación?
			si no, salir
		sexto, ¿la asignación del cliente está habilitada?
			si no, ofrecer reponerla
		séptimo, si tiene asignación y está habilitada, ofrecer modificarla
		
		> validaciones de la nueva sucursal
		que sea una sucursal existente
		
		
		✓ Pedir agregar asginación eliminada
		✓ Pedir modificar asginación eliminada	
	JSON:
		- mejorar la impresión usando tabla
	Usuarios:
		✓ Crear nuevo usuario e iniciar sesión
		- Equivocarse al crear nuevo usuario
		- Ver usuarios
		- Buscar
		- Modificar
		- Eliminar
		
		