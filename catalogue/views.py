from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Categoria, Producto
from .forms import CategoriaForm, ProductoForm

# ==================== CRUD CATEGORÍA ====================

@login_required
def categoria_lista(request):
    """Vista para listar todas las categorías"""
    categorias = Categoria.objects.all().order_by('nombre')
    context = {'categorias': categorias}
    return render(request, 'templateCatalogue/categoria_lista.html', context)


@login_required
def categoria_crear(request):
    """Vista para crear una nueva categoría"""
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoría creada exitosamente.')
            return redirect('categoria_lista')
    else:
        form = CategoriaForm()
    
    context = {'form': form, 'accion': 'Crear'}
    return render(request, 'templateCatalogue/categoria_form.html', context)


@login_required
def categoria_editar(request, pk):
    """Vista para editar una categoría existente"""
    categoria = get_object_or_404(Categoria, pk=pk)
    
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoría actualizada exitosamente.')
            return redirect('categoria_lista')
    else:
        form = CategoriaForm(instance=categoria)
    
    context = {'form': form, 'accion': 'Editar', 'categoria': categoria}
    return render(request, 'templateCatalogue/categoria_form.html', context)


@login_required
def categoria_eliminar(request, pk):
    """Vista para eliminar una categoría"""
    categoria = get_object_or_404(Categoria, pk=pk)
    
    if request.method == 'POST':
        try:
            categoria.delete()
            messages.success(request, 'Categoría eliminada exitosamente.')
        except Exception as e:
            messages.error(request, f'No se puede eliminar. Hay productos asociados. Error: {str(e)}')
        return redirect('categoria_lista')
    
    context = {'categoria': categoria}
    return render(request, 'templateCatalogue/categoria_eliminar.html', context)


# ==================== CRUD PRODUCTO ====================

@login_required
def producto_lista(request):
    """Vista para listar todos los productos"""
    productos = Producto.objects.all().select_related('categoria_id').order_by('nombre')
    context = {'productos': productos}
    return render(request, 'templateCatalogue/producto_lista.html', context)


@login_required
def producto_detalle(request, pk):
    """Vista para ver el detalle de un producto"""
    producto = get_object_or_404(Producto, pk=pk)
    context = {'producto': producto}
    return render(request, 'templateCatalogue/producto_detalle.html', context)


@login_required
def producto_crear(request):
    """Vista para crear un nuevo producto"""
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto creado exitosamente.')
            return redirect('producto_lista')
    else:
        form = ProductoForm()
    
    context = {'form': form, 'accion': 'Crear'}
    return render(request, 'templateCatalogue/producto_form.html', context)


@login_required
def producto_editar(request, pk):
    """Vista para editar un producto existente"""
    producto = get_object_or_404(Producto, pk=pk)
    
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto actualizado exitosamente.')
            return redirect('producto_lista')
    else:
        form = ProductoForm(instance=producto)
    
    context = {'form': form, 'accion': 'Editar', 'producto': producto}
    return render(request, 'templateCatalogue/producto_form.html', context)


@login_required
def producto_eliminar(request, pk):
    """Vista para eliminar un producto"""
    producto = get_object_or_404(Producto, pk=pk)
    
    if request.method == 'POST':
        try:
            producto.delete()
            messages.success(request, 'Producto eliminado exitosamente.')
        except Exception as e:
            messages.error(request, f'No se puede eliminar. Error: {str(e)}')
        return redirect('producto_lista')
    
    context = {'producto': producto}
    return render(request, 'templateCatalogue/producto_eliminar.html', context)