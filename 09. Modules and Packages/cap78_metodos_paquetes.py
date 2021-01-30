# En esta leccion veremos como podemos crear nuestros propios modulos y paquetes
# veremos como personalizar nuestros modulos y paquetes.

# Tener en cuenta que los modulos son solo scripts .py que pueden ser llamados en otro script .py
# Y los pquetes son una coleccion de modulos

# Esto es interesante con programas muy largos con la intencion de modularizar y dividir el problema
# en parte mas pequeñas, con la intencion de luego crear un paquete

# ESTE ES MI PROGRAMA
# Imaginamos que este es el programa principal que quiero ejecutar del paquete que he creado con los scripts
# en la carpeta principal y subcarpeta

# Esta es la forma en la que se puede organizar no solo un unico directorio sino en subdirectorios
# Incluso solo se podrian importal funciones especificas

from paquete78 import some_main_script as p
from paquete78.Subpaquetes import mysubscript as s

p.main_report()
s.sub_report()

