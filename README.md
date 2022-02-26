# Proyecto Landing Page Django

## Consiste en una app construida en Django para el registro online de personas a un evento virtual sobre “cómo humanizar la experiencia del cliente en el nuevo entorno digital”
___ 

### Librerías utilizadas:
- PostgreSQL para la base de datos (psycopg2)
- Django environ para utilizar variables de entorno (django-environ)
- Heroku y Gunicorn para hacer el deploy (django-heroku, gunicorn)
- Se utilizo un módulo de Python para enviar un email de bienvenida a las personas que se registren al evento, con una cuenta de gmail creada para el proyecto, la cuenta de email se puede modificar desde el archivo .env EMAIL_ADDRESS (smtplib)
- 
> Todas la paginas son responsivas  

### Rutas:  

- `Principal o index` : página principal donde tenemos la información del evento y el formulario de registro, al registrarse la persona recibe un email de agradecimiento   

- `/lista_registrados` : ruta donde podemos ver la lista de personas registradas al evento, para ingresar es necesario iniciar sesión si no estamos logueados nos va a redireccionar a la ruta /login  

- `/registro` : esta ruta es una especie de registro secreto para poder acceder a la lista de las personas registradas, para registrarse debemos hacerlo desde la url: `/registro?username=<nombre-de-usuario>&password=<contraseña>&key=<clave-secreta>`  

Para este login se necesita una clave secreta que se puede establecer en las variables de entorno como REGISTRATION_KEY tambien podemos cambiar el email del cual se envian los emails con la variable EMAIL_PROVIDER  

- `/login` : para loguernos y ver la lista de participantes inscriptos  

---
## Para poder iniciar el proyecto desde otro pc debemos tener instalado:  

[GIT](https://git-scm.com/downloads)
[Python3](https://www.python.org/downloads/)  

> Clonar el repositorio con:
``` 
>> git clone <url>  
```

> Luego instalamos las dependencias:
``` 
>> pip install -r requirement.txt  
```

> Crear un archivo .env 

Dentro de la carpeta donde clonamos el repositorio tenemos un archivo .env_example el cual contiene que claves debemos tener para poder correr nuestro proyecto.  

(debemos crear o tener una SECRET KEY que se genera al crear un proyecto en Django)

> Una vez creado el archivo .env con los datos necesarios, realizamos las migraciones:
``` 
>> python manage.py makemigrations  
``` 

``` 
>> python manage.py migrate  
``` 

Luego podemos crear un superusuario para ingresar a la interfaz de administrador de django.  


Por último, ejecutamos:
``` 
>>  python manage.py runserver  
```
Y listo ya tenemos la app funcionando en nuestro localhost 🎉 

 