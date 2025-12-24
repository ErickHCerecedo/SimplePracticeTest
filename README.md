# SimplePractice Test Automation

Framework de automatización de pruebas para SimplePractice usando Selenium y pytest.

## Configuración

### Variables de Entorno

Para mayor seguridad, las credenciales se pueden configurar mediante variables de entorno:

#### Windows (PowerShell)
```powershell
$env:SP_USERNAME="your_email@example.com"
$env:SP_PASSWORD="your_password"
```

#### Windows (CMD)
```cmd
set SP_USERNAME=your_email@example.com
set SP_PASSWORD=your_password
```

#### Linux/Mac
```bash
export SP_USERNAME="your_email@example.com"
export SP_PASSWORD="your_password"
```

#### Usando archivo .env (opcional)

Si prefieres usar un archivo `.env`, puedes instalar `python-dotenv`:

```bash
pip install python-dotenv
```

Y crear un archivo `.env` en la raíz del proyecto:

```
SP_USERNAME=your_email@example.com
SP_PASSWORD=your_password
```

**Nota:** El archivo `.env` está en `.gitignore` y no se subirá al repositorio.

## Ejecución de Tests

```bash
# Ejecutar todos los tests
pytest

# Ejecutar tests específicos
pytest tests/test_login.py
pytest tests/test_tasks.py

# Ejecutar con marcadores
pytest -m positive
pytest -m negative

# Ejecutar con navegador específico
pytest --browser=chrome
pytest --browser=firefox

# Ejecutar con salida detallada
pytest -v -s
```

## Estructura del Proyecto

```
SimplePracticeTest/
├── pages/          # Page Object Models
├── tests/          # Test cases
├── utils/          # Utilidades
└── reports/        # Reportes de tests
```
