from django.db import models

# ==========================================
# MODELO: PROVEEDOR
# ==========================================
class Proveedor(models.Model):
    contacto_nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    direccion = models.TextField()
    pais = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)

    def __str__(self):
        return self.contacto_nombre

# ==========================================
# MODELO: PRODUCTO (Actualizado para usar Proveedor)
# ==========================================
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    # Relacionado con Proveedor (antes era Categoria)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, related_name="productos")
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50, blank=True, null=True)
    fecha_agregado = models.DateField(auto_now_add=True)
    disponible = models.BooleanField(default=True)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} - {self.marca}"

# ==========================================
# MODELO: CLIENTE
# ==========================================
class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    compra = models.ManyToManyField(Producto, blank=True, related_name="clientes")
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)
    fecha_registro = models.DateField(auto_now_add=True)
    activo = models.BooleanField(default=True)
    imagen = models.ImageField(upload_to='clientes/', blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} - {self.id_cliente}"

# ==========================================
# MODELO: EMPLEADO
# ==========================================
class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)
    fecha_contratacion = models.DateField(auto_now_add=True)
    activo = models.BooleanField(default=True)
    # Relación ManyToMany con Cliente para saber quién atendió
    clientes_atendidos = models.ManyToManyField(Cliente, blank=True, related_name="empleados_atendieron")

    def __str__(self):
        return self.nombre

# ==========================================
# MODELO: VENTA
# ==========================================
class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="ventas")
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, related_name="ventas_realizadas")
    productos = models.ManyToManyField(Producto, related_name="ventas")
    fecha_venta = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Venta {self.id} - {self.cliente.nombre} - {self.fecha_venta.strftime('%Y-%m-%d')}"
