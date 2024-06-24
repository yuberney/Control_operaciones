/**
 Script para buscador 
*/

$(document).ready(function(){
  $("#buscar").on("keyup", function() {
    var value = $(this).val().toLowerCase();
    $("#usuarios tr").filter(function() {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    });
  });
});



/**
 Script para evitar espacios en blanco 
*/
txtNombres.addEventListener("keyup" , e=>{
  let String = e.target.value
  e.target.value = String.trimStart();
})

txtApellidos.addEventListener("keyup" , e=>{
  let String = e.target.value
  e.target.value = String.trimStart();
})
txtSalario.addEventListener("keyup" , e=>{
  let String = e.target.value
  e.target.value = String.trimStart();
})
txtBanco.addEventListener("keyup" , e=>{
  let String = e.target.value
  e.target.value = String.trimStart();
})
txtUsuario.addEventListener("keyup" , e=>{
  let String = e.target.value
  e.target.value = String.trimStart();
})
txtContraseña.addEventListener("keyup" , e=>{
  let String = e.target.value
  e.target.value = String.trimStart();
})




 
