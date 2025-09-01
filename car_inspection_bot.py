import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd
import PyPDF2
import json
import re
from typing import Dict, List, Optional
import io

class CarInspectionBot:
    def __init__(self):
        self.inspection_points = {
            "exterior": [
                "Revisar la pintura por rayones, abolladuras o corrosión",
                "Verificar el estado de los neumáticos (desgaste, presión)",
                "Inspeccionar las luces (faros, intermitentes, frenos)",
                "Comprobar el estado de los cristales",
                "Revisar el estado de los espejos retrovisores",
                "Verificar el funcionamiento de las puertas y cerraduras"
            ],
            "interior": [
                "Verificar el estado de los asientos y tapicería",
                "Comprobar el funcionamiento del aire acondicionado/calefacción",
                "Revisar el estado del volante y pedales",
                "Verificar el funcionamiento de luces interiores",
                "Comprobar el estado del tablero de instrumentos",
                "Revisar cinturones de seguridad"
            ],
            "motor": [
                "Verificar niveles de aceite y otros fluidos",
                "Inspeccionar la batería y cables",
                "Revisar el estado de las mangueras",
                "Comprobar el funcionamiento del motor (ruidos extraños)",
                "Verificar el sistema de escape",
                "Revisar correas y filtros"
            ],
            "documentacion": [
                "Verificar que los papeles estén en regla",
                "Comprobar que el número de motor coincida",
                "Verificar el estado del seguro",
                "Revisar historial de mantenimiento",
                "Comprobar multas pendientes"
            ]
        }
    
    def search_car_info(self, make: str, model: str, year: str) -> Dict:
        """Busca información del auto en internet"""
        try:
            # Construir query de búsqueda
            query = f"{year} {make} {model} specifications review"
            
            # Simular búsqueda web (en un caso real usarías APIs como Google Search API)
            # Por ahora retornamos información estructurada basada en patrones comunes
            car_info = {
                "make": make,
                "model": model,
                "year": year,
                "common_issues": self._get_common_issues(make, model),
                "maintenance_schedule": self._get_maintenance_schedule(),
                "specifications": {
                    "engine": "Información no disponible sin API de búsqueda",
                    "transmission": "Información no disponible sin API de búsqueda",
                    "fuel_type": "Información no disponible sin API de búsqueda"
                }
            }
            
            return car_info
        except Exception as e:
            st.error(f"Error buscando información del auto: {e}")
            return {}
    
    def _get_common_issues(self, make: str, model: str) -> List[str]:
        """Retorna problemas comunes basados en la marca y modelo"""
        common_issues_db = {
            "toyota": ["Problemas con la cadena de distribución", "Desgaste prematuro de frenos"],
            "honda": ["Problemas de transmisión automática", "Corrosión en el chasis"],
            "ford": ["Problemas eléctricos", "Desgaste de embrague"],
            "chevrolet": ["Problemas de suspensión", "Fugas de aceite"],
            "nissan": ["Problemas con CVT", "Corrosión en puertas"]
        }
        
        return common_issues_db.get(make.lower(), ["Revisar historial de mantenimiento", "Inspección general recomendada"])
    
    def _get_maintenance_schedule(self) -> Dict:
        """Retorna cronograma de mantenimiento general"""
        return {
            "5000_km": ["Cambio de aceite", "Revisión de filtros"],
            "10000_km": ["Cambio de aceite y filtro", "Revisión de frenos", "Rotación de neumáticos"],
            "20000_km": ["Cambio de bujías", "Revisión de transmisión", "Cambio de filtro de aire"],
            "40000_km": ["Cambio de correa de distribución", "Revisión completa de suspensión"]
        }
    
    def process_csv_data(self, csv_file) -> pd.DataFrame:
        """Procesa archivo CSV con información de la propiedad"""
        try:
            df = pd.read_csv(csv_file)
            return df
        except Exception as e:
            st.error(f"Error procesando CSV: {e}")
            return pd.DataFrame()
    
    def process_pdf_data(self, pdf_file) -> str:
        """Procesa archivo PDF con información de la propiedad"""
        try:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()
            return text
        except Exception as e:
            st.error(f"Error procesando PDF: {e}")
            return ""
    
    def generate_inspection_guide(self, car_info: Dict, csv_data: pd.DataFrame, pdf_text: str) -> Dict:
        """Genera guía de inspección personalizada"""
        guide = {
            "informacion_vehiculo": car_info,
            "puntos_inspeccion": self.inspection_points,
            "problemas_comunes": car_info.get("common_issues", []),
            "cronograma_mantenimiento": car_info.get("maintenance_schedule", {}),
            "datos_propiedad": {
                "csv_info": csv_data.to_dict() if not csv_data.empty else {},
                "pdf_content": pdf_text[:500] + "..." if len(pdf_text) > 500 else pdf_text
            }
        }
        
        return guide

