[English](README.md) | Español

# Laboratorio de Sistemas de Control

Experimentos mínimos que ilustran el control por retroalimentación y la dinámica de sistemas en sistemas de control.

Este repositorio explora simulaciones sencillas del comportamiento de sistemas de control, comunes en robótica, automatización y sistemas ciberfísicos.

Los ejemplos demuestran cómo los mecanismos de control por retroalimentación pueden regular el comportamiento del sistema y mantener la estabilidad en entornos dinámicos.

## Contenido

El directorio `src/` contiene tres experimentos mínimos:

* `pid_controller_sim.py`

    Implementa un controlador proporcional-integral-derivativo (PID) simple que regula un sistema simulado.

* `system_response_sim.py`

    Demuestra la respuesta a un escalón de un sistema dinámico simple.

* `feedback_control_demo.py`

    Simula el control por retroalimentación de lazo cerrado que regula un sistema hacia un valor objetivo.

## Propósito

Estos experimentos ilustran conceptos de ingeniería relevantes para:

* Ingeniería de sistemas de control
* Control por retroalimentación
* Arquitecturas de control robótico
* Sistemas ciberfísicos

## Motivación

Los sistemas de control son fundamentales para la robótica, la automatización y los sistemas mecatrónicos.

La mayoría de las máquinas reales dependen de mecanismos de control por retroalimentación para regular el movimiento, mantener la estabilidad y responder a perturbaciones.

Comprender cómo se comportan los sistemas dinámicos bajo control por retroalimentación es esencial para diseñar sistemas ciberfísicos fiables.

## Método

El repositorio implementa simulaciones simplificadas del comportamiento de los sistemas de control.

Los experimentos incluyen:

* Control PID para regular la salida del sistema
* Respuesta dinámica del sistema a entradas escalonadas
* Control por retroalimentación de lazo cerrado

Estas implementaciones son intencionadamente minimalistas y se centran en ilustrar el comportamiento conceptual de los sistemas de control por retroalimentación, en lugar de implementar implementaciones completas de control industrial.

## Ejecutando los ejemplos

Clonar el repositorio y ejecutar cualquiera de los scripts:

```bash
git clone https://github.com/Jorge-de-la-Flor/control-systems-lab
cd control-systems-lab
python src/pid_controller_sim.py
```

Cada script simula el comportamiento del sistema e imprime el proceso de control resultante en la consola.

## Árbol del proyecto

```bash
control-systems-lab
├─ .python-version
├─ LICENSE
├─ README.es.md
├─ README.md
├─ pyproject.toml
├─ src
│ ├─ feedback_control_demo.py
│ ├─ pid_controller_sim.py
│ └─ system_response_sim.py
└─ uv.lock
```

## Requisitos

Los ejemplos usan:

* Python 3.12+
* NumPy
* Matplotlib

## Instalación

Instalar las dependencias necesarias:

* using `pip`

```bash
pip install numpy matplotlib
```

* usando `uv`

```bash
uv agrega numpy matplotlib
```

## Referencias

* Åström, K. J. y Murray, R. M. (2008).
*Sistemas de retroalimentación.*

* Ogata, K. (2010).
*Ingeniería de control moderna.*