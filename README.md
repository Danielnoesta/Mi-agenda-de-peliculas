# 🎬 Mi Agenda de Películas para la Semana de Receso

Este proyecto fue desarrollado como parte del **Nivel 2 del curso de Introducción a la Programación**. Consiste en una aplicación de consola que permite planear y gestionar una agenda de 5 películas para ver durante la semana de receso.

## 📌 Objetivo del Proyecto

Practicar y aplicar los conceptos aprendidos durante el nivel, incluyendo:

- Uso de funciones con parámetros y composición de funciones
- Técnica de **Dividir y Conquistar**
- Modularización del código
- Estructuras condicionales
- Uso de **diccionarios**
- Creación de una **interfaz de consola** amigable

---

## 🎯 Funcionalidades

La aplicación permite:

- ✅ Consultar la **película más larga**
- ✅ Calcular la **duración promedio** de las películas (formato `HH:MM`)
- ✅ Buscar películas estrenadas después de un año ingresado
- ✅ Contar cuántas películas son **clasificación 18+**
- ✅ **Reagendar** una película (cambiando el día y/o la hora)
- ✅ Decidir si se puede **invitar a un amigo o familiar** a ver una película, respetando reglas de edad y clasificación
- ✅ Salir del programa

---

## 🎞️ Representación de una Película

Cada película es un **diccionario** con las siguientes claves:

| Clave         | Descripción |
|---------------|-------------|
| `nombre`      | Nombre de la película |
| `genero`      | Géneros separados por coma (e.g., `"Drama, Comedia"`) |
| `anio`        | Año de estreno |
| `duracion`    | Duración en minutos |
| `clasificacion` | Clasificación por edad: `"todos"`, `"7+"`, `"13+"`, `"16+"`, `"18+"` |
| `dia`         | Día de la semana para verla |
| `hora`        | Hora en formato 24h (por ejemplo `2030` para 8:30 p.m.) |

---

## 📂 Estructura del Proyecto

```
N2-AgendaPeliculas/
│
├── modulo_peliculas.py      # Contiene la lógica principal de manejo de la agenda
├── consola_peliculas.py     # Interfaz de usuario basada en consola
├── README.md                # Este archivo
```

---

## ⚠️ Reglas de Validación

### Al reagendar:
- No deben solaparse horarios de películas el mismo día
- Se puede activar una validación adicional con preferencias como:
  - No ver Documentales después de las 10 p.m.
  - No ver Dramas los viernes
  - No ver películas en semana entre 11 p.m. y 6 a.m.

### Al invitar:
- Personas **mayores de edad** pueden ver cualquier película
- **Menores de 15** no pueden ver películas de **Terror**
- **Niños de 10 o menos** solo pueden ver películas de **género Familiar**
- Si la edad no cumple con la clasificación de la película, se requiere **permiso de los padres**, salvo que sea un **Documental**

---

## ▶️ Cómo Ejecutar

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/N2-AgendaPeliculas.git
   cd N2-AgendaPeliculas
   ```

2. Abre el proyecto en tu entorno de desarrollo preferido (como **Spyder**).

3. Ejecuta el archivo `consola_peliculas.py`.

---

## 📜 Créditos

Proyecto individual desarrollado por **Jerson Daniel Fandiño Bohorquez**, como parte del curso en Uniandes.  
Todos los derechos reservados para fines académicos.
