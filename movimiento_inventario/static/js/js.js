document.addEventListener('DOMContentLoaded', function () {
    // Obtener todos los campos de selección de productos en el inline
    var productosSelects = document.querySelectorAll('[id^="id_movimientoinventarioproducto_set-"][id$="-producto"]')
  
    // Manejar el evento de cambio en la selección de productos para cada campo
    productosSelects.forEach(function (productoSelect) {
      var inlinePrefix = productoSelect.id.split('-')[1];
  
      Object.defineProperty(productoSelect, 'value', {
        get() {
          return productoSelect.__lastValue;
        },
        set(nuevoValor) {
          productoSelect.__lastValue = nuevoValor;
          productoSelect.setAttribute("value", nuevoValor);
          console.log('Nuevo valor:', nuevoValor);
          // Obtener el ID del producto seleccionado
          var productoId = productoSelect.value;
  
          // Realizar una petición AJAX para obtener los detalles del producto
          fetch('/obtener_detalles_producto/?producto_id=' + productoId)
            .then(function (response) {
              if (response.ok) {
                return response.json();
              } else {
                throw new Error('Error en la solicitud AJAX');
              }
            })
            .then(function (data) {
              // Actualizar los campos del inline con los detalles del producto
              document.getElementById('id_movimientoinventarioproducto_set-' + inlinePrefix + '-descripcion').value = data.descripcion;
              document.getElementById('id_movimientoinventarioproducto_set-' + inlinePrefix + '-umed').value = data.umed;
            })
            .catch(function (error) {
              document.getElementById('id_movimientoinventarioproducto_set-' + inlinePrefix + '-descripcion').value = '';
              document.getElementById('id_movimientoinventarioproducto_set-' + inlinePrefix + '-umed').value = '';
            });
        }
      });
  
      // Agregar event listener al evento de entrada de texto
      productoSelect.addEventListener('input', function (e) {
        productoSelect.value = e.data;
      });
    });
  });