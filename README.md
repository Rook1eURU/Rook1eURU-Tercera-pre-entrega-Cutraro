# Pre-entrega 3 | Leonardo Cutraro | Musicy
v1.0 - 06/03/2024

**Admin login:**
Name: Rookmin |
Pass: pyton1234r

**Descripción:**
El proyecto consiste en una página web de nombre *Musicy* en la cual los usuarios pueden buscar traducciones de las letras de distintas canciones. En la versión final, cada canción tendrá su propia página, con información relevante, un video de youtube, y la letra tanto original como traducida al idioma deseado. Si una canción, artista, álbum o género no existe en la BD, el usuario lo podrá ingresar junto a la información necesaria. Por el momento, sólo es posible añadir manualmente a cada canción, artista, álbum o género.

**Funcionalidades:**
El proyecto cuenta con 4 módulos (* indica características por añadir):

- Canción
    - Título
    - Artista
    - Álbum
    - Año
    - Género
    - Video de YouTube*
    - Letra original*
    - Traducción*
- Artista
    - Nombre
    - Canciones
    - Álbumes
- Álbum
    - Título
    - Artista
    - Año
    - Género
    - Canciones
    - Imágen*
    - Productora*
- Género
    - Nombre
    - Canciones

Cada uno de estos módulos puede accederse desde las pestañas que se encuentran en la parte superior derecha de la pantalla. Esto llevará al usuario a una página donde podran buscar en las bases de datos de distintos módulos, o crear una nueva entrada en cualquiera de ellas. A su vez, hay una página principal que puede accederse dando click en el nombre de la página, en la parte superior izquierda.

Seleccionar pestaña de módulo a probar > Dar click en el botón "¿Añadir?" para crear una instancia > Llenar el formulario > En la página del módulo, escribir en el buscador el nombre de la instancia creada (primer casilla del formulario)

A su vez, en la versión final del programa, los módulos se relacionarán entre si, creando nuevas instancias que se ramifiquen de nuevas entradas en los otros módulos. Por ejemplo al ingresar una canción con un Artista que no esté en la BD, se ingresará el mismo en esta, sin la necesidad de ingresarlo manualmente. Si se ingresa una canción con un artista ya existente, la canción se añadirá a la lista de canciones de dicho Artista.
