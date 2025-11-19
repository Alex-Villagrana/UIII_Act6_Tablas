# TODO: Agregar Tablas Empleado y Venta

## Pasos a Completar:
- [ ] Editar models.py: Agregar modelo Empleado con campos básicos y relación ManyToMany con Cliente (empleados que atendieron).
- [ ] Editar models.py: Agregar modelo Venta con ForeignKey a Cliente y Empleado, ManyToMany a Producto, fecha_venta, total.
- [ ] Ejecutar makemigrations para generar migración.
- [ ] Ejecutar migrate para aplicar cambios a la base de datos.
- [ ] Editar admin.py: Registrar Empleado y Venta en el admin de Django.
- [ ] Leer views.py para entender la estructura existente.
- [ ] Editar views.py: Agregar vistas CRUD para Empleado (ver_empleados, agregar_empleado, actualizar_empleado, borrar_empleado).
- [ ] Editar views.py: Agregar vistas CRUD para Venta (ver_ventas, agregar_venta, actualizar_venta, borrar_venta).
- [ ] Editar urls.py: Agregar rutas para empleados y ventas.
- [ ] Crear directorio app_Skateshop/templates/empleado/.
- [ ] Crear templates HTML para empleados: ver_empleados.html, agregar_empleado.html, actualizar_empleado.html, borrar_empleado.html.
- [ ] Crear directorio app_Skateshop/templates/venta/.
- [ ] Crear templates HTML para ventas: ver_ventas.html, agregar_venta.html, actualizar_venta.html, borrar_venta.html.
- [ ] Verificar que todo funcione en el admin y con los templates.
