
// Script para sumar tptal Valor Total Operacion
window.addEventListener("load", function(){
    valorTotalOperacion();
})

function valorTotalOperacion(){
    let total = 0;
    const table = document.getElementById("Proceso_Operaciones");
    for(let i = 1; i< table.rows.length-1; i++){

        let rowValue = table.rows[i].cells[6].innerHTML;
        total = total + Number(rowValue);
    }
    const tdTotal = document.getElementById("tdTotal");
    tdTotal.textContent = total;
}
////////////////////////////////////////////////////////////////////////////////////////
// Script para botones filtros de busqueda
window.onload = () => {
    console.log(document.querySelector("#Proceso_Operaciones > tbody > tr:nth-child(1) > td:nth-child(2) ").innerHTML);
};
getUniqueValuesFromColumn()
function getUniqueValuesFromColumn() {

    var unique_col_values_dict = {}

    allFilters = document.querySelectorAll(".table-filter")
    allFilters.forEach((filter_i) => {
        col_index = filter_i.parentElement.getAttribute("col-index");
        // alert(col_index)
        const rows = document.querySelectorAll("#Proceso_Operaciones > tbody > tr")

        rows.forEach((row) => {
            cell_value = row.querySelector("td:nth-child("+col_index+")").innerHTML;
            if (col_index in unique_col_values_dict) {

                if (unique_col_values_dict[col_index].includes(cell_value)) {

                } else {
                    unique_col_values_dict[col_index].push(cell_value)
                   

                }


            } else {
                unique_col_values_dict[col_index] = new Array(cell_value)
            }
        });

    });
    updateSelectOptions(unique_col_values_dict)

};

function updateSelectOptions(unique_col_values_dict) {
    allFilters = document.querySelectorAll(".table-filter")

    allFilters.forEach((filter_i) => {
        col_index = filter_i.parentElement.getAttribute('col-index')

        unique_col_values_dict[col_index].forEach((i) => {
            filter_i.innerHTML = filter_i.innerHTML + `\n<option value="${i}">${i}</option>`
        });

    });
};

function filter_rows() {
    allFilters = document.querySelectorAll(".table-filter")
    var filter_value_dict = {}

    allFilters.forEach((filter_i) => {
        col_index = filter_i.parentElement.getAttribute('col-index')

        value = filter_i.value
        if (value != "all") {
            filter_value_dict[col_index] = value;
        }
    });

    var col_cell_value_dict = {};

    const rows = document.querySelectorAll("#Proceso_Operaciones tbody tr");
    rows.forEach((row) => {
        var display_row = true;

        allFilters.forEach((filter_i) => {
            col_index = filter_i.parentElement.getAttribute('col-index')
            col_cell_value_dict[col_index] = row.querySelector("td:nth-child(" + col_index+ ")").innerHTML
        })

        for (var col_i in filter_value_dict) {
            filter_value = filter_value_dict[col_i]
            row_cell_value = col_cell_value_dict[col_i]
            
            if (row_cell_value.indexOf(filter_value) == -1 && filter_value != "all") {
                display_row = false;
                break;
            }

        }

        if (display_row == true) {
            row.style.display = "table-row"

        } else {
            row.style.display = "none"

        }

    })

}

//////////////////////////////////////////////////////////////////////////////

// Script para imprimir
function imprimirDatos(){
        Window.print();
    }
    const $btnExportar = document.querySelector("#btnExportar"),
        $tabla = document.querySelector("#Proceso_Operaciones");

    $btnExportar.addEventListener("click", function() {
        let tableExport = new TableExport($tabla, {
            exportButtons: false, // No queremos botones
            filename: "Proceso-Operaciones", //Nombre del archivo de Excel
            sheetname: "Proceso-Operaciones", //Título de la hoja
        });
        let datos = tableExport.getExportData();
        let preferenciasDocumento = datos.Proceso_Operaciones.xlsx;
        tableExport.export2file(preferenciasDocumento.data, preferenciasDocumento.mimeType, 
                                preferenciasDocumento.filename, preferenciasDocumento.fileExtension, 
                                preferenciasDocumento.merges, preferenciasDocumento.RTL, preferenciasDocumento.sheetname);
    });

//////////////////////////////////////////////////////////////////////////
   





