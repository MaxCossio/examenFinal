function cargarInformacionTarea(idTarea)
{
    console.log(idTarea)
    fetch(`/conseguirInfoTarea?idTarea=${idTarea}`)
    .then(response => response.json())
    .then(data => {
        fechaInicioDetalle = document.getElementById('fechaInicioDetalle')
        fechaFinDetalle = document.getElementById('fechaFinDetalle')
        estadoTareaDetalle = document.getElementById('estadoTareaDetalle')
        descripcionTareaDetalle = document.getElementById('descripcionTareaDetalle')
        indTarea = document.getElementById('indTarea')
        comentariosTareaTotales = document.getElementById('comentariosTareaTotales')

        fechaInicioDetalle.value = data.fechaInicio
        fechaFinDetalle.value = data.fechaFin
        estadoTareaDetalle.value = data.estadoTarea
        descripcionTareaDetalle.value = data.descripcionTarea
        indTarea.innerHTML = data.idTarea
        comentariosTareaTotales.innerHTML = ''
        for(let j = 0; j < data.comentariosTotales.length; j++)
        {
            comentariosTareaTotales.innerHTML += `
                <div class='row mb-3'>
                    <div class='col-3'>
                        ${data.comentariosTotales[j][0]}
                    </div>
                    <div class='col-9'>
                        ${data.comentariosTotales[j][1]}
                    </div>
                </div>
            `
        }
    })
}

function enviarComentario()
{
    url = '/publicarComentario'
    datos = {
        'comentario':document.getElementById('comentarioUsuario').value,
        'idTarea':document.getElementById('indTarea').innerHTML
    }
    fetch(url,{
        method:"POST",
        headers:{
            "X-Requested-With":"XMLHttpRequest",
            "X-CSRFToken":getCookie("csrftoken")
        },
        body:JSON.stringify(datos)
    })
    .then(response => response.json())
    .then(data => {
        console.log(data)
        cargarInformacionTarea(document.getElementById('indTarea').innerHTML)
        document.getElementById('comentarioUsuario').value = ''
    })
}

function getCookie(name)
{
    let cookieValue = null
    if(document.cookie && document.cookie !== '')
    {
        cookies = document.cookie.split(';')
        for(let i = 0; i < cookies.length; i++)
        {
            cookie = cookies[i].trim()
            if(cookie.substring(0,name.length + 1) === (name + '='))
            {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue
}