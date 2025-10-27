# GitHub Actions Demo

Este repositorio es un proyecto de demostración para explorar y aprender las capacidades de GitHub Actions.

## 🎯 Objetivo

Demostrar diferentes tipos de workflows y actions personalizadas que se pueden crear con GitHub Actions, desde ejemplos básicos hasta implementaciones más complejas.

## 📋 Contenido

### Workflows

- **Hello World** - Workflow básico que imprime mensajes de bienvenida
- **Test Composite Action** - Workflow que prueba nuestra action personalizada de saludo

### Actions Personalizadas

#### Greet and Show Repo Info
Una composite action que:
- Saluda personalizadamente con nombre y emoji
- Muestra información del repositorio (branch, commit, actor, etc.)
- Muestra fecha y hora de ejecución
- Proporciona outputs reutilizables

#### Update README Date
Una composite action que:
- Actualiza automáticamente la fecha de última modificación
- Usa `awk` para actualizar secciones específicas del README

#### Generate Random ASCII Art
Una composite action que:
- Usa `actions/setup-python@v5` para configurar Python
- Instala la librería `art` usando pip
- Genera arte ASCII aleatorio usando diferentes textos y fuentes
- Puede generar arte predefinido (café, perro, gato, mariposa) o texto estilizado
- Actualiza el README con el arte generado dinámicamente

## 🚀 Cómo usar

Todas las actions se ejecutan automáticamente en cada push o pull request a la rama `main`. También puedes ejecutarlas manualmente desde la pestaña Actions.

## 📊 Estado del Proyecto

- ✅ Workflow básico implementado
- ✅ Composite action de saludo implementado
- 🔄 En desarrollo: Más examples y casos de uso

## 🎨 Arte ASCII Dinámico

Cada vez que se ejecuta el workflow, se genera un patrón aleatorio diferente:

<!-- ASCII_ART_START -->
```
Generado: 2025-10-27 21:56:42 UTC
Tipo: text2art(Art, font=block)


 .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. |
| |      __      | || |  _______     | || |  _________   | |
| |     /       | || | |_   __     | || | |  _   _  |  | |
| |    / /     | || |   | |__) |   | || | |_/ | | _|  | |
| |   / ____    | || |   |  __ /    | || |     | |      | |
| | _/ /     _ | || |  _| |   _  | || |    _| |_     | |
| ||____|  |____|| || | |____| |___| | || |   |_____|    | |
| |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------' 
```
<!-- ASCII_ART_END -->

## 📅 Última actualización

<!-- LAST_UPDATE_START -->
Última actualización: 2025-10-27 21:21:16 UTC
<!-- LAST_UPDATE_END -->

---

Creado como proyecto de aprendizaje de GitHub Actions
