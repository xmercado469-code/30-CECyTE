from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">

<title>30 Aniversario CECyTE Jalisco Plantel 08 Ixtlahuacan del Río</title>

<style>

:root {
    --verde: #075b3b;
    --verde2: #168257;
    --dorado: #d9ad37;
    --blanco: #fffdf5;
    --texto: #26382d;
}

* {
    box-sizing: border-box;
}

body {
    margin: 0;
    font-family: Arial, sans-serif;
    background: #eaf2e9;
    color: var(--texto);
}

body.diseno2 {
    background: #f5f0df;
}

.barra {
    background: var(--verde);
    color: white;
    padding: 15px 5%;
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    border-bottom: 5px solid var(--dorado);
}

.barra a {
    color: var(--verde);
    background: var(--blanco);
    padding: 10px 15px;
    border-radius: 20px;
    text-decoration: none;
    font-weight: bold;
}

.contenedor {
    max-width: 1050px;
    margin: 25px auto;
    padding: 10px;
}

.pantalla {
    background: var(--blanco);
    border: 7px solid #1c3024;
    border-radius: 25px;
    overflow: hidden;
    box-shadow: 0 7px 20px #0002;
}

.diseno2 .pantalla {
    border: 5px solid var(--verde);
    border-radius: 10px;
}

