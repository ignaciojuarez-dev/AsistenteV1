# 🚗 Guía de Instalación - Asistente de Inspección Vehicular

## 📋 Requisitos del Sistema

- **Python 3.7+** (recomendado Python 3.8 o superior)
- **Sistema Operativo**: Linux, macOS, Windows
- **Espacio en disco**: ~50MB para dependencias
- **Conexión a internet**: Para búsqueda web (opcional)

## 🚀 Instalación Rápida

### Opción 1: Instalación con Virtual Environment (Recomendado)

```bash
# 1. Clonar o descargar el proyecto
cd /workspace

# 2. Crear entorno virtual
python3 -m venv car_inspection_env

# 3. Activar entorno virtual
# En Linux/macOS:
source car_inspection_env/bin/activate
# En Windows:
car_inspection_env\Scripts\activate

# 4. Instalar dependencias
pip install -r requirements.txt

# 5. Ejecutar la aplicación
streamlit run advanced_car_bot.py
```

### Opción 2: Instalación con pipx (Alternativa)

```bash
# Instalar pipx si no lo tienes
python3 -m pip install --user pipx
python3 -m pipx ensurepath

# Instalar streamlit con pipx
pipx install streamlit

# Instalar otras dependencias
pip install --user requests beautifulsoup4 pandas PyPDF2
```

### Opción 3: Demo Sin Dependencias Externas

```bash
# Ejecutar demo interactivo (no requiere instalación adicional)
python3 demo.py

# Ejecutar pruebas básicas
python3 simple_test.py
```

## 🛠️ Configuración

### 1. Archivos de Ejemplo
El sistema incluye archivos de ejemplo para probar:
- `vehiculo_ejemplo.csv` - Datos del vehículo
- `documento_ejemplo.txt` - Documento de registro

### 2. Estructura de Archivos CSV
Tu archivo CSV debe incluir columnas como:
```csv
vin,placa,propietario,fecha_compra,precio,kilometraje,seguro,revision_tecnica
1HGBH41JXMN109186,ABC-123,Juan Pérez,2023-01-15,15000,45000,Vigente,Vigente
```

### 3. Documentos PDF Soportados
- Certificados de registro vehicular
- Documentos de seguro
- Historiales de mantenimiento
- Facturas de compra

## 📱 Formas de Uso

### 1. Aplicación Web Completa
```bash
streamlit run advanced_car_bot.py
```
- Interfaz gráfica completa
- Carga de archivos CSV/PDF
- Búsqueda web simulada
- Reportes descargables

### 2. Aplicación Web Básica
```bash
streamlit run car_inspection_bot.py
```
- Interfaz simplificada
- Funcionalidad core
- Ideal para pruebas rápidas

### 3. Demo Interactivo (Terminal)
```bash
python3 demo.py
```
- Experiencia paso a paso
- No requiere navegador web
- Ideal para demostraciones

### 4. Pruebas Automatizadas
```bash
python3 simple_test.py
```
- Verificación de funcionalidad
- Pruebas de todos los componentes
- Diagnóstico de problemas

## 🔧 Configuración Avanzada

### Integración con APIs Reales

Para usar búsqueda web real, edita `web_search_integration.py`:

```python
# Google Custom Search API
GOOGLE_API_KEY = "tu_api_key_aqui"
SEARCH_ENGINE_ID = "tu_search_engine_id"

# Bing Search API
BING_API_KEY = "tu_bing_api_key"
```

### Personalización de Marcas

Agrega nuevas marcas en `web_search_integration.py`:

```python
"nueva_marca": {
    "common_problems": [
        "Problema específico 1",
        "Problema específico 2"
    ],
    "maintenance_tips": [
        "Consejo 1",
        "Consejo 2"
    ]
}
```

## 🐛 Solución de Problemas

### Error: "ModuleNotFoundError"
```bash
# Instalar dependencia faltante
pip install nombre_del_modulo

# O reinstalar todas las dependencias
pip install -r requirements.txt
```

### Error: "externally-managed-environment"
```bash
# Usar entorno virtual
python3 -m venv car_inspection_env
source car_inspection_env/bin/activate
pip install -r requirements.txt
```

### Error: "streamlit: command not found"
```bash
# Verificar instalación
pip show streamlit

# Reinstalar si es necesario
pip install streamlit
```

### Problemas con PDF
```bash
# Instalar dependencias adicionales para PDF
pip install PyPDF2 pdfplumber
```

## 📊 Verificación de Instalación

Ejecuta este comando para verificar que todo funciona:

```bash
python3 -c "
import sys
print('Python version:', sys.version)

try:
    import streamlit
    print('✅ Streamlit:', streamlit.__version__)
except ImportError:
    print('❌ Streamlit no instalado')

try:
    import pandas
    print('✅ Pandas:', pandas.__version__)
except ImportError:
    print('❌ Pandas no instalado')

try:
    import requests
    print('✅ Requests disponible')
except ImportError:
    print('⚠️ Requests no disponible (búsqueda web limitada)')

print('\\n🚗 Sistema listo para inspecciones vehiculares!')
"
```

## 🚀 Inicio Rápido

1. **Abrir la aplicación**:
   ```bash
   streamlit run advanced_car_bot.py
   ```

2. **En el navegador** (se abre automáticamente):
   - Ingresa marca, modelo y año del vehículo
   - Sube archivos CSV/PDF (opcional)
   - Haz clic en "Generar Guía Completa"

3. **Seguir la inspección**:
   - Marca cada punto completado
   - Revisa problemas específicos de la marca
   - Descarga el reporte final

## 📞 Soporte

Si tienes problemas:

1. **Revisa los logs**:
   ```bash
   streamlit run advanced_car_bot.py --logger.level debug
   ```

2. **Ejecuta las pruebas**:
   ```bash
   python3 simple_test.py
   ```

3. **Verifica dependencias**:
   ```bash
   pip list | grep -E "(streamlit|pandas|requests)"
   ```

## 🎯 Próximos Pasos

Una vez instalado, puedes:
- Personalizar las listas de inspección
- Agregar nuevas marcas de vehículos
- Integrar con APIs de búsqueda reales
- Crear bases de datos personalizadas
- Desarrollar funcionalidades adicionales

¡Disfruta inspeccionando vehículos de manera profesional! 🚗✨