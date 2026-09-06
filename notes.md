# Primeros pasos para crear agentes

Guía profesional para el entorno del proyecto usando **uv** (gestor moderno de Python) + `pyproject.toml`. Reemplaza el flujo clásico `pip + requirements.txt`.

> **Stack elegido (2026):** `uv` de Astral — 10-100x más rápido que pip, gestiona Python, venv y dependencias con `pyproject.toml` + `uv.lock` reproducible. Alternativas clásicas: Poetry, PDM, Hatch.

## Prerequisitos

Instalar `uv` (una vez por máquina):

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
# o
pipx install uv
uv --version
```

## 1. Crear el entorno virtual

`uv` crea `.venv` automáticamente con la versión pineada en `.python-version`:

```bash
uv venv          # crea .venv con Python 3.12 (definido en .python-version)
# o explícito: uv venv --python 3.12
```

> Antes (pip): `python3 -m venv .venv` — ahora `uv` lo gestiona.

## 2. Activar el entorno virtual

```bash
source .venv/bin/activate
```

## 3. Sincronizar dependencias

Las **dependencias directas** están en `pyproject.toml:7` (solo 6 que tú eliges). Las **transitivas** (71 paquetes) quedan congeladas en `uv.lock`.

```bash
uv sync                 # instala todo lo de pyproject.toml + uv.lock en .venv
uv sync --group dev     # incluye herramientas de desarrollo (pytest, ruff)
```

Para quien clona el repo por primera vez:

```bash
git clone git@github.com:kiltro-dev/ai-agent.git
cd ai-agent
uv sync
cp .env.example .env  # y editar HF_TOKEN
```

## 4. Añadir / actualizar librerías

**No uses `pip install` suelto.** Usa `uv add` — actualiza `pyproject.toml` y regenera `uv.lock` automáticamente:

```bash
uv add requests                 # prod
uv add --dev pytest ruff        # solo dev (va a [dependency-groups].dev en pyproject.toml:16)
uv add "langchain>=1.5"         # con restricción de versión
uv remove duckduckgo-search     # eliminar
uv lock --upgrade               # actualizar todas las transitivas a último compatible
uv lock --upgrade-package transformers  # actualizar solo una
```

Flujo tras añadir:

```bash
git add pyproject.toml uv.lock
git commit -m "feat: añade requests"
git push
# otros hacen: uv sync  -> quedan idénticos
```

> **¿Por qué `requirements.txt` tenía 64 líneas?** `pip freeze` vuelca transitivas (`langchain` → `langchain-core` → `langsmith` → `orjson`...). Con `uv` ves solo 6 directas en `pyproject.toml`, el `uv.lock` guarda las 71 exactas para reproducibilidad.

## 5. Crear el archivo de configuración

```bash
echo "HF_TOKEN=hf_token" > .env
```

## 6. Comprobar la instalación

```bash
uv run python -c "import langchain, transformers; print('setup successful!')"
# o con venv activo:
python -c "import langchain, transformers; print('setup successful!')"
```

## 7. Crear archivo de ejemplo para variables de entorno

Plantilla versionada para otros usuarios:

```bash
echo "HF_TOKEN=hf_token" > .env.example
```

> `.env` con token real está ignorado en `.gitignore:2`. `.env.example` sí se versiona.

## 8. Inicializar repositorio Git

```bash
git init
git add pyproject.toml uv.lock .python-version .env.example .gitignore notes.md ai_agent/
git commit -m "feat: setup inicial con uv, pyproject y notas"
```

## 9. Crear repositorio en GitHub y subir el código

Requiere `gh` autenticado y SSH:

```bash
gh repo create ai-agent --public --source=. --remote=origin --push
# si ya existe:
# git remote add origin git@github.com:kiltro-dev/ai-agent.git
# git branch -M main
# git push -u origin main
```

Para cambios posteriores:

```bash
git add pyproject.toml uv.lock
git commit -m "chore: bump deps"
git push
```

## Apéndice: Estructura profesional

```
ai-agent/
├── pyproject.toml      # directas (6) + metadatos + config ruff/pytest
├── uv.lock             # 71 paquetes exactos (commit siempre)
├── .python-version     # 3.12 pineado
├── .venv/              # ignorado (.gitignore:1)
├── .env / .env.example
├── ai_agent/__init__.py
└── notes.md
```

**Migración desde pip:** se eliminó `requirements.txt` (reemplazado por `pyproject.toml` + `uv.lock`). Si necesitas compatibilidad legacy: `uv pip compile pyproject.toml -o requirements.txt`.
