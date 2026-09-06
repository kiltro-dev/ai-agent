# Primeros pasos para crear agentes

Esta guia prepara el entorno del proyecto para trabajar con las herramientas del curso.

## 1. Crear el entorno virtual

El primer comando crea un entorno virtual llamado `.venv` para el proyecto.

```bash
python3 -m venv .venv
```

## 2. Activar el entorno virtual

Este comando activa el entorno virtual creado anteriormente.

```bash
source .venv/bin/activate
```

## 3. Actualizar pip

Este comando actualiza `pip`, la herramienta utilizada para instalar paquetes de Python.

```bash
python -m pip install --upgrade pip
```

## 4. Instalar las herramientas

Este comando instala las dependencias utilizadas en el proyecto.

```bash
pip install langchain langchain-huggingface transformers duckduckgo-search python-dotenv beautifulsoup4
```

## 5. Crear el archivo de configuración

Este comando crea el archivo `.env` con el valor de `HF_TOKEN`.

```bash
echo "HF_TOKEN=hf_token" > .env
```

## 6. Comprobar la instalación

Este comando comprueba que `langchain` y `transformers` se puedan importar correctamente.

```bash
python -c "import langchain, transformers; print('setup succesful!')"
```

## 7. Crear archivo de ejemplo para variables de entorno

Este archivo sirve como plantilla para que otros usuarios sepan qué variables configurar sin exponer valores reales.

```bash
echo "HF_TOKEN=hf_token" > .env.example
```

> `.env` contiene el token real y está ignorado por `.gitignore`. `.env.example` sí se versiona.

## 8. Inicializar repositorio Git

```bash
git init
git add .env.example .gitignore notes.md
git commit -m "feat: setup inicial con agentes, env example y notas"
```

## 9. Crear repositorio en GitHub y subir el código

Requiere `gh` autenticado y clave SSH configurada.

```bash
gh repo create ai-agent --public --source=. --remote=origin --push
# o si el repo ya existe:
# git remote add origin git@github.com:kiltro-dev/ai-agent.git
# git branch -M main
# git push -u origin main
```