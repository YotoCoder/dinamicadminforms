from django.http import JsonResponse
from .models import Producto

def obtener_detalles_producto(request):
    if request.method == 'GET':
        producto_id = request.GET.get('producto_id')
        try:
            producto = Producto.objects.get(id=producto_id)
            data = {
                'descripcion': producto.descripcion,
                'umed': producto.umed
            }
            return JsonResponse(data)
        except Producto.DoesNotExist:
            return JsonResponse({'error': 'Producto no encontrado'}, status=404)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)