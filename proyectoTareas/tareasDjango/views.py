from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .models import datosUsuario, tareasInformacion, comentarioTarea
import datetime
import json
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph
from reportlab.lib.units import inch
import io


# Create your views here.
def index(request):
    if request.method == 'POST':
        print(request)
        print(request.POST)
        nombreUsuario = request.POST.get('nombreUsuario')
        contraUsuario = request.POST.get('contraUsuario')
        usuarioInfo = authenticate(request,username=nombreUsuario,password=contraUsuario)
        if usuarioInfo is not None:
            login(request,usuarioInfo)
            return HttpResponseRedirect(reverse('tareasDjango:consolaAdministrador'))
        else:
            return HttpResponseRedirect(reverse('tareasDjango:index'))
    return render(request,'ingresoUsuario.html')

@login_required(login_url='/')
def consolaAdministrador(request):
    if request.method == 'POST':
        usernameUsuario = request.POST.get('usernameUsuario')
        contraUsuario = request.POST.get('contraUsuario')
        nombreUsuario = request.POST.get('nombreUsuario')
        apellidoUsuario = request.POST.get('apellidoUsuario')
        profesionUsuario = request.POST.get('profesionUsuario')
        emailUsuario = request.POST.get('emailUsuario')
        tipoUsuario = request.POST.get('tipoUsuario')
        nroCelular = request.POST.get('nroCelular')
        perfilUsuario = request.POST.get('perfilUsuario')
        usuarioNuevo = User.objects.create(
            username=usernameUsuario,
            email=emailUsuario
        )
        usuarioNuevo.set_password(contraUsuario)
        usuarioNuevo.first_name = nombreUsuario
        usuarioNuevo.last_name = apellidoUsuario
        usuarioNuevo.is_staff = True
        usuarioNuevo.save()
        datosUsuario.objects.create(
            user=usuarioNuevo,
            tipoUsuario=tipoUsuario,
            nroCelular=nroCelular,
            profesionUsuario=profesionUsuario,
            perfilUsuario=perfilUsuario,
            fechaIngreso=datetime.datetime.today()
        )
        return HttpResponseRedirect(reverse('tareasDjango:consolaAdministrador'))
    return render(request,'consolaAdministrador.html',{
        'usuariosTotales':User.objects.all().order_by('id')
    })

@login_required(login_url='/')
def cerrarSesion(request):
    logout(request)
    return HttpResponseRedirect(reverse('tareasDjango:index'))

def eliminarUsuario(request,idUsuario):
    usuarioEliminar = User.objects.get(id=idUsuario)
    usuarioEliminar.delete()
    return HttpResponseRedirect(reverse('tareasDjango:consolaAdministrador'))

def verUsuario(request,idUsuario):
    usuarioInformacion = User.objects.get(id=idUsuario)
    tareasUsuario = tareasInformacion.objects.filter(usuarioRelacionado=usuarioInformacion)
    print(len(tareasUsuario))
    return render(request,'informacionUsuario.html',{
        'usuarioInfo':usuarioInformacion,
        'tareasUsuario':tareasUsuario,
    })

def nuevaTarea(request,idUsuario):
    if request.method == 'POST':
        usuarioRelacionado = User.objects.get(id=idUsuario)
        print(usuarioRelacionado)
        print(usuarioRelacionado.username)
        fechaInicio = request.POST.get('fechaInicio')
        fechaFin = request.POST.get('fechaFin')
        descripcionTarea = request.POST.get('descripcionTarea')
        fechaInicioDate = datetime.datetime.strptime(fechaInicio,'%Y-%m-%d')
        fechaFinDate = datetime.datetime.strptime(fechaFin,'%Y-%m-%d')
        print('REGISTRANDO TAREA')
        infoTarea = tareasInformacion.objects.create(
            usuarioRelacionado=usuarioRelacionado,
            fechaInicio=fechaInicioDate,
            fechaFin=fechaFinDate,
            descripcionTarea=descripcionTarea,
            estadoTarea='PROCESO'
        )
        print(infoTarea)
        return HttpResponseRedirect(reverse('tareasDjango:verUsuario', kwargs={'idUsuario':idUsuario}))

