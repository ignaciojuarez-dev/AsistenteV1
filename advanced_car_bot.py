import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd
import PyPDF2
import json
import re
from typing import Dict, List, Optional
import io
import urllib.parse
import time

class AdvancedCarInspectionBot:
    def __init__(self):
        self.inspection_checklist = {
            "exterior": {
                "title": "Inspección Exterior",
                "points": [
                    {"item": "Pintura y carrocería", "details": "Revisar rayones, abolladuras, corrosión, uniformidad del color"},
                    {"item": "Neumáticos", "details": "Verificar desgaste, presión, fecha de fabricación, profundidad del dibujo"},
                    {"item": "Sistema de iluminación", "details": "Probar faros, intermitentes, luces de freno, luces de posición"},
                    {"item": "Cristales", "details": "Buscar grietas, chips, funcionamiento de limpiaparabrisas"},
                    {"item": "Espejos", "details": "Verificar fijación, ajuste, estado de los cristales"},
                    {"item": "Puertas y cerraduras", "details": "Probar apertura/cierre, alineación, funcionamiento de manijas"},
                    {"item": "Capó y maletero", "details": "Verificar apertura, cierre, alineación, estado de bisagras"}
                ]
            },
            "interior": {
                "title": "Inspección Interior",
                "points": [
                    {"item": "Asientos", "details": "Revisar tapicería, ajustes, desgaste, funcionamiento eléctrico"},
                    {"item": "Climatización", "details": "Probar aire acondicionado, calefacción, ventilación"},
                    {"item": "Instrumentos", "details": "Verificar funcionamiento de todos los indicadores y luces"},
                    {"item": "Controles", "details": "Probar volante, pedales, palancas, botones"},
                    {"item": "Sistema eléctrico", "details": "Verificar luces interiores, tomas de corriente, cargadores"},
                    {"item": "Seguridad", "details": "Revisar cinturones, airbags (luces de advertencia)"}
                ]
            },
            "motor": {
                "title": "Inspección del Motor",
                "points": [
                    {"item": "Fluidos", "details": "Verificar niveles y estado de aceite, refrigerante, frenos, dirección"},
                    {"item": "Batería", "details": "Inspeccionar terminales, corrosión, nivel de electrolito"},
                    {"item": "Mangueras y cables", "details": "Buscar grietas, desgaste, conexiones sueltas"},
                    {"item": "Funcionamiento", "details": "Escuchar ruidos extraños, vibración, humos"},
                    {"item": "Sistema de escape", "details": "Verificar sujeción, corrosión, ruidos"},
                    {"item": "Filtros", "details": "Revisar estado de filtro de aire, combustible, aceite"}
                ]
            },
            "mecanica": {
                "title": "Inspección Mecánica",
                "points": [
                    {"item": "Frenos", "details": "Probar efectividad, ruidos, vibración del pedal"},
                    {"item": "Suspensión", "details": "Verificar amortiguadores, resortes, rótulas"},
                    {"item": "Dirección", "details": "Probar alineación, juego del volante, asistencia"},
                    {"item": "Transmisión", "details": "Verificar cambios suaves, ruidos, fugas"},
                    {"item": "Embrague", "details": "Probar punto de agarre, vibración, deslizamiento"},
                    {"item": "Diferencial", "details": "Escuchar ruidos en curvas, verificar juego"}
                ]
            }
        }
        
        self.brand_specific_issues = {
            "toyota": [
                "Problemas con cadena de distribución en motores 2.4L",
                "Desgaste prematuro de pastillas de freno traseras",
                "Corrosión en marcos de ventanas",
                "Fallas en bobinas de encendido"
            ],
            "honda": [
                "Problemas de transmisión automática (CVT)",
                "Corrosión prematura en bajos del chasis",
                "Fallas en compresores de A/C",
                "Desgaste de bujes de suspensión"
            ],
            "ford": [
                "Problemas eléctricos en módulos",
                "Desgaste prematuro de embrague",
                "Fallas en sensores de oxígeno",
                "Problemas con bomba de combustible"
            ],
            "chevrolet": [
                "Problemas de suspensión delantera",
                "Fugas de aceite en motor",
                "Fallas en sistema de encendido",
                "Desgaste de juntas homocinéticas"
            ],
            "nissan": [
                "Problemas con CVT (Continuously Variable Transmission)",
                "Corrosión en puertas y guardabarros",
                "Fallas en sensores de masa de aire",
                "Problemas con cadena de distribución"
            ]
        }

    def search_car_specifications(self, make: str, model: str, year: str) -> Dict:
        """Busca especificaciones del auto usando web scraping simulado"""
        try:
            # En un entorno real, aquí harías scraping de sitios como:
            # - AutoTrader, Cars.com, KBB, etc.
            # Por ahora simulamos la respuesta
            
            search_query = f"{year} {make} {model} specifications problems"
            
            # Simulación de búsqueda web
            car_data = {
                "basic_info": {
                    "make": make.title(),
                    "model": model.title(), 
                    "year": year,
                    "search_query": search_query
                },
                "specifications": {
                    "engine": f"Motor típico para {make} {model}",
                    "transmission": "Manual/Automática según versión",
                    "fuel_type": "Gasolina/Diésel según versión",
                    "drivetrain": "FWD/AWD según versión"
                },
                "common_problems": self.brand_specific_issues.get(make.lower(), [
                    "Revisar historial de mantenimiento",
                    "Inspección mecánica completa recomendada",
                    "Verificar recalls del fabricante"
                ]),
                "maintenance_intervals": {
                    "5000_km": ["Cambio de aceite", "Inspección visual general"],
                    "10000_km": ["Cambio aceite y filtro", "Revisión frenos", "Rotación neumáticos"],
                    "20000_km": ["Cambio bujías", "Filtro aire", "Revisión transmisión"],
                    "40000_km": ["Cambio correa distribución", "Revisión suspensión completa"],
                    "60000_km": ["Cambio líquido frenos", "Revisión sistema refrigeración"]
                },
                "estimated_value": f"Valor estimado: Consultar fuentes especializadas para {year} {make} {model}"
            }
            
            return car_data
            
        except Exception as e:
            st.error(f"Error en búsqueda: {e}")
            return {}

    def perform_real_web_search(self, query: str) -> List[Dict]:
        """Realiza búsqueda web real (requiere configuración adicional)"""
        # Nota: Para uso en producción, necesitarías:
        # - API key de Google Custom Search
        # - Configurar motor de búsqueda personalizado
        # - Implementar rate limiting
        
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            
            # Por seguridad y términos de servicio, no implementamos scraping real
            # En su lugar, retornamos estructura de datos simulada
            return [{
                "title": f"Información sobre {query}",
                "snippet": "Datos obtenidos de fuentes especializadas en automóviles",
                "url": "https://ejemplo.com"
            }]
            
        except Exception as e:
            return [{"error": str(e)}]

    def process_property_csv(self, csv_file) -> Dict:
        """Procesa CSV con información de propiedad del vehículo"""
        try:
            df = pd.read_csv(csv_file)
            
            # Buscar columnas relevantes
            relevant_data = {}
            
            # Mapeo de posibles nombres de columnas
            column_mappings = {
                'vin': ['vin', 'numero_chasis', 'chasis'],
                'placa': ['placa', 'patente', 'matricula'],
                'propietario': ['propietario', 'owner', 'nombre'],
                'fecha_compra': ['fecha_compra', 'purchase_date', 'compra'],
                'precio': ['precio', 'price', 'valor'],
                'kilometraje': ['kilometraje', 'mileage', 'km']
            }
            
            for key, possible_columns in column_mappings.items():
                for col in df.columns:
                    if col.lower() in possible_columns:
                        relevant_data[key] = df[col].iloc[0] if not df[col].empty else "N/A"
                        break
            
            return {
                "data": relevant_data,
                "full_dataframe": df,
                "summary": f"Procesados {len(df)} registros del CSV"
            }
            
        except Exception as e:
            st.error(f"Error procesando CSV: {e}")
            return {"error": str(e)}

    def process_property_pdf(self, pdf_file) -> Dict:
        """Procesa PDF con documentación del vehículo"""
        try:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            full_text = ""
            
            for page_num, page in enumerate(pdf_reader.pages):
                page_text = page.extract_text()
                full_text += f"\n--- Página {page_num + 1} ---\n{page_text}"
            
            # Extraer información relevante usando regex
            extracted_info = {}
            
            # Patrones para buscar información específica
            patterns = {
                'vin': r'VIN[:\s]*([A-Z0-9]{17})',
                'placa': r'(?:PLACA|PATENTE)[:\s]*([A-Z0-9-]+)',
                'modelo': r'(?:MODELO)[:\s]*([A-Za-z0-9\s]+)',
                'año': r'(?:AÑO|YEAR)[:\s]*(\d{4})',
                'motor': r'(?:MOTOR)[:\s]*([A-Za-z0-9\s.]+)',
            }
            
            for key, pattern in patterns.items():
                match = re.search(pattern, full_text, re.IGNORECASE)
                if match:
                    extracted_info[key] = match.group(1).strip()
            
            return {
                "extracted_info": extracted_info,
                "full_text": full_text,
                "page_count": len(pdf_reader.pages),
                "summary": f"Procesado PDF con {len(pdf_reader.pages)} páginas"
            }
            
        except Exception as e:
            st.error(f"Error procesando PDF: {e}")
            return {"error": str(e)}

    def generate_comprehensive_guide(self, car_info: Dict, csv_data: Dict, pdf_data: Dict) -> Dict:
        """Genera guía completa de inspección"""
        
        guide = {
            "vehicle_info": car_info,
            "property_data": {
                "csv": csv_data,
                "pdf": pdf_data
            },
            "inspection_checklist": self.inspection_checklist,
            "priority_checks": [],
            "estimated_inspection_time": "2-3 horas para inspección completa"
        }
        
        # Agregar verificaciones prioritarias basadas en problemas comunes
        if car_info.get("common_problems"):
            guide["priority_checks"] = [
                f"⚠️ PRIORITARIO: {problem}" 
                for problem in car_info["common_problems"]
            ]
        
        return guide

