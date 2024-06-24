
 // obtenemos todas las filas del tbody
 var filas=document.querySelectorAll("#OperacionesDisponibles tbody tr");
 var total=0;

 // recorremos cada una de las filas
 filas.forEach(function(e) {

     // obtenemos las columnas de cada fila
     var columnas=e.querySelectorAll("td");

     // obtenemos los valores de la cantidad y importe
     var CantidadRegistrada=parseFloat(columnas[5].textContent);
     var tdTotal_Procesados=parseFloat(columnas[6].textContent);

     // mostramos el total por fila
     columnas[7].textContent=(CantidadRegistrada - tdTotal_Procesados);
     total+=CantidadRegistrada-tdTotal_Procesados;
 });
 // mostramos la suma total
 var filas=document.querySelectorAll("#OperacionesDisponibles tfoot tr td");
 filas[1].textContent=total;         