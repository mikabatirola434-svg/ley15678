
# Actividad 10 - Ley 15.678

## Datos del proyecto

- **Materia:** Laboratorio de Programación (LPR)
- **Curso:** 5° año
- **Estudiante:** Mikaela Batirola
- **Docente:** Yamil Ganduglia y Mansilla Muñoz York Elías
- **Lenguaje:** Python
- **Versión:** 1.0.0
- **Año:** 2026

## Descripción

Este proyecto consiste en desarrollar un simulador que representa las condiciones para el uso de celulares dentro del aula, tomando como referencia la Ley 15.678.

El programa evalúa si existe autorización del docente para utilizar el celular con fines pedagógicos o si se presenta una emergencia familiar. Si ninguna de estas condiciones se cumple, indica que el dispositivo debe permanecer guardado.

## Estructura del repositorio

```text
ley15678/
├── .gitignore
├── LICENSE
├── README.md
├── src/
│   └── ley_celulares.py
├── docs/
│   └── InformeEEST1_LPR2026_ACT10_Batirola_v1.0.0.pdf
└── capturas/
    ├── ejecucion_false.png
    └── ejecucion_true.png
```

## Funcionamiento

El programa utiliza una estructura condicional `if`, `elif` y `else` para evaluar tres situaciones:

1. Si el docente autoriza el uso del celular con fines pedagógicos, se permite utilizarlo.
2. Si existe una emergencia familiar, la comunicación se gestiona mediante preceptoría o dirección.
3. Si ninguna condición se cumple, el celular debe permanecer guardado en la mochila.

## Ejecución

Para ejecutar el programa:

1. Abrir el repositorio en Visual Studio Code.
2. Ingresar a la carpeta `src`.
3. Abrir el archivo `ley_celulares.py`.
4. Ejecutarlo utilizando Python.

## Historial de versiones

- **v1.0.0 - 23/11/2026:** creación del simulador y documentación inicial.
