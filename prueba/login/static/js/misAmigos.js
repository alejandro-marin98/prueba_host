document.addEventListener('DOMContentLoaded', setup);

async function setup() {
    console.log('Ha cargado el html')
    let datatable1;
    let datatable2;


    // try {
        // openSpinner();

        const dataTableOptions = {
            
            // Modificar las columnas de los resultados de la tabla
            columnDefs: [
                // classname es el nombre de la clase que le quieres añadir
                // targets es el indice de las columnas que quieres que sean afectadas
                // { className: "nombre_clase", targets: [0, 1, 2, 3, 4] },
                // // qué columnas NO van a ser ordenables
                // { orderable: false, targets: [4] },
                // { searchable: false, targets: [2, 3, 4] }

            ],

            // Items por página
            pageLength: 5,

            // Que se pueda destruir y volver a crear
            destroy: true,

            // Idioma
            language: {
                lengthMenu: "Mostrar _MENU_ registros por página",
                zeroRecords: "No se han encontrado usuarios.",
                info: "Mostrando _START_ - _END_ de _TOTAL_ usuarios",
                infoEmpty: "Ningún usuario encontrado.",
                infoFiltered: "(filtrados desde _MAX_ registros totales)",
                loadingRecords: "Cargando...",
                paginate: {
                    first: "Primero",
                    last: "Último",
                    next: "Siguiente",
                    previous: "Anterior"
                }

            },

            scrollX: true,
            "activate": function(event, ui) {
                $( $.fn.dataTable.tables( true ) ).DataTable().columns.adjust();
            }


        };
        
        datatable1 = $('.table-amigos').DataTable(dataTableOptions);
        datatable2 = $('.table-no_amigos').DataTable(dataTableOptions);
        console.log(datatable1)
        console.log(datatable2)

        document.querySelector('#label-amigos').addEventListener('click', () => {
            let divs = document.querySelectorAll('.esconder');
            console.log(divs.length)
            divs[0].classList.remove('desaparecer');
            divs[1].classList.add('desaparecer');
            datatable1.columns.adjust().draw();
        })
        document.querySelector('#label-noamigos').addEventListener('click', () => {
            let divs = document.querySelectorAll('.esconder');
            console.log(divs.length)
            divs[0].classList.add('desaparecer');
            divs[1].classList.remove('desaparecer');
            datatable2.columns.adjust().draw();
        })



        // closeSpinner();

        
    // } catch(e) {
    //     closeSpinner();
    //     alert(`Lo sentimos, no hemos podido mostrar los datos. Error: ${e}`)
    // }

}