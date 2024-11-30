# InstagramConDjango  

Este proyecto es una implementación básica de una aplicación similar a Instagram, desarrollada con el framework **Django**. Incluye funcionalidades básicas como la gestión de perfiles, publicaciones y vistas personalizadas, utilizando vistas basadas en clases (Class-Based Views).

---

## Estructura del Proyecto  

El proyecto está organizado en las siguientes carpetas principales:  

- **instagram/**  
  Contiene los templates HTML utilizados para renderizar las vistas, vistas, modelos y urls generales.  
- **posts/**  
  Gestor de publicaciones. Incluye modelos y vistas relacionadas con las publicaciones de los usuarios.  
- **profiles/**  
  Gestión de perfiles de usuario. Incluye modelos y vistas para manejar los datos y la información de los usuarios.  

---

## Requisitos  

Asegúrate de tener instalado lo siguiente:  

- Python 3.8 o superior  
- Django 4.0 o superior  
- SQLite (configuración predeterminada para la base de datos)  

Para instalar las dependencias del proyecto:  

```bash
pip install -r requirements.txt
```

---

## Instalación y Configuración

### Clona el repositorio:
```bash
git clone https://github.com/tu_usuario/InstagramConDjango.git
cd InstagramConDjango
```
###Crea y aplica migraciones:
```bash
python manage.py makemigrations
python manage.py migrate
```
### Crea un superusuario:
```bash
python manage.py createsuperuser
```
### Inicia el servidor de desarrollo:
```bash
python manage.py runserver
```
Accede a la aplicación en tu navegador: http://127.0.0.1:8000/

---

## Funcionalidades

### Gestión de perfiles de usuario:

- Registro de nuevos usuarios.
- Inicio y cierre de sesión.
- Actualización y edición de información personal.

### Publicaciones:

- Creación de nuevas publicaciones.
- Edición y eliminación de publicaciones existentes.
- Visualización de publicaciones en un feed dinámico.

### Interacciones:

- Sistema de "me gusta" para las publicaciones.
- Comentarios en publicaciones.

### Vistas basadas en clases:

- Organización del código para facilitar la reutilización y legibilidad.

---

## Tests
Este proyecto incluye tests para garantizar el correcto funcionamiento de las funcionalidades principales.

### Ejecución de Tests
Para ejecutar los tests, utiliza el siguiente comando:
```bash
python manage.py test
```
Se probarán los modelos, vistas y funcionalidades principales de la aplicación.

---

## Licencia
Este proyecto está licenciado bajo la MIT License. Puedes consultar más detalles en el archivo LICENSE.

---

## Contacto
Si tienes dudas o sugerencias, no dudes en contactarme:

Email: mariafrenchitas@gmail.com
GitHub: Frenchitas
