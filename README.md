# 🎬 Catálogo de Películas

Programa de consola en Python para administrar un catálogo personal de películas, desarrollado aplicando **Programación Orientada a Objetos (POO)**.

> Mini proyecto 3 — Opción A: Catálogo de películas

## ✨ Funcionalidades

1. Agregar película (validando que el código no se repita)
2. Mostrar el catálogo completo
3. Buscar película por código
4. Buscar película por título (búsqueda parcial, sin distinguir mayúsculas)
5. Marcar película como vista
6. Mostrar películas por género
7. Mostrar películas pendientes
8. Mostrar estadísticas del catálogo
9. Eliminar película
0. Salir

### 📊 Estadísticas incluidas
- Cantidad total de películas
- Películas vistas y pendientes
- Promedio de duración
- Película más larga
- Cantidad de películas por género

## 🧱 Estructura del código

### Clase `Pelicula`
Representa una película con sus datos:

| Atributo        | Descripción                                   |
|-----------------|-----------------------------------------------|
| `codigo`        | Identificador único (ej. `P01`)               |
| `titulo`        | Título de la película                         |
| `genero`        | Género (Acción, Comedia, Animación...)        |
| `_duracion`     | Duración en minutos (atributo **protegido**)  |
| `clasificacion` | Clasificación por edad (ej. `+12`)            |
| `vista`         | `True` si ya se vio, `False` si está pendiente |

Métodos principales: `get_duracion()`, `set_duracion()`, `validar_duracion()`, `marcar_vista()`, `mostrar_info()` y `__str__()`.

### Clase `Catalogo`
Administra una lista de objetos `Pelicula` y ofrece métodos para agregar, buscar, filtrar, eliminar y calcular estadísticas.

### Funciones auxiliares
- `pedir_texto()` — evita que se ingresen datos vacíos.
- `pedir_entero()` — valida que se ingrese un número entero mayor que 0, usando `try/except` para que el programa no se caiga.

## 💡 Conceptos de POO aplicados
- **Clases y objetos:** `Pelicula` y `Catalogo`.
- **Encapsulamiento:** la duración es un atributo protegido (`_duracion`) que se modifica mediante métodos *get* y *set* con validación.
- **Composición:** el `Catalogo` contiene una lista de objetos `Pelicula`.
- **Método especial `__str__`:** para mostrar la información de cada película de forma legible.

## ▶️ Cómo ejecutarlo

Requisitos: **Python 3.6 o superior** (usa f-strings). No necesita librerías externas.

```bash
git clone https://github.com/RTXCARLOS/Catalogo-de-peliculas.git
cd Catalogo-de-peliculas
python Tarea_CatalogoPeliculas.py
```

## 🎞️ Películas precargadas

| Código | Título             | Género    | Duración | Clasificación | Estado    |
|--------|--------------------|-----------|----------|---------------|-----------|
| P01    | Iron Man           | Acción    | 126 min  | +12           | Vista     |
| P02    | Spider-Man         | Acción    | 121 min  | +12           | Vista     |
| P03    | Avengers: Endgame  | Acción    | 181 min  | +12           | Pendiente |
| P04    | Coyote vs. Acme    | Comedia   | 101 min  | Todo público  | Pendiente |
| P05    | Toy Story          | Animación | 81 min   | Todo público  | Vista     |

## 🖥️ Ejemplo de uso

```
========== CATÁLOGO DE PELÍCULAS ==========
1. Agregar película
2. Mostrar catálogo completo
3. Buscar película por código
4. Buscar película por título
5. Marcar película como vista
6. Mostrar películas por género
7. Mostrar películas pendientes
8. Mostrar estadísticas del catálogo
9. Eliminar película
0. Salir
Elige una opción: 8

-----Estadísticas del catálogo-----
Cantidad total de películas: 5
Películas vistas: 3
Películas pendientes: 2
Promedio de duración: 122.00 min
Película más larga: Avengers: Endgame (181 min)
Películas por género:
  - Acción: 3
  - Comedia: 1
  - Animación: 1
```

## 👤 Autor

**RTXCARLOS** — [github.com/RTXCARLOS](https://github.com/RTXCARLOS)
