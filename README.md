# Colors-api
Api para proveer acceso fácil a los colores dentro de una organización.

## Instalación
Instalar con pip
```
$ pip install -r requirements.txt
```

## Estructura de la aplicación
```
Controllers - carpeta con archivo para ruta como en este caso registro_color.py
templates - carpeta con html para renderizar en navegador
.gitignore - para especificar archivos que debiera ignorar git
colors.csv - archivo original con los colores
Dockerfile - instrucciones para un contenedor de Docker
LICENSE - licencia de código libre
app.py - archivo principal para correr la aplicación
save_colors_in_db.py - archivo para crear la base de datos local
see_db.py - archivo para ver el contenido de la base de datos local
```

## Ejecución de la aplicación

### Ejecutar en desarrollo
Se puede utilizar la base de datos del proyecto directamente o se puede crear localmente.
Si se decide utilizar la base ya existente:
En /colors-api

```
$ python app.py
```

Si se decide crear de nuevo la base de datos:
```
$ python save_colors_in_db.py
$ python see_db.py
$ python app.py
```

La aplicación aparecerá en la dirección http://localhost:5000/.

La ruta http://localhost:5000/colores muestra en un json todos los colores de la base de datos.

La ruta http://localhost:5000/colores/:id muestra en un json un solo recurso de acuerdo al ID que se especifica.

La ruta http://localhost:5000/registro_color tiene método GET que muestra que el proyecto está corrienod correctamente
y un método POST el cual requiere un json con los campos name (string), year (int), color (string) y pantone (string).
Este registro agrega el color a la base de datos. Se puede probar con una herramienta como Postman.



### Ejecutar en Docker
```
$ docker build -t colors-api .
```

```
$ docker run -p 5000:5000 --name colors-api 
```

## Github

```
https://github.com/Alejandro13Lecter/colors-api.git
```


