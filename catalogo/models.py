from django.db import models


catalogoprincipal = {
    1: {'nombre': 'Alimentación ejecutiva a domicilio', 'imagen': 'transporte.png', 'servicio_tipo': 'transportado'},
    2: {'nombre': 'Menú presencial gourmet', 'imagen': 'presencial.png', 'servicio_tipo': 'tradicional'},
    3: {'nombre': 'Servicios Empresariales', 'imagen': 'servicio.png', 'servicio_tipo': 'concesion'},
    4: {'nombre': 'Jornadas corporativas y brunch', 'imagen': 'JORNADAS.png', 'servicio_tipo': 'coffee'},
    5: {'nombre': 'Box lunch y pastelería fina', 'imagen': 'snack.png', 'servicio_tipo': 'reposteria'},
}

catalogo_transporte = {
    1: {'nombre': 'Wrap de salmón ahumado', 'imagen': 'wrap de salmon.png'},
    2: {'nombre': 'Ensalada mediterránea', 'imagen': 'ensalada mediterranea.png'},
    3: {'nombre': 'Tarta de esapinaca y ricotta', 'imagen': 'tarta1.png'},
    4: {'nombre': 'Pollo teriyaki con arroz', 'imagen': 'teriyaki.png'},
    5: {'nombre': 'Couscous con vegetales asados', 'imagen': 'couscous vegetal.png'},
}

catalogo_eventos = {
    1: {'nombre': 'Canapés de camarón', 'imagen': 'canapes de camaron.png'},
    2: {'nombre': 'Mini quiches de champiñón', 'imagen': 'quiches.png'},
    3: {'nombre': 'Brochetas caprese', 'imagen': 'Brochetas caprese.png'},
    4: {'nombre': 'Tartaleta de limón', 'imagen': 'Tartaleta de limón.png'},
    5: {'nombre': 'Trufas de chocolate', 'imagen': 'Trufas de chocolate.png'},
}

catalogo_presencial = {
    1: {'nombre': 'Risotto de champiñones', 'imagen': 'Risotto de champiñones.png'},
    2: {'nombre': 'Pasta al pesto', 'imagen': 'Pasta al pesto.png'},
    3: {'nombre': 'Omelette de espárragos', 'imagen': 'Omelette de espárragos.png'},
    4: {'nombre': 'Sopa de tomate y albahaca', 'imagen': 'Sopa de tomate y albahaca.png'},
    5: {'nombre': 'Tortilla española', 'imagen': 'Tortilla española.png'},
}

catalogo_snacks = {
    1: {'nombre': 'Barritas de avena y miel', 'imagen': 'Barritas de avena y miel.png'},
    2: {'nombre': 'Chips de manzana', 'imagen': 'Chips de manzana.png'},
    3: {'nombre': 'Mix de frutos secos', 'imagen': 'Mix de frutos secos.png'},
    4: {'nombre': 'Galletas de zanahoria', 'imagen': 'Galletas de zanahoria.png'},
    5: {'nombre': 'Brownies de batata', 'imagen': 'Brownies de batata.png'},
}

catalogo_servicios = {
    1: {'nombre': 'Equipo de sanitización avanzada', 'imagen': 'Equipo de sanitización avanzada.png'},
    2: {'nombre': 'Chef internacional', 'imagen': 'Chef internacional.png'},
    3: {'nombre': 'Montaje express', 'imagen': 'Montaje express.png'},
    4: {'nombre': 'Asesores de eventos', 'imagen': 'Asesores de eventos.png'},
    5: {'nombre': 'Técnicos multimedia', 'imagen': 'Técnicos multimedia.png'},
}