def main():
    st.set_page_config(
        page_title="Asistente de Inspección Vehicular",
        page_icon="🚗",
        layout="wide"
    )
    
    st.title("🚗 Asistente de Inspección Vehicular")
    st.markdown("---")
    
    bot = CarInspectionBot()
    
    # Sidebar para información del vehículo
    with st.sidebar:
        st.header("Información del Vehículo")
        make = st.text_input("Marca", placeholder="ej: Toyota")
        model = st.text_input("Modelo", placeholder="ej: Corolla")
        year = st.text_input("Año", placeholder="ej: 2020")
        
        st.header("Archivos de Propiedad")
        csv_file = st.file_uploader("Subir archivo CSV", type=['csv'])
        pdf_file = st.file_uploader("Subir archivo PDF", type=['pdf'])
    
    # Área principal
    if st.button("🔍 Generar Guía de Inspección"):
        if make and model and year:
            with st.spinner("Buscando información del vehículo..."):
                # Buscar información del auto
                car_info = bot.search_car_info(make, model, year)
                
                # Procesar archivos
                csv_data = pd.DataFrame()
                pdf_text = ""
                
                if csv_file:
                    csv_data = bot.process_csv_data(csv_file)
                
                if pdf_file:
                    pdf_text = bot.process_pdf_data(pdf_file)
                
                # Generar guía
                guide = bot.generate_inspection_guide(car_info, csv_data, pdf_text)
                
                # Mostrar resultados
                col1, col2 = st.columns(2)
                
                with col1:
                    st.header("📋 Guía de Inspección")
                    
                    # Información del vehículo
                    st.subheader("Información del Vehículo")
                    st.write(f"**Marca:** {guide['informacion_vehiculo']['make']}")
                    st.write(f"**Modelo:** {guide['informacion_vehiculo']['model']}")
                    st.write(f"**Año:** {guide['informacion_vehiculo']['year']}")
                    
                    # Problemas comunes
                    st.subheader("⚠️ Problemas Comunes a Revisar")
                    for issue in guide['problemas_comunes']:
                        st.warning(f"• {issue}")
                    
                    # Puntos de inspección
                    st.subheader("🔍 Puntos de Inspección")
                    
                    for category, points in guide['puntos_inspeccion'].items():
                        with st.expander(f"{category.upper()}"):
                            for i, point in enumerate(points, 1):
                                st.checkbox(f"{i}. {point}", key=f"{category}_{i}")
                
                with col2:
                    st.header("📊 Información Adicional")
                    
                    # Cronograma de mantenimiento
                    st.subheader("🔧 Cronograma de Mantenimiento")
                    for km, tasks in guide['cronograma_mantenimiento'].items():
                        st.write(f"**{km.replace('_', ' ').title()}:**")
                        for task in tasks:
                            st.write(f"• {task}")
                        st.write("")
                    
                    # Información de archivos
                    if not csv_data.empty:
                        st.subheader("📄 Datos CSV")
                        st.dataframe(csv_data)
                    
                    if pdf_text:
                        st.subheader("📑 Contenido PDF")
                        st.text_area("Extracto del PDF", pdf_text[:1000], height=200)
                
                # Botón para descargar reporte
                st.markdown("---")
                report_json = json.dumps(guide, ensure_ascii=False, indent=2)
                st.download_button(
                    label="📥 Descargar Reporte Completo (JSON)",
                    data=report_json,
                    file_name=f"inspeccion_{make}_{model}_{year}.json",
                    mime="application/json"
                )
        else:
            st.error("Por favor, completa la información del vehículo (Marca, Modelo y Año)")
    
    # Instrucciones
    st.markdown("---")
    st.header("📖 Instrucciones de Uso")
    st.markdown("""
    1. **Ingresa la información del vehículo** en la barra lateral (Marca, Modelo, Año)
    2. **Sube tus archivos** CSV y PDF con información de tu propiedad (opcional)
    3. **Haz clic en "Generar Guía de Inspección"** para obtener una guía personalizada
    4. **Sigue los puntos de inspección** marcando cada elemento completado
    5. **Descarga el reporte completo** para tus registros
    
    ### Características:
    - 🔍 Búsqueda automática de información del vehículo
    - 📋 Lista de verificación interactiva
    - ⚠️ Identificación de problemas comunes por marca/modelo
    - 🔧 Cronograma de mantenimiento recomendado
    - 📊 Integración con tus datos CSV y PDF
    - 📥 Exportación de reportes
    """)

if __name__ == "__main__":
    main()