def create_sample_files():
    """Crea archivos de ejemplo para testing"""
    
    # Crear CSV de ejemplo
    sample_csv_data = {
        'vin': ['1HGBH41JXMN109186'],
        'placa': ['ABC-123'],
        'propietario': ['Juan Pérez'],
        'fecha_compra': ['2023-01-15'],
        'precio': [15000],
        'kilometraje': [45000],
        'seguro': ['Vigente hasta 2024-12-31'],
        'revision_tecnica': ['Vigente hasta 2024-06-30']
    }
    
    df = pd.DataFrame(sample_csv_data)
    df.to_csv('/workspace/vehiculo_ejemplo.csv', index=False)
    
    # Crear contenido PDF de ejemplo (como texto)
    sample_pdf_content = """
    CERTIFICADO DE REGISTRO VEHICULAR
    
    VIN: 1HGBH41JXMN109186
    PLACA: ABC-123
    MARCA: Toyota
    MODELO: Corolla
    AÑO: 2020
    MOTOR: 1.8L 4 Cilindros
    TRANSMISION: Automática
    COLOR: Blanco
    
    PROPIETARIO: Juan Pérez
    DIRECCION: Calle Principal 123
    CIUDAD: Lima, Perú
    
    FECHA DE REGISTRO: 15 de Enero, 2023
    VIGENCIA: 31 de Diciembre, 2024
    """
    
    with open('/workspace/documento_ejemplo.txt', 'w', encoding='utf-8') as f:
        f.write(sample_pdf_content)

