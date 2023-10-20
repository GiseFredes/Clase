from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def indice(request):
    context={
        'nombre_usuario':'Carlos Vives',
        'fecha': datetime.now(),
        'es_instructor': True,
    }
    return render(request, 'portal/index.html', context)

# def cursos(request):
#     return HttpResponse('<b>Todos los cursos</b>') ahora le agrego un parametro
def cursos(request, inicio):
    return HttpResponse(f"<b>Todos los cursos desde {inicio}</b>")

def alumno_listado(request):
    # return HttpResponse("""
    #     <ul>
    #         <li>Paquita  la del Barrio</li>
    #         <li>Angela Leiva</li>
    #         <li>Luciano Pereyra</li>
    #     </ul>
    #     """) Lo vamos a a cambiar por la plantilla de html
    context = {
        'cant_inscriptos': 10,
        'listado': [
            'Abel Pintos',
            'Luciando Pereyra',
            'Ricardo Arjona',
            'Ulises Bueno',
            'Rocio Quiroz',
            'Leo Matioli',
            'Emanuel Nohir',
        ] #Son las variables que utilizo en en la pagina html   
    } #El context puede estar definido o no, y es un diccionario siempre qque va a tener las variables de contexto, o sea la data con la que quiero renderizar esta plantilla
    return render(request, 'portal/alumno_listado.html', context)

def alumno_detalle(request, nombreAlumno):
    return HttpResponse(
        f"""
        <h1>Bienvenido {nombreAlumno}</h1>
        <p>Página personal de usuario</p>
        """
    )

def alumnos_historico(request, year):
    return HttpResponse(f'<h1>Historico de Alumnos del año: {year}</h1>')

def alumnos_estado(request, estado):
    return HttpResponse(f'Filtrar alumnos por estado: {estado}')