menu_transporte = {
    1: {'nombre':'Wrap de salmón ahumado',
        'descripcion':'Wrap fresco con salmón ahumado, queso crema y rúcula.',
        'ingredientes':'Tortilla integral, salmón ahumado, queso crema, rúcula, pepino','tiempo_entrega':'15 - 25 Minutos','condiciones_consumo':'Mantener refrigerado, consumir frío.','imagen':'pollo a la chilena.png'},
    2: {'nombre':'Ensalada mediterránea',
        'descripcion':'Ensalada con ingredientes típicos del mediterráneo.',
        'ingredientes':'Tomate cherry, aceitunas, queso feta, pepino, orégano','tiempo_entrega':'10 - 20 Minutos','condiciones_consumo':'Consumir fría, mantener refrigerada.','imagen':'lasagna de verduras.png'},
    3: {'nombre':'Tarta de espinaca y ricotta',
        'descripcion':'Tarta salada con masa artesanal y relleno cremoso.',
        'ingredientes':'Espinaca, ricotta, masa quebrada, huevo, nuez moscada','tiempo_entrega':'25 - 35 Minutos','condiciones_consumo':'Consumir tibio o frío.','imagen':'bowl de quinoa.png'},
    4: {'nombre':'Pollo teriyaki con arroz',
        'descripcion':'Pollo salteado en salsa teriyaki acompañado de arroz blanco.',
        'ingredientes':'Pechuga de pollo, salsa teriyaki, arroz, cebollín','tiempo_entrega':'20 - 30 Minutos','condiciones_consumo':'Consumir caliente, mantener tapado.','imagen':'filete de pescado.png'},
    5: {'nombre':'Couscous con vegetales asados',
        'descripcion':'Couscous suave con variedad de vegetales asados.',
        'ingredientes':'Couscous, berenjena, zapallo italiano, pimentón, zanahoria','tiempo_entrega':'20 - 30 Minutos','condiciones_consumo':'Consumir caliente o a temperatura ambiente.','imagen':'pastel de choclo.png'}
}

menu_eventos = {
    1: {'nombre':'Canapés de camarón',
        'descripcion':'Bocados fríos con camarón y salsa tártara.',
        'ingredientes':'Pan de molde, camarón, mayonesa, limón, eneldo','tiempo_entrega':'10 - 20 Minutos','condiciones_consumo':'Mantener refrigerado, consumir frío.'},
    2: {'nombre':'Mini quiches de champiñón',
        'descripcion':'Pequeñas tartaletas saladas rellenas de champiñón y queso.','ingredientes':'Champiñón, queso, masa quebrada, huevo, crema','tiempo_entrega':'15 - 25 Minutos','condiciones_consumo':'Consumir tibio o frío.'},
    3: {'nombre':'Brochetas caprese',
        'descripcion':'Brochetas frescas de tomate cherry, mozzarella y albahaca.','ingredientes':'Tomate cherry, mozzarella, albahaca, aceite de oliva','tiempo_entrega':'10 - 15 Minutos','condiciones_consumo':'Consumir frío, mantener refrigerado.'},
    4: {'nombre':'Tartaleta de limón',
        'descripcion':'Postre individual con base de masa y crema de limón.','ingredientes':'Masa quebrada, limón, leche condensada, merengue','tiempo_entrega':'20 - 30 Minutos','condiciones_consumo':'Mantener refrigerado, consumir en 2 días.'},
    5: {'nombre':'Trufas de chocolate',
        'descripcion':'Dulces de chocolate y frutos secos, ideales para coffee break.','ingredientes':'Chocolate, nuez, galleta, cacao, leche condensada','tiempo_entrega':'15 - 20 Minutos','condiciones_consumo':'Mantener en frío, consumir en 3 días.'}
}

