# Contenido de app_Skateshop/views.py
from django.shortcuts import render, redirect, get_object_or_404
from decimal import Decimal
from .models import Cliente, Producto, Proveedor, Empleado, Venta # Importamos los modelos

# 1. Función de Inicio
def inicio_skateshop(request):
    return render(request, 'inicio.html')

# 2. CRUD: Agregar Cliente
def agregar_cliente(request):
    if request.method == 'POST':
        # No validar entrada de datos:
        cliente = Cliente(
            nombre=request.POST.get('nombre'),
            email=request.POST.get('email'),
            telefono=request.POST.get('telefono'),
            direccion=request.POST.get('direccion'),
            activo=request.POST.get('activo', False) == 'on'
        )
        if 'imagen' in request.FILES:
            cliente.imagen = request.FILES['imagen']
        cliente.save()
        # Asignar productos comprados
        productos_ids = request.POST.getlist('compra')
        if productos_ids:
            productos = Producto.objects.filter(id__in=productos_ids)
            cliente.compra.set(productos)
        return redirect('ver_clientes')
    productos = Producto.objects.all()
    context = {'productos': productos}
    return render(request, 'cliente/agregar_cliente.html', context)

# 3. CRUD: Ver Clientes (Listado)
def ver_clientes(request):
    clientes = Cliente.objects.all().order_by('nombre')
    context = {'clientes': clientes}
    return render(request, 'cliente/ver_clientes.html', context)

# 4. CRUD: Actualizar Cliente (Mostrar Formulario)
def actualizar_cliente(request, pk):
    cliente_a_actualizar = get_object_or_404(Cliente, pk=pk)
    productos = Producto.objects.all()
    context = {'cliente': cliente_a_actualizar, 'productos': productos}
    return render(request, 'cliente/actualizar_cliente.html', context)

# 5. CRUD: Actualizar Cliente (Procesar POST)
def realizar_actualizacion_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.nombre = request.POST.get('nombre')
        cliente.email = request.POST.get('email')
        cliente.telefono = request.POST.get('telefono')
        cliente.direccion = request.POST.get('direccion')
        cliente.activo = request.POST.get('activo', False) == 'on'
        if 'imagen' in request.FILES:
            cliente.imagen = request.FILES['imagen']
        cliente.save()
        # Actualizar productos comprados
        productos_ids = request.POST.getlist('compra')
        productos = Producto.objects.filter(id__in=productos_ids)
        cliente.compra.set(productos)
        return redirect('ver_clientes')
    return redirect('actualizar_cliente', pk=pk)

# 6. CRUD: Borrar Cliente
def borrar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('ver_clientes')
    context = {'cliente': cliente}
    return render(request, 'cliente/borrar_cliente.html', context)

# 7. CRUD: Agregar Proveedor
def agregar_proveedor(request):
    if request.method == 'POST':
        proveedor = Proveedor(
            contacto_nombre=request.POST.get('contacto_nombre'),
            telefono=request.POST.get('telefono'),
            email=request.POST.get('email'),
            direccion=request.POST.get('direccion'),
            pais=request.POST.get('pais'),
            estado=request.POST.get('estado'),
            ciudad=request.POST.get('ciudad')
        )
        proveedor.save()
        return redirect('ver_proveedores')
    return render(request, 'proveedor/agregar_proveedor.html')

# 8. CRUD: Ver Proveedores (Listado)
def ver_proveedores(request):
    proveedores = Proveedor.objects.all().order_by('contacto_nombre')
    context = {'proveedores': proveedores}
    return render(request, 'proveedor/ver_proveedores.html', context)

# 9. CRUD: Actualizar Proveedor (Mostrar Formulario)
def actualizar_proveedor(request, pk):
    proveedor_a_actualizar = get_object_or_404(Proveedor, pk=pk)
    context = {'proveedor': proveedor_a_actualizar}
    return render(request, 'proveedor/actualizar_proveedor.html', context)

# 10. CRUD: Actualizar Proveedor (Procesar POST)
def realizar_actualizacion_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        proveedor.contacto_nombre = request.POST.get('contacto_nombre')
        proveedor.telefono = request.POST.get('telefono')
        proveedor.email = request.POST.get('email')
        proveedor.direccion = request.POST.get('direccion')
        proveedor.pais = request.POST.get('pais')
        proveedor.estado = request.POST.get('estado')
        proveedor.ciudad = request.POST.get('ciudad')
        proveedor.save()
        return redirect('ver_proveedores')
    return redirect('actualizar_proveedor', pk=pk)