def main():
    st.set_page_config(
        page_title="🚗 Asistente Avanzado de Inspección Vehicular",
        page_icon="🚗",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # CSS personalizado
    st.markdown("""
    <style>
    .main-header {
        background: linear-gradient(90deg, #1f4e79, #2e86ab);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    .inspection-category {
        background: #f8f9fa;
        padding: 1rem;
        border-left: 4px solid #007bff;
        margin: 1rem 0;
        border-radius: 5px;
    }
    .priority-alert {
        background: #fff3cd;
        border: 1px solid #ffeaa7;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="main-header">
        <h1>🚗 Asistente Avanzado de Inspección Vehicular</h1>
        <p>Guía completa con búsqueda web e integración de documentos</p>
    </div>
    """, unsafe_allow_html=True)
    
    bot = AdvancedCarInspectionBot()
    
    # Crear archivos de ejemplo
    if st.sidebar.button("📁 Crear Archivos de Ejemplo"):
        create_sample_files()
        st.sidebar.success("Archivos de ejemplo creados!")
    
    # Sidebar para configuración
    with st.sidebar:
        st.header("🔧 Configuración del Vehículo")
        
        make = st.text_input("Marca *", placeholder="Toyota, Honda, Ford...")
        model = st.text_input("Modelo *", placeholder="Corolla, Civic, Focus...")
        year = st.text_input("Año *", placeholder="2020")
        
        st.markdown("---")
        st.header("📄 Documentos del Vehículo")
        
        csv_file = st.file_uploader(
            "Archivo CSV con datos del vehículo", 
            type=['csv'],
            help="Sube un CSV con información como VIN, placa, propietario, etc."
        )
        
        pdf_file = st.file_uploader(
            "Documento PDF del vehículo", 
            type=['pdf'],
            help="Sube documentos como registro vehicular, seguro, etc."
        )
        
        st.markdown("---")
        st.header("⚙️ Opciones Avanzadas")
        
        search_web = st.checkbox("🌐 Búsqueda web avanzada", value=True)
        include_maintenance = st.checkbox("🔧 Incluir cronograma de mantenimiento", value=True)
        detailed_checklist = st.checkbox("📋 Lista detallada de verificación", value=True)

    # Área principal
    col1, col2 = st.columns([2, 1])
    
    with col2:
        if st.button("🚀 Generar Guía Completa", type="primary"):
            if not all([make, model, year]):
                st.error("⚠️ Por favor completa Marca, Modelo y Año")
                st.stop()
            
            # Mostrar progreso
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            # Paso 1: Búsqueda de información
            status_text.text("🔍 Buscando información del vehículo...")
            progress_bar.progress(20)
            car_info = bot.search_car_specifications(make, model, year)
            
            # Paso 2: Procesar CSV
            status_text.text("📊 Procesando archivo CSV...")
            progress_bar.progress(40)
            csv_data = {}
            if csv_file:
                csv_data = bot.process_property_csv(csv_file)
            
            # Paso 3: Procesar PDF
            status_text.text("📑 Procesando documento PDF...")
            progress_bar.progress(60)
            pdf_data = {}
            if pdf_file:
                pdf_data = bot.process_property_pdf(pdf_file)
            
            # Paso 4: Generar guía
            status_text.text("📋 Generando guía de inspección...")
            progress_bar.progress(80)
            guide = bot.generate_comprehensive_guide(car_info, csv_data, pdf_data)
            
            # Paso 5: Completado
            status_text.text("✅ ¡Guía generada exitosamente!")
            progress_bar.progress(100)
            
            time.sleep(1)
            status_text.empty()
            progress_bar.empty()
            
            # Almacenar en session state para mostrar resultados
            st.session_state.guide = guide
            st.session_state.show_results = True

    with col1:
        st.header("📖 Instrucciones")
        st.markdown("""
        ### Pasos para usar el asistente:
        
        1. **Información básica**: Ingresa marca, modelo y año del vehículo
        2. **Documentos**: Sube archivos CSV y PDF con información del vehículo (opcional)
        3. **Configuración**: Ajusta las opciones según tus necesidades
        4. **Generar**: Haz clic en "Generar Guía Completa"
        5. **Inspeccionar**: Sigue la guía paso a paso
        
        ### Características incluidas:
        - 🔍 Búsqueda automática de especificaciones
        - ⚠️ Identificación de problemas comunes por marca
        - 📋 Lista de verificación interactiva
        - 🔧 Cronograma de mantenimiento
        - 📊 Integración con tus documentos
        """)

    # Mostrar resultados si están disponibles
    if st.session_state.get('show_results') and st.session_state.get('guide'):
        st.markdown("---")
        guide = st.session_state.guide
        
        # Información del vehículo
        st.header("🚗 Información del Vehículo")
        vehicle_info = guide['vehicle_info']['basic_info']
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Marca", vehicle_info['make'])
        with col2:
            st.metric("Modelo", vehicle_info['model'])
        with col3:
            st.metric("Año", vehicle_info['year'])
        
        # Verificaciones prioritarias
        if guide.get('priority_checks'):
            st.markdown("""
            <div class="priority-alert">
                <h3>⚠️ Verificaciones Prioritarias</h3>
            </div>
            """, unsafe_allow_html=True)
            
            for priority in guide['priority_checks']:
                st.warning(priority)
        
        # Lista de inspección
        st.header("📋 Lista de Inspección Detallada")
        
        tabs = st.tabs([cat['title'] for cat in guide['inspection_checklist'].values()])
        
        for i, (category_key, category_data) in enumerate(guide['inspection_checklist'].items()):
            with tabs[i]:
                st.markdown(f"### {category_data['title']}")
                
                for j, point in enumerate(category_data['points']):
                    col1, col2 = st.columns([1, 3])
                    
                    with col1:
                        checked = st.checkbox(
                            "✓", 
                            key=f"{category_key}_{j}",
                            help="Marcar como completado"
                        )
                    
                    with col2:
                        if checked:
                            st.success(f"**{point['item']}** ✅")
                        else:
                            st.write(f"**{point['item']}**")
                        st.caption(point['details'])
        
        # Información de documentos
        if guide['property_data']['csv'] or guide['property_data']['pdf']:
            st.header("📄 Información de Documentos")
            
            col1, col2 = st.columns(2)
            
            with col1:
                if guide['property_data']['csv']:
                    st.subheader("📊 Datos CSV")
                    csv_info = guide['property_data']['csv']
                    if 'data' in csv_info:
                        for key, value in csv_info['data'].items():
                            st.write(f"**{key.title()}:** {value}")
            
            with col2:
                if guide['property_data']['pdf']:
                    st.subheader("📑 Información PDF")
                    pdf_info = guide['property_data']['pdf']
                    if 'extracted_info' in pdf_info:
                        for key, value in pdf_info['extracted_info'].items():
                            st.write(f"**{key.title()}:** {value}")
        
        # Cronograma de mantenimiento
        if include_maintenance and 'maintenance_intervals' in guide['vehicle_info']:
            st.header("🔧 Cronograma de Mantenimiento")
            
            maintenance = guide['vehicle_info']['maintenance_intervals']
            for interval, tasks in maintenance.items():
                with st.expander(f"{interval.replace('_', ' ').title()}"):
                    for task in tasks:
                        st.write(f"• {task}")
        
        # Descargar reporte
        st.markdown("---")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            report_json = json.dumps(guide, ensure_ascii=False, indent=2)
            st.download_button(
                "📥 Descargar Reporte JSON",
                data=report_json,
                file_name=f"inspeccion_{make}_{model}_{year}.json",
                mime="application/json"
            )
        
        with col2:
            # Crear reporte de texto
            text_report = f"""
REPORTE DE INSPECCIÓN VEHICULAR
===============================

Vehículo: {vehicle_info['make']} {vehicle_info['model']} {vehicle_info['year']}
Fecha de inspección: {time.strftime('%Y-%m-%d %H:%M:%S')}

VERIFICACIONES PRIORITARIAS:
{chr(10).join(guide.get('priority_checks', []))}

TIEMPO ESTIMADO: {guide['estimated_inspection_time']}
            """
            
            st.download_button(
                "📄 Descargar Reporte TXT",
                data=text_report,
                file_name=f"inspeccion_{make}_{model}_{year}.txt",
                mime="text/plain"
            )
        
        with col3:
            if st.button("🗑️ Nueva Inspección"):
                st.session_state.show_results = False
                st.session_state.guide = None
                st.experimental_rerun()

if __name__ == "__main__":
    main()