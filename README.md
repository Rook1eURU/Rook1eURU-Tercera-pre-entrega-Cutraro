# Proyecto Final CODERHOUSE | Leonardo Cutraro | Musicy
v1.1 - 23/03/2024

**Descripción:**
El proyecto consiste en una página web de nombre *Musicy* en la cual los usuarios pueden buscar traducciones de las letras de distintas canciones. Cada canción cuenta con su propia página con información relevante, un video de youtube, y la letra tanto original como traducida (por el momento, entre Español e Inglés). Si una canción, artista, álbum o género no existe en la BD, el usuario lo podrá ingresar junto a la información necesaria.

**Video Introducción:**
https://drive.google.com/file/d/1vSTRIShUeQK6ZYIp37oJ_SPMKCaMDS7-/view?usp=sharing

**SETUP Y USO:**
1. Descargar el repositorio en formato zip
2. Extraer y abrir con Visual Studio Code o el IDE de preferencia
3. En la consola, dirigirse a la carpeta Musicy con el comando ``cd Musicy`` e ingresar el comando ``python manage.py runserver``
4. El comando devolverá un link. Copiar el link, pegarlo en tu navegador y añadir al final ``/AppMusicy/``
5. Crea una cuenta utilizando el botón de Registrarse. La cuenta de correo puede ser falsa.
6. Inicia sesión con la cuenta que acabas de crear.
7. Una vez dentro de la página, podrás ver todos los módulos en forma de pestaña arriba a la derecha
8. Selecciona la pestaña de módulo a probar
9. Da click en el botón "¿Añadir?" para crear una instancia
10. Llena el formulario
11. En la página del módulo, escribe en el buscador el nombre de la instancia creada (primer casilla del formulario)
12. Repite para cuantos módulos sean necesarios

**Admin login:**
``Name: Rookmin |
Pass: pyton1234r``

**Funcionalidades:**
El proyecto cuenta con 4 módulos (* indica características por añadir):

- Canción
    - Título
    - Artista
    - Álbum
    - Año
    - Género
    - Video de YouTube
    - Letra original
    - Traducción
- Artista
    - Nombre
- Álbum
    - Título
    - Artista
    - Año
    - Canciones*
    - Imágen*
    - Productora*
- Género
    - Nombre
    - Canciones*

Cada uno de estos módulos puede accederse desde las pestañas que se encuentran en la parte superior derecha de la pantalla. Esto llevará al usuario a una página donde podran buscar en las bases de datos de distintos módulos, o crear una nueva entrada en cualquiera de ellas. A su vez, hay una página principal que puede accederse dando click en el nombre de la página, en la parte superior izquierda.
