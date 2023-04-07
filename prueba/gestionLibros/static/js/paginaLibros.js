document.addEventListener('DOMContentLoaded', () => {
    let datatable = $('#opiniones').DataTable();

    const select = document.querySelector('select');
    select.addEventListener('change', e => {
        document.querySelector('.cont button').style.display = 'block';

        if (e.target.value == 'sin_guardar') {
                e.target.classList.value = 'op1'
                console.log(e.target)
        }

        if (e.target.value == 'pendiente') {
                e.target.classList.value = 'op2'
                console.log(e.target)
        }

        if (e.target.value == 'leyendo') {
                e.target.classList.value = 'op3'
                console.log(e.target)
        }
        
        if (e.target.value == 'leido') {
                e.target.classList.value = 'op4'
                console.log(e.target)
        }
    })

});