.encabezado {
    background: linear-gradient(120deg, #075b3b, #168257);
    color: white;
    text-align: center;
    padding: 25px 15px;
    border-bottom: 5px solid var(--dorado);
}

.logo {
    height: 280px;
    max-width: 100%;
    object-fit: fill;
    margin: 10px auto;
}

.aniversario {
    height: 220px;
    max-width: 180px;
    object-fit: contain;
    display: block;
    margin: 12px auto;
}

h1 {
    font-size: 30px;
    margin: 10px 0;
}

h2 {
    background: var(--verde);
    color: white;
    padding: 12px;
    border-left: 6px solid var(--dorado);
    border-radius: 8px;
    font-size: 20px;
    margin-top: 25px;
}

h3 {
    color: var(--verde);
}

.contenido {
    padding: 22px;
}

.intro {
    background: white;
    padding: 17px;
    border: 2px solid #e5d49a;
    border-radius: 13px;
    line-height: 1.6;
    margin: 15px 0;
}

.tarjetas {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 15px;
}

.tarjeta {
    background: white;
    border: 2px solid #dce6d9;
    padding: 15px;
    border-radius: 13px;
    box-shadow: 0 4px 5px #0001;
}

.diseno2 .tarjeta {
    border-radius: 3px;
    border-color: #d9bd68;
}

.foto {
    width: 100%;
    height: 170px;
    object-fit: cover;
    border-radius: 9px;
    margin: 8px 0;
    background: #e7eee5;
}

.foto-deportes {
    width: 65%;
    height: auto;
    max-height: 280px;
    object-fit: contain;
    display: block;
    margin: 10px auto;
    border-radius: 12px;
}
.foto-cultura {
    width: 65%;
    height: auto;
    max-height: 280px;
    object-fit: contain;
    display: block;
    margin: 10px auto;
    border-radius: 12px;
}
.foto-logros {
    width: 65%;
    height: auto;
    max-height: 280px;
    object-fit: contain;
    display: block;
    margin: 10px auto;
    border-radius: 12px;
}
.foto-grande {
    width: 100%;
    max-height: 260px;
    object-fit: cover;
    border-radius: 12px;
}

.boton {
    display: block;
    background: var(--verde2);
    color: white;
    text-align: center;
    text-decoration: none;
    padding: 13px;
    border: 2px solid var(--dorado);
    border-radius: 12px;
    font-weight: bold;
    margin: 8px 0;
}

.boton:hover {
    background: var(--verde);
}

.menu {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 12px;
}

.menu .boton:last-child {
    grid-column: 1 / -1;
}

.linea {
    border-left: 4px solid var(--dorado);
    padding-left: 18px;
    margin-left: 12px;
}

.evento {
    border-left: 5px solid var(--dorado);
}

.cita {
    font-style: italic;
    color: #455b49;
}

.formulario input,
.formulario textarea {
    width: 100%;
    padding: 12px;
    border: 2px solid #b8cdb9;
    border-radius: 8px;
    margin: 8px 0 15px;
    font-size: 15px;
}

.formulario label {
    font-weight: bold;
    color: var(--verde);
}

.formulario textarea {
    min-height: 100px;
}

.navegacion {
    display: flex;
    justify-content: space-between;
    gap: 10px;
    padding: 15px;
    background: var(--verde);
    flex-wrap: wrap;
}

.foto-generacion {
    width: 100%;
    max-width: 350px;
    height: 180px;
    object-fit: cover;
    border-radius: 12px;
    display: block;
    margin: 10px auto;
}
.video-entrevista {
    width: 100%;
    max-width: 500px;
    height: auto;
    border-radius: 12px;
    margin: 10px 0;
}
.foto-completa {
    width: 100%;
    height: auto;
    max-height: 350px;
    object-fit: contain;
    display: block;
    margin: 10px auto;
    border-radius: 12px;
}

.navegacion a {
    background: #fff1bd;
    color: var(--verde);
    padding: 11px 17px;
    border-radius: 25px;
    text-decoration: none;
    font-weight: bold;
}


.navegacion .inicio {
    background: var(--dorado);
}

.pie {
    text-align: center;
    padding: 15px;
    color: #526b58;
    font-size: 13px;
}

@media(max-width:650px) {
    .tarjetas {
        grid-template-columns: 1fr;
    }

    h1 {
        font-size: 23px;
    }

    .menu {
        grid-template-columns: 1fr;
    }

    .menu .boton:last-child {
        grid-column: auto;
    }
}

</style>
</head>



<header class="barra">
    <div>
        <b>CECyTEJ PLANTEL 08</b>
        <br>
        <small>IXTLAHUACAN DEL RIO · 30 ANIVERSARIO</small>
    </div>

</header>

<div class="contenedor">

<section class="pantalla">

<header class="encabezado">

<img src="{{ url_for('static', filename='logo_cecytej.png.jpeg') }}"
class="logo" alt="Logotipo CECyTEJ">

<h1>{{ titulo }}</h1>

<p>{{ subtitulo }}</p>

</header>

<div class="contenido">

{% if numero == 1 %}

<h2>Bienvenidos a nuestra historia</h2>

<img src="{{ url_for('static', filename='plantel.jpg.jpeg') }}"
class="foto-grande" alt="Plantel 08">

<div class="intro">
Celebramos 30 años de aprendizaje, esfuerzo y superación.
Durante tres décadas, el CECyTEJ Plantel 08 Ixtlahuacán del Río
ha formado generaciones de estudiantes y brindado oportunidades
para construir un mejor futuro.
</div>

<h2>Explora nuestra aplicación</h2>

<nav class="menu">

<a class="boton" href="/pantalla/2/{{ estilo }}">
📖 Nuestra historia
</a>

<a class="boton" href="/pantalla/3/{{ estilo }}">
👥 Voces que dejan huella
</a>

<a class="boton" href="/pantalla/4/{{ estilo }}">
🏆 Orgullo CECyTEJ
</a>

<a class="boton" href="/pantalla/5/{{ estilo }}">
🎉 Celebremos juntos
</a>

<a class="boton" href="/pantalla/6/{{ estilo }}">
🚀 Nuestro futuro
</a>

</nav>

{% elif numero == 2 %}

<div class="intro">
El Plantel 08 inició su historia en septiembre de 1999,
gracias a la iniciativa del entonces presidente municipal,
el Dr. Haro Trello, quien impulsó la creación de una
institución tecnológica en el municipio.
</div>

<h2>Línea del tiempo: tres décadas de transformación</h2>

<div class="linea">

<div class="tarjeta">
<h3>1999 · El comienzo</h3>
<p>
Surgió la idea de crear una escuela tecnológica en el municipio.
Las primeras clases se impartieron en lo que actualmente
es el DIF municipal.
</p>
</div>

<br>

<div class="tarjeta">
<h3>2000 · Primeras instalaciones</h3>
<p>
Para este año ya se contaba con cuatro grupos y el plantel
se trasladó a su ubicación actual. Se inició con un edificio
que tenía baños, un laboratorio de química, uno de computación
y cinco salones.
</p>
</div>

<br>

<div class="tarjeta">
<h3>2010 - 2015 · Crecimiento</h3>
<p>
Durante estos años comenzó la construcción de otro edificio
y el plantel continuó extendiéndose para brindar mejores
espacios a sus estudiantes.
</p>
</div>

<br>

<div class="tarjeta">
<h3>2026 · Actualidad</h3>
<p>
Actualmente el plantel cuenta con dos laboratorios de
computación, diez aulas, taller de electromecánica,
cafetería, domo, laboratorio de química y oficinas
administrativas.
</p>
</div>

</div>

<h2>El plantel antes y ahora</h2>

<div class="tarjetas">

<div class="tarjeta">
<h3>Antes</h3>
<img src="{{ url_for('static', filename='antes.jpg') }}"
class="foto" alt="Instalaciones antiguas">
<p>Así eran las primeras instalaciones del plantel.</p>
</div>

<div class="tarjeta">
<h3>Después</h3>
<img src="{{ url_for('static', filename='despues.jpg.jpeg') }}"
class="foto" alt="Instalaciones actuales">
<p>Así luce actualmente nuestra institución.</p>
</div>

</div>

<h2>Cambios y mejoras</h2>

<div class="intro">
El Plantel 08 ha tenido muchas mejoras a lo largo de los años,
desde sus aulas hasta sus áreas verdes. La institución se ha
extendido considerablemente. Entre las construcciones más
recientes destacan unas escaleras y el bardeado de la zona
que se encuentra alrededor de la escuela, del lado del río.
</div>

<h2>Recuerdos de generaciones anteriores</h2>

<div class="tarjeta">
<p>
Uno de los recuerdos que nos compartieron fue el de una
generación que enganchó los carros de Nicolás y del profesor
Juan por las defensas. No se dieron cuenta hasta que el
profesor Juan intentó irse y notó que su carro no avanzaba
normalmente. Fue entonces cuando descubrió lo que habían hecho.
</p>
</div>

<h2>Acontecimientos importantes</h2>

<div class="tarjetas">

<div class="tarjeta">
<h3>🏅 Encuentro deportivo</h3>
<p>
Se realizó un encuentro deportivo en las instalaciones
de nuestro plantel, reuniendo a estudiantes de diferentes
lugares.
</p>
</div>

<div class="tarjeta">
<h3>👑 Embajadora CECyTEJ</h3>
<p>
El municipio fue sede del concurso de Embajadora CECyTEJ.
Nuestro plantel brindó hospedaje a participantes provenientes
de los 15 planteles.
</p>
</div>

</div>

<h2>Crecimiento de nuestra comunidad estudiantil</h2>

<div class="intro">
En sus inicios, la institución tenía aproximadamente
60 alumnos distribuidos en dos grupos. Actualmente cuenta
con 12 grupos y alrededor de 500 estudiantes.
<br><br>
<b>¡Tres décadas de crecimiento y oportunidades!</b>
</div>

{% elif numero == 3 %}

<div class="intro">
La historia del CECyTEJ también está formada por las personas
que han dejado huella en nuestra institución: exalumnos,
docentes, personal administrativo y estudiantes.
</div>

<h2>Entrevistas a exalumnos</h2>

<div class="tarjetas">

<div class="tarjeta">
<h3>🎥 Entrevista en video</h3>
<video controls
<video controls class="video-entrevista">
    <source src="{{ url_for('static', filename='entrevista1.mp4') }}" type="video/mp4">
    Tu navegador no puede reproducir este video.
</video>

<p>
Entrevista a Norma Avila
</p>
</div>

<div class="tarjeta">
<h3>🎤 Entrevista de preguntas y respuestas</h3>
<p>
Entrevista a Melisa Mercado <br>
 <br>
1-¿Porqué elegiste CECyTEJ? <br>

Me parecio una escuela que cumplia con la mayoria de los criterios, era amplia y en buenas condiciones, aparte tenia buenas referencias de ella. <br>
 <br>
2-¿Los conocimientos que adquiriste en CECyTEJ te ayudaron en la universidad y en la vida? <br>
Si, ya que son conocimientos que muchas veces se practican y te sirven a lo largo de ru vida  <br>
 <br>
3-¿Qué consejos podrias darles a loa alumnos que hoy en dia estudian en CECyTEJ? <br>
Que estudien y disfruten su etapa, ya que sus conocimientos los pueden usar mas adelante para sus siguientes estudios <br>
 <br>
4-¿Cual fue tu mayor satisfacción al estudiar en CECyTEJ? <br>
Tener buena relación con maestros, amigos y personal que trabajan ahí, además de poder egresar con un título.

</p>
</div>

</div>

<h2>Mensajes de nuestros docentes</h2>

<div class="tarjeta">
<h3>José Juan Angulo</h3>
<p class="cita">
"Sigan sus metas académicas y cumplan sus sueños,
que pueden lograr todos sus sueños".
</p>
</div>

<div class="tarjeta">
<h3>Aurelia Rostro</h3>
<p class="cita">
"Siempre den lo mejor de ustedes, estando donde estén".
</p>
</div>

<div class="tarjeta">
<h3>Cristina Limón</h3>
<p class="cita">
"Que valoren y aprovechen su escuela".
</p>
</div>

<div class="tarjeta">
<h3>Nicolás Tovar</h3>
<p class="cita">
"No dejen de estudiar, de trabajar y mucho menos de soñar,
ya que son el futuro de México".
</p>
</div>

<h2>Experiencias de estudiantes actuales</h2>


<p>
Alumnas de nuestro plantel tuvieron la oportunidad de viajar
a otro estado para representar con orgullo al CECyTEJ
en un concurso, demostrando su talento, preparación
y compromiso.
</p>
</div>

<h2>Fundador y primeros docentes</h2>


<p>
<b>Fundador:</b> Dr. Haro Trello.
</p>

<p>
<b>Docentes:</b> Juan Angulo, José de Jesús Estrada,
Juan José Esqueda, Cristina Limón, Nicolás Tovar,
Víctor Manuel González y Ricardo Canales.
</p>
</div>


<h2>Generaciones</h2>

<div class="tarjetas">

<div class="tarjeta">
<img src="{{ url_for('static', filename='generacion1.png.jpeg') }}"
class="foto-generacion" 
<p>Recuerdo de una generación de nuestro plantel.</p>
</div>

<div class="tarjeta">
<img src="{{ url_for('static', filename='generacion2.jpeg') }}"
class="foto" alt="Generación pasada ">
<p>Recuerdo de otra generación que forma parte de nuestra historia.</p>

</div>

</div>

<h2>Orgullo de pertenecer al CECyTEJ</h2>

<div class="intro">
"Ser parte del CECyTEJ significa crecer, aprender y
construir nuevas oportunidades".

"Cada generación deja una huella y cada estudiante
contribuye a nuestra historia".
</div>

<h2>Formando profesionistas y mejores personas</h2>

<div class="intro">
Nuestro plantel no solamente brinda conocimientos académicos
y técnicos, también fomenta valores como el respeto,
la responsabilidad, el compañerismo y el trabajo en equipo.
Prepara a sus estudiantes para continuar sus estudios,
incorporarse al mundo laboral y contribuir positivamente
a la sociedad.
</div>

{% elif numero == 4 %}

<div class="intro">
El talento y esfuerzo de nuestros estudiantes se reflejan
en sus proyectos, concursos, actividades y reconocimientos.
Estos logros representan el orgullo de pertenecer
al CECyTEJ Plantel 08.
</div>

<h2>💻 Tecnología</h2>

<div class="tarjeta">
<img src="{{ url_for('static', filename='tecnologia.jpg') }}"
class="foto" alt="Proyectos tecnológicos">

<h3>Proyectos tecnológicos</h3>

<p>
Los estudiantes desarrollan aplicaciones y páginas web
como parte de su formación en la carrera de Programación,
poniendo en práctica sus conocimientos y creatividad.
</p>
</div>

<h2>🧪 Ciencia</h2>

<div class="tarjeta">
<img src="{{ url_for('static', filename='feria.jpg.jpeg') }}"
class="foto-completa" alt="Feria de ciencias">

<h3>Feria de ciencias</h3>

<p>
Cada año se lleva a cabo una feria de ciencias en las
instalaciones del plantel. En ella se presentan diferentes
proyectos realizados en las distintas materias y se
comparten con estudiantes de secundaria.
</p>
</div>

<h2>⚽ Deportes</h2>

<div class="tarjeta">
<img src="{{ url_for('static', filename='deportes.jpeg') }}"
class="foto-deportes" alt="Actividades deportivas">

<p>
Nuestros estudiantes participan en encuentros deportivos.
En uno de ellos, el equipo varonil de voleibol obtuvo
el primer lugar, representando con orgullo a nuestra escuela.
</p>
</div>

<h2>🎭 Cultura</h2>

<div class="tarjeta">
<img src="{{ url_for('static', filename='cultura1.jpeg') }}"
class="foto-cultura" alt="Actividades culturales">

<p>
Entre las actividades culturales y extracurriculares
destaca el certamen de Embajadora CECyTEJ, que se realiza
cada año y permite la participación y convivencia
de la comunidad estudiantil. 
</p>
</div>

<h2>🏆 Logros académicos</h2>

<div class="tarjeta">
<img src="{{ url_for('static', filename='logros.jpeg') }}"
class="foto-logros" alt="Logros académicos">

<h3>Festival Académico CECyTE Jalisco 2026</h3>

<p>
En la edición 2026 del Festival Académico CECyTE Jalisco,
seis alumnos de nuestro plantel lograron avanzar
a la etapa estatal, demostrando su preparación,
dedicación y talento académico.
</p>
</div>

<h2>♟️ Otras actividades</h2>

<div class="intro">
También se realizan actividades extracurriculares,
torneos y dinámicas que fomentan la convivencia,
el aprendizaje y el desarrollo de nuevas habilidades.
</div>

{% elif numero == 5 %}

<div class="intro">
¡Estamos de fiesta!
Invitamos a estudiantes, docentes, exalumnos y padres
de familia a celebrar los 30 años de historia del
CECyTEJ Plantel 08 Ixtlahuacán del Río.
</div>

<h2>Agenda de actividades del 30 aniversario</h2>

<div class="tarjetas">

<div class="tarjeta evento">
<h3>🎉 1. Ceremonia de inauguración</h3>
<p>
Acto conmemorativo para dar inicio a los festejos
del 30 aniversario.
</p>
<b>Fecha:</b> Por confirmar.
<br><b>Horario:</b> Por confirmar.
<br><b>Lugar:</b> Plantel 08.
</div>

<div class="tarjeta evento">
<h3>📸 2. Exposición fotográfica</h3>
<p>
Recorrido por fotografías antiguas y actuales
que muestran la historia de nuestra institución.
</p>
<b>Fecha:</b> Por confirmar.
<br><b>Horario:</b> Por confirmar.
<br><b>Lugar:</b> Plantel 08.
</div>

<div class="tarjeta evento">
<h3>🎤 3. Festival de talentos</h3>
<p>
Presentaciones de canto, baile, música y otras
habilidades de nuestros estudiantes.
</p>
<b>Fecha:</b> Por confirmar.
<br><b>Horario:</b> Por confirmar.
<br><b>Lugar:</b> Domo del plantel.
</div>

<div class="tarjeta evento">
<h3>💻 4. Feria tecnológica</h3>
<p>
Exposición de aplicaciones, páginas web y proyectos
tecnológicos elaborados por estudiantes.
</p>
<b>Fecha:</b> Por confirmar.
<br><b>Horario:</b> Por confirmar.
<br><b>Lugar:</b> Laboratorios.
</div>

<div class="tarjeta evento">
<h3>⚽ 5. Encuentro deportivo</h3>
<p>
Actividades y competencias deportivas para
fomentar la convivencia.
</p>
<b>Fecha:</b> Por confirmar.
<br><b>Horario:</b> Por confirmar.
<br><b>Lugar:</b> Instalaciones deportivas.
</div>

<div class="tarjeta evento">
<h3>🏅 6. Reconocimiento a generaciones</h3>
<p>
Homenaje a exalumnos, docentes y personas que
han formado parte de los 30 años de historia.
</p>
<b>Fecha:</b> Por confirmar.
<br><b>Horario:</b> Por confirmar.
<br><b>Lugar:</b> Plantel 08.
</div>

</div>

<h2>Galería de la celebración</h2>

<div class="tarjeta">
<p>
Aquí se mostrarán las fotografías de los momentos
más especiales de nuestro aniversario.
</p>
</div>

<div class="intro">
Todas las actividades anteriores son propuestas
conmemorativas. Las fechas y horarios se actualizarán
cuando sean confirmados oficialmente.
</div>

{% elif numero == 6 %}

<div class="intro">
Imaginamos al CECyTEJ Plantel 08 dentro de los próximos
30 años como una institución moderna, reconocida
por su calidad educativa, tecnología y compromiso
con la comunidad.
</div>

<h2>Nuestros sueños para el futuro</h2>

<div class="tarjetas">

<div class="tarjeta">
<h3>🏫 Mejores instalaciones</h3>
<p>
Contar con aulas modernas, laboratorios equipados,
espacios deportivos y áreas verdes en mejores condiciones.
</p>
</div>

<div class="tarjeta">
<h3>💻 Nuevas tecnologías</h3>
<p>
Incorporar herramientas digitales, computadoras
modernas y recursos tecnológicos para mejorar
el aprendizaje.
</p>
</div>

<div class="tarjeta">
<h3>🌟 Nuevas metas y proyectos</h3>
<p>
Desarrollar proyectos innovadores que permitan
a los estudiantes demostrar sus habilidades
y conocimientos.
</p>
</div>

<div class="tarjeta">
<h3>🌱 Compromiso ambiental</h3>
<p>
Cuidar las áreas verdes, ahorrar agua y energía,
separar residuos y mantener limpias las instalaciones.
</p>
</div>

<div class="tarjeta">
<h3>🤝 Compromiso con la comunidad</h3>
<p>
Participar en actividades que beneficien al municipio
y fortalezcan la relación entre la escuela y la sociedad.
</p>
</div>

<div class="tarjeta">
<h3>💚 Mensaje a las futuras generaciones</h3>
<p>
Aprovechen cada oportunidad, valoren su escuela,
esfuércense por cumplir sus metas y nunca dejen
de aprender y soñar.
</p>
</div>

</div>

<h2>Mi mensaje para el futuro</h2>

<div class="tarjeta formulario">

<form method="POST" action="/enviar">

<label>Nombre del estudiante</label>
<input type="text" name="nombre" required
placeholder="Escribe tu nombre">

<label>Semestre y grupo</label>
<input type="text" name="grupo" required
placeholder="Ejemplo: 3° C">

<label>Mensaje para las próximas generaciones</label>
<textarea name="mensaje" required
placeholder="Escribe tu mensaje para el futuro..."></textarea>

<button class="boton" type="submit">
Enviar mi mensaje
</button>

</form>

</div>

<h2>Una historia que continúa</h2>

<div class="intro">
Cada generación tiene la oportunidad de escribir
una nueva página en la historia de nuestra institución.
Sigamos construyendo juntos un mejor CECyTEJ.

<br><br>

<b>¡El futuro comienza con nosotros!</b>
</div>

{% endif %}

</div>

<nav class="navegacion">

{% if numero > 1 %}
<a href="/pantalla/{{ numero-1 }}/{{ estilo }}">
← Regresar
</a>
{% endif %}

<a class="inicio" href="/pantalla/1/{{ estilo }}">
⌂ Inicio
</a>

{% if numero < 6 %}
<a href="/pantalla/{{ numero+1 }}/{{ estilo }}">
Continuar →
</a>
{% endif %}

</nav>

</section>

<div class="pie">
CECyTEJ Plantel 08 Ixtlahuacán del Río
<br>
30 AÑOS FORMANDO GENERACIONES, CONSTRUYENDO OPORTUNIDADES
</div>

</div>

</body>
</html>
"""


TITULOS = {
    1: ("30 años haciendo historia",
        "30 años formando generaciones, construyendo oportunidades"),
    2: ("Nuestra historia",
        "Tres décadas de transformación"),
    3: ("Voces que dejan huella",
        "Nuestra comunidad"),
    4: ("Orgullo CECyTEJ",
        "Logros, talento y proyectos"),
    5: ("Celebremos juntos",
        "30 años de orgullo y tradición"),
    6: ("Nuestro futuro",
        "Los próximos 30 años")
}


@app.route("/")
def inicio():
    return mostrar(1, 1)


@app.route("/pantalla/<int:numero>/<int:estilo>")
def pantalla(numero, estilo):
    return mostrar(numero, estilo)


def mostrar(numero, estilo):

    if numero not in TITULOS:
        numero = 1

    if estilo not in [1, 2]:
        estilo = 1

    return render_template_string(
        HTML,
        numero=numero,
        estilo=estilo,
        titulo=TITULOS[numero][0],
        subtitulo=TITULOS[numero][1]
    )


@app.route("/enviar", methods=["POST"])
def enviar():

    nombre = request.form.get("nombre", "")
    grupo = request.form.get("grupo", "")
    mensaje = request.form.get("mensaje", "")

    return render_template_string("""
    <!DOCTYPE html>
    <html lang="es">
    <head>
    <meta charset="UTF-8">
    <title>Mensaje enviado</title>
    <style>
    body {
        font-family: Arial;
        background: #eaf2e9;
        padding: 30px;
    }
    .caja {
        background: white;
        max-width: 550px;
        margin: auto;
        padding: 25px;
        border: 5px solid #075b3b;
        border-radius: 20px;
    }
    h1 { color: #075b3b; }
    a {
        display: inline-block;
        background: #075b3b;
        color: white;
        padding: 12px;
        text-decoration: none;
        border-radius: 15px;
    }
        .foto-generacion {
    width: 100%;
    max-width: 350px;
    height: 180px;
    object-fit: cover;
    border-radius: 12px;
    display: block;
    margin: 10px auto;
}
    
    </style>
    </head>
    <body>
    <div class="caja">
    <h1>¡Gracias por compartir tu mensaje!</h1>
    <p><b>Nombre:</b> {{ nombre }}</p>
    <p><b>Semestre y grupo:</b> {{ grupo }}</p>
    <p><b>Mensaje:</b> {{ mensaje }}</p>
    <p>Tu mensaje forma parte de nuestra celebración.</p>
    <p><small>Demostración escolar: los datos no se guardan permanentemente.</small></p>
    <a href="/pantalla/6/1">Regresar</a>
    </div>
    </body>
    </html>
    """, nombre=nombre, grupo=grupo, mensaje=mensaje)


if __name__ == "__main__":
    app.run(debug=True)