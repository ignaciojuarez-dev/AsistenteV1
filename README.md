# 🚗 Asistente de Inspección Vehicular

Un bot inteligente que te guía paso a paso en la inspección de automóviles, integrando búsqueda web de información vehicular y procesamiento de documentos CSV/PDF.

## 🌟 Características Principales

- **🔍 Búsqueda Inteligente**: Obtiene información específica del vehículo basada en marca, modelo y año
- **📋 Guía Paso a Paso**: Lista de verificación detallada para inspección completa
- **⚠️ Problemas Comunes**: Identifica issues típicos por marca y modelo
- **📊 Integración de Documentos**: Procesa archivos CSV y PDF con información del vehículo
- **🔧 Cronograma de Mantenimiento**: Recomendaciones basadas en kilometraje
- **📱 Interfaz Moderna**: Aplicación web interactiva con Streamlit

## 📁 Estructura del Proyecto

```
/workspace/
├── car_inspection_bot.py          # Bot básico de inspección
├── advanced_car_bot.py            # Bot avanzado con interfaz completa
├── web_search_integration.py      # Módulo de búsqueda web
├── requirements.txt               # Dependencias del proyecto
├── vehiculo_ejemplo.csv          # Archivo CSV de ejemplo
├── documento_ejemplo.txt         # Documento de ejemplo
└── README.md                     # Este archivo
```

## 🚀 Instalación y Uso

### 1. Instalar Dependencias

```bash
pip install -r requirements.txt
```

### 2. Ejecutar la Aplicación

#### Versión Básica:
```bash
streamlit run car_inspection_bot.py
```

#### Versión Avanzada (Recomendada):
```bash
streamlit run advanced_car_bot.py
```

### 3. Usar la Aplicación

1. **Información del Vehículo**: Ingresa marca, modelo y año
2. **Subir Documentos**: Opcionalmente sube archivos CSV/PDF
3. **Generar Guía**: Haz clic en "Generar Guía de Inspección"
4. **Seguir Checklist**: Marca cada punto completado
5. **Descargar Reporte**: Guarda el reporte para tus registros

## 📊 Formato de Archivos

### CSV de Ejemplo
```csv
vin,placa,propietario,fecha_compra,precio,kilometraje,seguro,revision_tecnica
1HGBH41JXMN109186,ABC-123,Juan Pérez,2023-01-15,15000,45000,Vigente hasta 2024-12-31,Vigente hasta 2024-06-30
```

### Campos Reconocidos en CSV:
- `vin` / `numero_chasis` / `chasis`
- `placa` / `patente` / `matricula`
- `propietario` / `owner` / `nombre`
- `fecha_compra` / `purchase_date` / `compra`
- `precio` / `price` / `valor`
- `kilometraje` / `mileage` / `km`

### PDF Soportado
El bot puede extraer información de documentos PDF como:
- Certificados de registro vehicular
- Documentos de seguro
- Historiales de mantenimiento
- Facturas de compra

## 🔍 Puntos de Inspección

### Exterior
- Pintura y carrocería
- Neumáticos y llantas
- Sistema de iluminación
- Cristales y espejos
- Puertas y cerraduras

### Interior
- Asientos y tapicería
- Sistema de climatización
- Instrumentos y controles
- Sistema eléctrico
- Elementos de seguridad

### Motor
- Niveles de fluidos
- Batería y cables
- Mangueras y conexiones
- Funcionamiento general
- Sistema de escape

### Mecánica
- Sistema de frenos
- Suspensión y dirección
- Transmisión
- Diferencial

## 🛠️ Personalización

### Agregar Nuevas Marcas
Edita el archivo `web_search_integration.py` y añade información en `known_issues_db`:

```python
"nueva_marca": {
    "common_problems": [
        "Problema específico 1",
        "Problema específico 2"
    ],
    "maintenance_tips": [
        "Consejo de mantenimiento 1",
        "Consejo de mantenimiento 2"
    ]
}
```

### Modificar Puntos de Inspección
En `advanced_car_bot.py`, edita el diccionario `inspection_checklist` para agregar o modificar categorías y puntos de verificación.

## 🌐 Integración Web Real

Para usar búsqueda web real en producción:

1. **Google Custom Search API**:
   ```python
   # Obtener API key de Google Cloud Console
   # Configurar motor de búsqueda personalizado
   ```

2. **Bing Search API**:
   ```python
   # Obtener API key de Microsoft Azure
   # Implementar búsqueda con Bing
   ```

3. **APIs Especializadas**:
   - Edmunds API
   - KBB API
   - AutoTrader API

## 📋 Lista de Verificación de Desarrollo

- [x] ✅ Bot básico de inspección
- [x] ✅ Interfaz web con Streamlit
- [x] ✅ Procesamiento de archivos CSV/PDF
- [x] ✅ Base de datos de problemas comunes
- [x] ✅ Cronograma de mantenimiento
- [x] ✅ Sistema de reportes
- [ ] 🔄 Integración con APIs de búsqueda reales
- [ ] 🔄 Base de datos persistente
- [ ] 🔄 Autenticación de usuarios
- [ ] 🔄 Historial de inspecciones

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver `LICENSE` para más detalles.

## 🆘 Soporte

Si tienes problemas o preguntas:

1. Revisa la documentación
2. Verifica que todas las dependencias estén instaladas
3. Asegúrate de usar Python 3.7+
4. Consulta los archivos de ejemplo incluidos

## 🔮 Roadmap Futuro

- **v2.0**: Integración con APIs de valuación vehicular
- **v2.1**: Sistema de notificaciones de mantenimiento
- **v2.2**: Integración con talleres mecánicos
- **v2.3**: App móvil nativa
- **v3.0**: IA para diagnóstico predictivo

---

**Desarrollado con ❤️ para facilitar las inspecciones vehiculares**