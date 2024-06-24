//FUbcion para calcular valor total a pagar

function ValorTotal(){
    try {
        var valorProcesos = parseFloat(document.getElementById("txtValorProcesos").value) || 0;
        var otrosPagos = parseFloat(document.getElementById("txtOtrosPagos").value) || 0;
        var descuentos = parseFloat(document.getElementById("txtDescuentos").value) || 0;

        document.getElementById("txtValorPagar").value = (valorProcesos + otrosPagos) - descuentos;

} catch (e) {

}
}