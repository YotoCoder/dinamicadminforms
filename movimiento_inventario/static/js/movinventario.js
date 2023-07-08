

document.addEventListener('DOMContentLoaded', function () {
  if (window.location.href.endsWith("/change/")) {
    const main = document.getElementById('main')
    main.classList.remove('shifted')
  }
  var productosSelects = document.querySelectorAll('[id^="id_movimientoinventarioproducto_set-"][id$="-producto"]');

  productosSelects.forEach(function (productoSelect) {
    var inlinePrefix = productoSelect.id.split('-')[1];
    var lastValue = productoSelect.value;

    function handleInputChange() {
      var productoId = productoSelect.value;

      fetch('/obtener_detalles_producto/?producto_id=' + productoId)
        .then(function (response) {
          if (response.ok) {
            return response.json();
          } else {
            throw new Error('Error en la solicitud AJAX');
          }
        })
        .then(function (data) {
          document.getElementById('id_movimientoinventarioproducto_set-' + inlinePrefix + '-descripcion').value = data.descripcion;
          document.getElementById('id_movimientoinventarioproducto_set-' + inlinePrefix + '-umed').value = data.umed;
        })
        .catch(function (error) {
          document.getElementById('id_movimientoinventarioproducto_set-' + inlinePrefix + '-descripcion').value = '';
          document.getElementById('id_movimientoinventarioproducto_set-' + inlinePrefix + '-umed').value = '';
        });
    }

    productoSelect.addEventListener('input', function () {
      lastValue = productoSelect.value;
    });

    setInterval(() => {
      if (productoSelect.value !== lastValue) {
        lastValue = productoSelect.value;
        handleInputChange();
      }
    }, 500);

    productoSelect.addEventListener('input', function () {
      handleInputChange();
    });
  });
});