menu_snacks = {
    1: {'nombre':'Barritas de avena y miel',
        'descripcion':'Barritas energéticas caseras con avena y miel.',
        'ingredientes':'Avena, miel, frutos secos, semillas de chía','tiempo_entrega':'20 - 30 Minutos','condiciones_consumo':'Mantener en envase hermético, consumir en 5 días.'},
    2: {'nombre':'Chips de manzana',
        'descripcion':'Láminas de manzana deshidratada, crocantes y dulces.','ingredientes':'Manzana, canela, azúcar','tiempo_entrega':'40 - 50 Minutos','condiciones_consumo':'Mantener en envase cerrado, consumir en 7 días.'},
    3: {'nombre':'Mix de frutos secos',
        'descripcion':'Mezcla de nueces, almendras, pasas y semillas.','ingredientes':'Nueces, almendras, pasas, semillas de girasol','tiempo_entrega':'5 Minutos','condiciones_consumo':'Mantener en lugar fresco y seco.'},
    4: {'nombre':'Galletas de zanahoria',
        'descripcion':'Galletas suaves y saludables con zanahoria rallada.','ingredientes':'Zanahoria, harina integral, azúcar rubia, huevo','tiempo_entrega':'25 - 35 Minutos','condiciones_consumo':'Mantener en envase hermético, consumir en 3 días.'},
    5: {'nombre':'Brownies de batata',
        'descripcion':'Brownies húmedos y dulces hechos con batata.','ingredientes':'Batata, cacao, azúcar, huevo, harina','tiempo_entrega':'30 - 40 Minutos','condiciones_consumo':'Mantener cerrado, consumir en 2 días.'}
}

menu_presencial = {
    1: {'nombre':'Risotto de champiñones',
        'descripcion':'Arroz cremoso con champiñones y queso parmesano.',
        'ingredientes':'Arroz arborio, champiñones, parmesano, vino blanco','tiempo_entrega':'30 - 40 Minutos','condiciones_consumo':'Consumir caliente, mantener tapado.'},
    2: {'nombre':'Pasta al pesto',
        'descripcion':'Pasta italiana con salsa pesto de albahaca fresca.','ingredientes':'Pasta, albahaca, piñones, ajo, aceite de oliva','tiempo_entrega':'20 - 30 Minutos','condiciones_consumo':'Consumir caliente, no recalentar más de una vez.'},
    3: {'nombre':'Omelette de espárragos',
        'descripcion':'Omelette esponjoso relleno de espárragos y queso.','ingredientes':'Huevos, espárragos, queso, cebollín','tiempo_entrega':'15 - 20 Minutos','condiciones_consumo':'Consumir caliente, servir recién hecho.'},
    4: {'nombre':'Sopa de tomate y albahaca',
        'descripcion':'Sopa cremosa de tomate con toque de albahaca fresca.','ingredientes':'Tomate, albahaca, crema, pan tostado','tiempo_entrega':'25 - 35 Minutos','condiciones_consumo':'Consumir caliente, mantener en envase térmico.'},
    5: {'nombre':'Tortilla española',
        'descripcion':'Clásica tortilla de papas y cebolla al estilo español.','ingredientes':'Papas, cebolla, huevo, aceite de oliva','tiempo_entrega':'30 - 40 Minutos','condiciones_consumo':'Consumir caliente o a temperatura ambiente.'}
}

menu_servicios = {
    1: {'nombre':'Equipo de sanitización avanzada',
        'descripcion':'Especialistas en limpieza profunda y desinfección de espacios.','componentes':'Máquinas de vapor, desinfectantes hospitalarios, EPP, paños especiales'},
    2: {'nombre':'Chef internacional',
        'descripcion':'Cocineros con experiencia en gastronomía internacional.','componentes':'Utensilios gourmet, recetarios internacionales, ingredientes premium'},
    3: {'nombre':'Montaje express',
        'descripcion':'Equipo rápido para montaje y desmontaje de eventos.','componentes':'Estructuras modulares, herramientas eléctricas, señalética'},
    4: {'nombre':'Asesores de eventos',
        'descripcion':'Expertos en planificación y coordinación de eventos.','componentes':'Software de gestión, agendas digitales, teléfonos, tablets'},
    5: {'nombre':'Técnicos multimedia',
        'descripcion':'Soporte para audio, video e iluminación en eventos.','componentes':'Micrófonos, parlantes, proyectores, consolas de luces'}
}