# 11. CRUD: Borrar Proveedor
def borrar_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        proveedor.delete()
        return redirect('ver_proveedores')
    context = {'proveedor': proveedor}
    return render(request, 'proveedor/borrar_proveedor.html', context)

# 12. CRUD: Agregar Producto
def agregar_producto(request):
    if request.method == 'POST':
        producto = Producto(
            nombre=request.POST.get('nombre'),
            descripcion=request.POST.get('descripcion'),
            precio=request.POST.get('precio'),
            stock=request.POST.get('stock'),
            proveedor_id=request.POST.get('proveedor'),
            marca=request.POST.get('marca'),
            modelo=request.POST.get('modelo'),
            disponible=request.POST.get('disponible', False) == 'on'
        )
        if 'imagen' in request.FILES:
            producto.imagen = request.FILES['imagen']
        producto.save()
        return redirect('ver_productos')
    proveedores = Proveedor.objects.all()
    context = {'proveedores': proveedores}
    return render(request, 'producto/agregar_producto.html', context)

# 13. CRUD: Ver Productos (Listado)
def ver_productos(request):
    productos = Producto.objects.all().order_by('nombre')
    context = {'productos': productos}
    return render(request, 'producto/ver_productos.html', context)

# 14. CRUD: Actualizar Producto (Mostrar Formulario)
def actualizar_producto(request, pk):
    producto_a_actualizar = get_object_or_404(Producto, pk=pk)
    proveedores = Proveedor.objects.all()
    context = {'producto': producto_a_actualizar, 'proveedores': proveedores}
    return render(request, 'producto/actualizar_producto.html', context)

# 15. CRUD: Actualizar Producto (Procesar POST)
def realizar_actualizacion_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.nombre = request.POST.get('nombre')
        producto.descripcion = request.POST.get('descripcion')
        producto.precio = request.POST.get('precio')
        producto.stock = request.POST.get('stock')
        producto.proveedor_id = request.POST.get('proveedor')
        producto.marca = request.POST.get('marca')
        producto.modelo = request.POST.get('modelo')
        producto.disponible = request.POST.get('disponible', False) == 'on'
        if 'imagen' in request.FILES:
            producto.imagen = request.FILES['imagen']
        producto.save()
        return redirect('ver_productos')
    return redirect('actualizar_producto', pk=pk)

# 16. CRUD: Borrar Producto
def borrar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('ver_productos')
    context = {'producto': producto}
    return render(request, 'producto/borrar_producto.html', context)

# 17. CRUD: Agregar Empleado
def agregar_empleado(request):
    if request.method == 'POST':
        empleado = Empleado(
            nombre=request.POST.get('nombre'),
            email=request.POST.get('email'),
            telefono=request.POST.get('telefono'),
            direccion=request.POST.get('direccion'),
            activo=request.POST.get('activo', False) == 'on'
        )
        empleado.save()
        # Asignar clientes atendidos
        clientes_ids = request.POST.getlist('clientes_atendidos')
        if clientes_ids:
            clientes = Cliente.objects.filter(id_cliente__in=clientes_ids)
            empleado.clientes_atendidos.set(clientes)
        return redirect('ver_empleados')
    clientes = Cliente.objects.all()
    context = {'clientes': clientes}
    return render(request, 'empleado/agregar_empleado.html', context)

# 18. CRUD: Ver Empleados (Listado)
def ver_empleados(request):
    empleados = Empleado.objects.all().order_by('nombre')
    context = {'empleados': empleados}
    return render(request, 'empleado/ver_empleados.html', context)

# 19. CRUD: Actualizar Empleado (Mostrar Formulario)
def actualizar_empleado(request, pk):
    empleado_a_actualizar = get_object_or_404(Empleado, pk=pk)
    clientes = Cliente.objects.all()
    context = {'empleado': empleado_a_actualizar, 'clientes': clientes}
    return render(request, 'empleado/actualizar_empleado.html', context)

