from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Venta, DetalleVenta
from .forms import VentaForm, DetalleVentaForm

# ==================== CRUD VENTA ====================

@login_required
def venta_lista(request):
    """Vista para listar todas las ventas"""
    ventas = Venta.objects.all().select_related('usuario').order_by('-fecha_venta')
    context = {'ventas': ventas}
    return render(request, 'templateVentas/venta_lista.html', context)


@login_required
def venta_detalle(request, pk):
    """Vista para ver el detalle de una venta con sus productos"""
    venta = get_object_or_404(Venta, pk=pk)
    detalles = DetalleVenta.objects.filter(venta=venta).select_related('producto')
    context = {
        'venta': venta,
        'detalles': detalles
    }
    return render(request, 'templateVentas/venta_detalle.html', context)


@login_required
def venta_crear(request):
    """Vista para crear una nueva venta"""
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            venta = form.save()
            messages.success(request, f'Venta #{venta.id} creada exitosamente.')
            return redirect('venta_detalle', pk=venta.pk)
    else:
        form = VentaForm()
    
    context = {'form': form, 'accion': 'Crear'}
    return render(request, 'templateVentas/venta_form.html', context)


@login_required
def venta_editar(request, pk):
    """Vista para editar una venta existente"""
    venta = get_object_or_404(Venta, pk=pk)
    
    if request.method == 'POST':
        form = VentaForm(request.POST, instance=venta)
        if form.is_valid():
            form.save()
            messages.success(request, 'Venta actualizada exitosamente.')
            return redirect('venta_detalle', pk=venta.pk)
    else:
        form = VentaForm(instance=venta)
    
    context = {'form': form, 'accion': 'Editar', 'venta': venta}
    return render(request, 'templateVentas/venta_form.html', context)


@login_required
def venta_eliminar(request, pk):
    """Vista para eliminar una venta"""
    venta = get_object_or_404(Venta, pk=pk)
    
    if request.method == 'POST':
        try:
            venta.delete()
            messages.success(request, 'Venta eliminada exitosamente.')
        except Exception as e:
            messages.error(request, f'No se puede eliminar. Error: {str(e)}')
        return redirect('venta_lista')
    
    context = {'venta': venta}
    return render(request, 'templateVentas/venta_eliminar.html', context)


# ==================== CRUD DETALLE VENTA ====================

@login_required
def detalle_crear(request, venta_id):
    """Vista para agregar productos a una venta"""
    venta = get_object_or_404(Venta, pk=venta_id)
    
    if request.method == 'POST':
        form = DetalleVentaForm(request.POST)
        if form.is_valid():
            detalle = form.save(commit=False)
            detalle.venta = venta
            
            # Actualizar stock del producto
            producto = detalle.producto
            if producto.stock >= detalle.cantidad:
                producto.stock -= detalle.cantidad
                producto.save()
                detalle.save()
                messages.success(request, 'Producto agregado a la venta.')
            else:
                messages.error(request, 'Stock insuficiente.')
            
            return redirect('venta_detalle', pk=venta.pk)
    else:
        form = DetalleVentaForm(initial={'venta': venta})
    
    context = {'form': form, 'venta': venta, 'accion': 'Agregar Producto'}
    return render(request, 'templateVentas/detalle_form.html', context)


@login_required
def detalle_eliminar(request, pk):
    """Vista para eliminar un producto de una venta"""
    detalle = get_object_or_404(DetalleVenta, pk=pk)
    venta_id = detalle.venta.id
    
    if request.method == 'POST':
        try:
            # Restaurar stock
            producto = detalle.producto
            producto.stock += detalle.cantidad
            producto.save()
            
            detalle.delete()
            messages.success(request, 'Producto eliminado de la venta.')
        except Exception as e:
            messages.error(request, f'Error: {str(e)}')
        return redirect('venta_detalle', pk=venta_id)
    
    context = {'detalle': detalle}
    return render(request, 'templateVentas/detalle_eliminar.html', context)