def ejemploJavascript(request):
    return render(request,'ejemploJavascript.html')

def devolverMensaje(request):
    nombre = request.GET.get('nombre')
    apellido = request.GET.get('apellido')
    idTarea = request.GET.get('idTarea')
    return JsonResponse({
        'nombre':nombre,
        'apellido':apellido,
        'idTarea':idTarea
    })
def generate_user_report(users_data):
 # Esta función genera un reporte PDF de usuarios.
# 
    buffer = io.BytesIO()  # Crear un buffer de bytes para almacenar el PDF.
    
    doc = SimpleDocTemplate(buffer, pagesize=landscape(letter))
    styles = getSampleStyleSheet()
    
    data = []  # Lista para almacenar los datos de los usuarios en forma de tabla.
    
    # Agregar encabezados de columna a la tabla.
    data.append(['Nombre', 'Apellido', 'Celular', 'Edad'])
    
    for user in users_data:
        # Agregar los datos de cada usuario a la tabla.
        data.append([user['nombre'], user['apellido'], user['celular'], str(user['edad'])])
    
    # Crear la tabla con los datos.
    table = Table(data)
    table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                               ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                               ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                               ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                               ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                               ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                               ('GRID', (0, 0), (-1, -1), 1, colors.black)]))
    
    # Agregar la tabla al documento.
    elements = []
    elements.append(Paragraph("Reporte de Usuarios", styles['Title']))
    elements.append(table)
    
    doc.build(elements)  # Construir el documento PDF.
    
    buffer.seek(0)
    return buffer

def descargarReporteUsuarios(request):

    # Ejemplo de datos de usuarios 
    sample_users_data = [
        {'nombre': 'Juan', 'apellido': 'Pérez', 'celular': '920151260', 'edad': 30},
        {'nombre': 'María', 'apellido': 'Gómez', 'celular': '30320303', 'edad': 25},
        # Agrega más usuarios aquí...
                        ]

    # Generar el reporte PDF utilizando los datos de ejemplo.
    pdf_buffer = generate_user_report(sample_users_data)
    
    # Ahora, puedes guardar el contenido del buffer en un archivo PDF.

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="reporte_usuarios.pdf"'
    
    pdf_buffer.seek(0)
    response.write(pdf_buffer.read())
    
    return response   
    
def conseguirInfoTarea(request):
    comentariosTotales = []
    idTarea = request.GET.get('idTarea')
    tareaSeleccionada = tareasInformacion.objects.get(id=idTarea)
    comentariosTarea = tareaSeleccionada.comentariotarea_set.all().order_by('id')
    for comentarioInfo in comentariosTarea:
        comentariosTotales.append([
            str(comentarioInfo.usuarioRelacionado.first_name),
            comentarioInfo.comentario
        ])
    return JsonResponse({
        'descripcionTarea':tareaSeleccionada.descripcionTarea,
        'estadoTarea':tareaSeleccionada.estadoTarea,
        'fechaInicio':tareaSeleccionada.fechaInicio.strftime("%d-%m-%Y"),
        'fechaFin':tareaSeleccionada.fechaFin.strftime("%d-%m-%Y"),
        'idTarea':idTarea,
        'comentariosTotales':comentariosTotales
    })

def publicarComentario(request):
    datos = json.load(request)
    idTarea = datos.get('idTarea')
    comentario = datos.get('comentario')
    usuarioRelacionado = request.user
    tareaRelacionado = tareasInformacion.objects.get(id=idTarea)
    comentarioTarea.objects.create(
        tareaRelacionado=tareaRelacionado,
        usuarioRelacionado=usuarioRelacionado,
        comentario=comentario
    )
    return JsonResponse({
        'resp':'ok'
    })

def reactDjango(request):
    return render(request,'reactDjango.html')

def conseguirInfoUsuarios(request):
    return JsonResponse({
        'infoDjango':[
            ['Alexander','Segovia','25'],
            ['Javier','Hilario','32'],
            ['Miguel','Vargas','26'],
            ['Martin','Jara','25']
        ]
    })