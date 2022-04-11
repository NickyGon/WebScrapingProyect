# WebScrapingProyect
## Introducción

Scraping es un término en inglés que, traducido, literalmente quiere decir “rascado”. Sin embargo, en un contexto de tecnología y análisis de información, se refiere a la limpieza y filtro de datos. Muchas veces, una sección relevante de información hacia un sector no está al alcance de un click en el Internet: existiendo restricciones del acceso a esta, o con un formato inentendible a primera vista y cambiante por cada página web que existe si se intenta inspeccionarla. Para solucionar este problema, se empezó a utilizar la técnica Web Scrapping, una clase de diversos métodos capaces de identificar y extraer datos escondidos en los documentos de especificación de la web, haciéndolos útiles para cualquier utilidad posible en otros entornos.

## Proyecto de Web Scraping con interfaz Django

En este proyecto se centraliza el uso de Web Scraping que según fuentes "El raspado web, la recolección web o la extracción de datos web es el raspado de datos que se utiliza para extraer datos de sitios web."

### Los requisitos para la ejecución del proyecto son:

### 1. Tener Python instalado (la mejor versión actualizada mejor).
### 2. Instalar Django (se puede usar la siguiente línea de código para ello en cuyo caso ya se tenga instalado pip que es lo mas recomendable)
```
pip install django
```
### 3. Ya teniendo las librerías necesarias instaladas, clonamos el repositorio del proyecto (trabajamos en master como main branch asi que clonamos el repositorio y hacemos un pull del branch o en su defecto clonamos el branch directamente).
#### comandos git para ello
```
git clone https://github.com/NickyGon/WebScrapingProyect.git                  <-- clona el repositorio
git clone --branch master https://github.com/NickyGon/WebScrapingProyect.git  <-- clona el repositorio pero del branch master específicamente
git pull --rebase origin master                                               <-- jala los datos del branch master despues de haber clonado el repositorio
```
### 4. Después de ya tener las librerías y el proyecto en nuestro IDE de confianza (en nuestro caso preferimos usar VSCode por la comodidad) podemos ejecutar primero el script de la carpeta "webscrapingscript" cuyo archivo es "scrap.py" (podemos usar el comando de la terminal)
```
>python scrap.py
```
### 5. Después nos generará un archivo tipo JSON que almacena todos los datos de la página https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38 \
el archivo se guardará como "cards.json". Este archivo es usado en el HTML "resultados.html" donde visualiza los datos extraidos de  dicha página
### 6. Ahora para ejecutar la página web de manera localhost en la terminal usamos el siguiente comando
```
>python manage.py runserver
```
(ojo, ejecutar dentro de la carpeta "webscrapingpc" donde se encuentra manage.py)
### 7. después de ejecutar el servidor nos mostrara la url del localhost (generalmente asignado a su ip local , ejemplo http://127.0.0.1:5500/)
### 8. Y ya se esta corriendo el localhosts, solo necesitamos entrar al url asignado (el ip) en nuestro navegador web y se verá la página ya creada
### 9. Para visualizar datos extraidos (el uso de web scraping soap) solo necesitamos buscar en la caja de texto lo que necesitamos, como por ejemplo "Asrock" y nos mostrará tarjetas de newegg de la marca Asrcok
