function aumentarValor()
{
    numeroAumentar = document.querySelector('h1')
    nuevoNumero = Number(numeroAumentar.innerHTML) + 1
    numeroAumentar.innerHTML = String(nuevoNumero)
}

function disminuirValor()
{
    numeroAumentar = document.querySelector('h1')
    nuevoNumero = Number(numeroAumentar.innerHTML) - 1
    numeroAumentar.innerHTML = String(nuevoNumero)
}

function agregarNumero()
{
    valorNumero = document.getElementById('numeroNuevo')
    listaNumeros = document.getElementById('listaNumeros')
    listaNumeros.innerHTML += `<li class='numeroLista'>${valorNumero.value}</li>`
}

function imprimirSeleccion()
{
    seleccionarNumero = document.getElementById('seleccionarNumero')
    console.log(seleccionarNumero.value)
    document.getElementById('numeroNuevo').value = seleccionarNumero.value
}

function sumarTodosLosNumeros()
{
    arregloElementos = document.querySelectorAll('.numeroLista')
    let sumaTotal = 0
    for(let i = 0; i < arregloElementos.length; i++)
    {
        numTemp = Number(arregloElementos[i].innerHTML)
        sumaTotal = sumaTotal + numTemp
    }
    sumaFinal = document.getElementById('sumaFinal')
    sumaFinal.innerHTML = String(sumaTotal)
}

function cambiarColor()
{
    console.log('Mouse encima del div')
    divisionColor = document.getElementById('divisionColor')
    divisionColor.style.backgroundColor = 'red'
}

function devolverColor()
{
    console.log('Mouse dejando del div')
    divisionColor = document.getElementById('divisionColor')
    divisionColor.style.backgroundColor = 'blue'
}