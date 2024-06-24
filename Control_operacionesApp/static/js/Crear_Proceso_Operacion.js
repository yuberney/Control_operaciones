
function ValorTotal(){
    try {
        var tdCantidadOperaciones = parseFloat(document.getElementById("tdCantidadOperaciones").value) || 0;
        var tdTotalProcesados = parseFloat(document.getElementById("txtOtrosPagos").value) || 0;
       
        document.getElementById("disponible").value = (tdCantidadOperaciones - tdTotalProcesados);

} catch (e) {

}
}


// Script para deshabilitar boton de disponibles
const inputDisabled = document.getElementById('disponible');
const inputNumber = document.getElementById('txtCantidad_Procesada');
const miBoton = document.getElementById('registrar');

inputNumber.addEventListener('input', () => {
    const numeroIngresado = parseFloat(inputNumber.value);
    const valorInputDisabled = parseFloat(inputDisabled.value);

    if (numeroIngresado <= valorInputDisabled) {
        miBoton.removeAttribute('hidden', 'true');
    } else {
        miBoton.setAttribute('hidden', 'true');
    }
});


