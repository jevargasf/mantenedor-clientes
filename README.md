Próximos pasos:

- Dejar funcional la P2
	- Formatear datos en interfaz con beautifultable

- Editar y eliminar registros
	- eliminar sucursal (deshabilitar)

- Menú login: 
	- Estructura menús:
		- Menu administrador
			- Gestión cliente
			- Gestión sucursal
			- Recuperar JSON
			- Cerrar sesión
		- Menu comercial
			- Gestión asignaciones
			- Cerrar sesión
	- Encriptación de contraseña -> modificar modelo de bbdd
	- Enmascarar contraseña en interfaz de usuario: usar maskpass para usar asteriscos.
admin 'inacap123'
comercial 'inacap321'


- Exportar datos JSON (menú API)
	- link: https://elprofemiguel.com/APIS_JSON/requisitos_formacion_api.json

id': 1, 
'titulo': 'Vendedor/a de Tienda', 
'detalles': 
    {'tipo': 'Puesto Comercial', 
     'empresa': 'Comercial XYZ', 
     'ubicacion': 'Santiago', 
    'requisitos': ['Título de educación media o equivalente', 'Experiencia previa en ventas', 'Habilidades de comunicación'],
    'descripcion': 'Atender a clientes y promover productos en la tienda.', 
    'formacion_adicional': ['Capacitación en atención al cliente', 'Conocimiento de productos']}
}