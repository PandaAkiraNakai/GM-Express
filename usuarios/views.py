from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Usuario, TipoUsuario
from .forms import UsuarioForm, TipoUsuarioForm

# ==================== CRUD TIPO USUARIO ====================

@login_required
def tipo_usuario_lista(request):
    """Vista para listar todos los tipos de usuario"""
    tipos = TipoUsuario.objects.all().order_by('-fecha_creacion')
    context = {'tipos': tipos}
    return render(request, 'templateUsuarios/tipo_usuario_lista.html', context)


@login_required
def tipo_usuario_crear(request):
    """Vista para crear un nuevo tipo de usuario"""
    if request.method == 'POST':
        form = TipoUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tipo de usuario creado exitosamente.')
            return redirect('tipo_usuario_lista')
    else:
        form = TipoUsuarioForm()
    
    context = {'form': form, 'accion': 'Crear'}
    return render(request, 'templateUsuarios/tipo_usuario_form.html', context)


@login_required
def tipo_usuario_editar(request, pk):
    """Vista para editar un tipo de usuario existente"""
    tipo = get_object_or_404(TipoUsuario, pk=pk)
    
    if request.method == 'POST':
        form = TipoUsuarioForm(request.POST, instance=tipo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tipo de usuario actualizado exitosamente.')
            return redirect('tipo_usuario_lista')
    else:
        form = TipoUsuarioForm(instance=tipo)
    
    context = {'form': form, 'accion': 'Editar', 'tipo': tipo}
    return render(request, 'templateUsuarios/tipo_usuario_form.html', context)


@login_required
def tipo_usuario_eliminar(request, pk):
    """Vista para eliminar un tipo de usuario"""
    tipo = get_object_or_404(TipoUsuario, pk=pk)
    
    if request.method == 'POST':
        try:
            tipo.delete()
            messages.success(request, 'Tipo de usuario eliminado exitosamente.')
        except Exception as e:
            messages.error(request, f'No se puede eliminar. Error: {str(e)}')
        return redirect('tipo_usuario_lista')
    
    context = {'tipo': tipo}
    return render(request, 'templateUsuarios/tipo_usuario_eliminar.html', context)


# ==================== CRUD USUARIO ====================

@login_required
def usuario_lista(request):
    """Vista para listar todos los usuarios"""
    usuarios = Usuario.objects.all().order_by('-fecha_registro')
    context = {'usuarios': usuarios}
    return render(request, 'templateUsuarios/usuario_lista.html', context)


@login_required
def usuario_detalle(request, pk):
    """Vista para ver el detalle de un usuario"""
    usuario = get_object_or_404(Usuario, pk=pk)
    context = {'usuario': usuario}
    return render(request, 'templateUsuarios/usuario_detalle.html', context)


@login_required
def usuario_crear(request):
    """Vista para crear un nuevo usuario"""
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario creado exitosamente.')
            return redirect('usuario_lista')
    else:
        form = UsuarioForm()
    
    context = {'form': form, 'accion': 'Crear'}
    return render(request, 'templateUsuarios/usuario_form.html', context)


@login_required
def usuario_editar(request, pk):
    """Vista para editar un usuario existente"""
    usuario = get_object_or_404(Usuario, pk=pk)
    
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario actualizado exitosamente.')
            return redirect('usuario_lista')
    else:
        form = UsuarioForm(instance=usuario)
    
    context = {'form': form, 'accion': 'Editar', 'usuario': usuario}
    return render(request, 'templateUsuarios/usuario_form.html', context)


@login_required
def usuario_eliminar(request, pk):
    """Vista para eliminar un usuario"""
    usuario = get_object_or_404(Usuario, pk=pk)
    
    if request.method == 'POST':
        try:
            usuario.delete()
            messages.success(request, 'Usuario eliminado exitosamente.')
        except Exception as e:
            messages.error(request, f'No se puede eliminar. Error: {str(e)}')
        return redirect('usuario_lista')
    
    context = {'usuario': usuario}
    return render(request, 'templateUsuarios/usuario_eliminar.html', context)