# 20. CRUD: Actualizar Empleado (Procesar POST)
def realizar_actualizacion_empleado(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    if request.method == 'POST':
        empleado.nombre = request.POST.get('nombre')
        empleado.email = request.POST.get('email')
        empleado.telefono = request.POST.get('telefono')
        empleado.direccion = request.POST.get('direccion')
        empleado.activo = request.POST.get('activo', False) == 'on'
        empleado.save()
        # Actualizar clientes atendidos
        clientes_ids = request.POST.getlist('clientes_atendidos')
        clientes = Cliente.objects.filter(id_cliente__in=clientes_ids)
        empleado.clientes_atendidos.set(clientes)
        return redirect('ver_empleados')
    return redirect('actualizar_empleado', pk=pk)

# 21. CRUD: Borrar Empleado
def borrar_empleado(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    if request.method == 'POST':
        empleado.delete()
        return redirect('ver_empleados')
    context = {'empleado': empleado}
    return render(request, 'empleado/borrar_empleado.html', context)

# 22. CRUD: Agregar Venta
def agregar_venta(request):
    if request.method == 'POST':
        cliente_id = request.POST.get('cliente')
        empleado_id = request.POST.get('empleado')
        total_str = request.POST.get('total')
        if not cliente_id or not empleado_id or not total_str:
            # Manejar error: campos requeridos faltantes
            context = {'error': 'Todos los campos son requeridos.'}
            clientes = Cliente.objects.all()
            empleados = Empleado.objects.all()
            productos = Producto.objects.all()
            context.update({'clientes': clientes, 'empleados': empleados, 'productos': productos})
            return render(request, 'venta/agregar_venta.html', context)
        cliente = get_object_or_404(Cliente, pk=cliente_id)
        empleado = get_object_or_404(Empleado, pk=empleado_id)
        total = Decimal(total_str)
        venta = Venta(
            cliente=cliente,
            empleado=empleado,
            total=total
        )
        venta.save()
        # Asignar productos vendidos
        productos_ids = request.POST.getlist('productos')
        if productos_ids:
            productos = Producto.objects.filter(id__in=productos_ids)
            venta.productos.set(productos)
        return redirect('ver_ventas')
    clientes = Cliente.objects.all()
    empleados = Empleado.objects.all()
    productos = Producto.objects.all()
    context = {'clientes': clientes, 'empleados': empleados, 'productos': productos}
    return render(request, 'venta/agregar_venta.html', context)

# 23. CRUD: Ver Ventas (Listado)
def ver_ventas(request):
    ventas = Venta.objects.all().order_by('-fecha_venta')
    context = {'ventas': ventas}
    return render(request, 'venta/ver_ventas.html', context)

# 24. CRUD: Actualizar Venta (Mostrar Formulario)
def actualizar_venta(request, pk):
    venta_a_actualizar = get_object_or_404(Venta, pk=pk)
    clientes = Cliente.objects.all()
    empleados = Empleado.objects.all()
    productos = Producto.objects.all()
    context = {'venta': venta_a_actualizar, 'clientes': clientes, 'empleados': empleados, 'productos': productos}
    return render(request, 'venta/actualizar_venta.html', context)

# 25. CRUD: Actualizar Venta (Procesar POST)
def realizar_actualizacion_venta(request, pk):
    venta = get_object_or_404(Venta, pk=pk)
    if request.method == 'POST':
        cliente_id = request.POST.get('cliente')
        empleado_id = request.POST.get('empleado')
        total_str = request.POST.get('total')
        if not cliente_id or not empleado_id or not total_str:
            # Manejar error: campos requeridos faltantes
            context = {'error': 'Todos los campos son requeridos.'}
            clientes = Cliente.objects.all()
            empleados = Empleado.objects.all()
            productos = Producto.objects.all()
            context.update({'venta': venta, 'clientes': clientes, 'empleados': empleados, 'productos': productos})
            return render(request, 'venta/actualizar_venta.html', context)
        venta.cliente = get_object_or_404(Cliente, id_cliente=cliente_id)
        venta.empleado = get_object_or_404(Empleado, pk=empleado_id)
        venta.total = Decimal(total_str)
        venta.save()
        # Actualizar productos vendidos
        productos_ids = request.POST.getlist('productos')
        productos = Producto.objects.filter(id__in=productos_ids)
        venta.productos.set(productos)
        return redirect('ver_ventas')
    return redirect('actualizar_venta', pk=pk)

# 26. CRUD: Borrar Venta
def borrar_venta(request, pk):
    venta = get_object_or_404(Venta, pk=pk)
    if request.method == 'POST':
        venta.delete()
        return redirect('ver_ventas')
    context = {'venta': venta}
    return render(request, 'venta/borrar_venta.html', context)

# 27. Ver Productos por Cliente (desde Ventas)
def productos_por_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id_cliente=cliente_id)
    ventas = Venta.objects.filter(cliente=cliente)
    productos = Producto.objects.filter(ventas__in=ventas).distinct()
    context = {'cliente': cliente, 'productos': productos}
    return render(request, 'venta/productos_por_cliente.html', context)
