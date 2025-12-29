# Chat con LLaMA – v1
## Primera versión publicada de una GUI local para ejecutar modelos LLM


## ¿Qué es esto?

Esta aplicación es la primera versión publicada de una interfaz gráfica
para ejecutar un modelo de IA local desde mi propio equipo.

No representa el primer intento absoluto, sino la primera versión
funcional completa que se conservó y decidió publicarse.

## ¿Por qué existe?

En el momento en que se creó esta app, mi hardware no podía ejecutar las aplicaciones habituales para trabajar con modelos de lenguaje.

Quería comprobar si era posible:

usar un modelo local,

sin depender de la nube,

sin conocimientos de programación,

y sin aplicaciones pesadas.

Esta ventana fue la respuesta a esa pregunta.

## ¿Qué hace?

Abre una interfaz gráfica sencilla.

Permite escribir un mensaje.

Ejecuta un modelo local mediante llama.cpp.

Muestra la respuesta del modelo en pantalla.

Nada más.
Y deliberadamente, nada más.

## ¿Qué no hace (a propósito)?

No guarda historial de conversaciones.

No permite cambiar el modelo desde la interfaz.

No permite detener la generación.

No gestiona configuraciones avanzadas.

Estas funciones se intentaron más adelante, pero aquí se conservó el código que sí funcionaba, sin forzarlo.

## Lecciones aprendidas

Una interfaz gráfica se rompe fácilmente si se añaden demasiadas cosas a la vez.

Volver al código que funciona es a veces la mejor decisión.

No todo debe resolverse en la primera versión.

## Estado del proyecto

Esta versión se conserva como un punto de partida histórico.
No se ha modernizado ni refactorizado deliberadamente.

Cualquier mejora posterior pertenece a versiones siguientes.

## Apéndice técnico (breve)

Lenguaje: Python

Interfaz: Tkinter

Ejecución del modelo: llama-run

Rutas al ejecutable y al modelo fijadas manualmente.

Codificación forzada a UTF-8.

## Agradecimientos

Este proyecto no existiría sin:

llama.cpp y su ecosistema de modelos GGUF.

Los modelos de lenguaje de código abierto que permiten experimentar en local.

Los asistentes de IA utilizados como apoyo durante el aprendizaje.

### Sobre esta versión

Aunque se publica como v1, esta aplicación corresponde a una etapa
temprana del proyecto (aproximadamente una versión 0.x).

Existieron versiones previas aún más simples que no se conservan.
Esta es la primera que funciona de forma estable y se mantiene como
referencia histórica.

- La salida del modelo puede incluir caracteres de control propios
  del uso en terminal (por ejemplo, secuencias ANSI).

### Uso básico

Esta aplicación no es plug & play.
Asume que el usuario tiene un entorno local mínimo configurado.

## Requisitos

Python 3

llama.cpp compilado localmente

Un modelo GGUF compatible

## Preparación

Antes de ejecutar la aplicación, es necesario editar el archivo
gui_antiguo.py y ajustar manualmente estas rutas:

llama_executable = "/ruta/a/llama.cpp/build/bin/llama-run"
model_path = "/ruta/a/tu_modelo.gguf"


Estas rutas dependen del sistema y de cómo se haya compilado
llama.cpp.

## Ejecución

Una vez ajustadas las rutas:

python3 gui_antiguo.py


La aplicación abrirá una ventana desde la que se puede enviar texto
al modelo local y recibir la respuesta.

### Este proyecto prioriza cerrar ciclos y conservar versiones funcionales
frente a seguir añadiendo complejidad.