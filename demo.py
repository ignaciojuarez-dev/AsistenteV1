#!/usr/bin/env python3
"""
Demostración interactiva del Bot de Inspección Vehicular
"""

import json
import sys
import os

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def print_header():
    print("🚗" + "=" * 58 + "🚗")
    print("     ASISTENTE DE INSPECCIÓN VEHICULAR - DEMO")
    print("🚗" + "=" * 58 + "🚗")

def print_section(title):
    print(f"\n📋 {title}")
    print("-" * (len(title) + 4))

class DemoCarInspectionBot:
    def __init__(self):
        self.inspection_checklist = {
            "exterior": {
                "title": "🚗 Inspección Exterior",
                "items": [
                    "Pintura y carrocería (rayones, abolladuras, corrosión)",
                    "Neumáticos (desgaste, presión, profundidad del dibujo)",
                    "Sistema de iluminación (faros, intermitentes, frenos)",
                    "Cristales (grietas, chips, limpiaparabrisas)",
                    "Espejos retrovisores (fijación, ajuste)",
                    "Puertas y cerraduras (funcionamiento, alineación)"
                ]
            },
            "interior": {
                "title": "🏠 Inspección Interior",
                "items": [
                    "Asientos y tapicería (desgaste, ajustes)",
                    "Climatización (A/C, calefacción, ventilación)",
                    "Instrumentos (funcionamiento de indicadores)",
                    "Controles (volante, pedales, palancas)",
                    "Sistema eléctrico (luces, tomas, cargadores)",
                    "Seguridad (cinturones, airbags)"
                ]
            },
            "motor": {
                "title": "🔧 Inspección del Motor",
                "items": [
                    "Niveles de fluidos (aceite, refrigerante, frenos)",
                    "Batería (terminales, corrosión, nivel)",
                    "Mangueras y cables (grietas, conexiones)",
                    "Funcionamiento (ruidos, vibración, humos)",
                    "Sistema de escape (sujeción, corrosión)",
                    "Filtros (aire, combustible, aceite)"
                ]
            },
            "mecanica": {
                "title": "⚙️ Inspección Mecánica",
                "items": [
                    "Sistema de frenos (efectividad, ruidos)",
                    "Suspensión (amortiguadores, resortes)",
                    "Dirección (alineación, asistencia)",
                    "Transmisión (cambios, ruidos, fugas)",
                    "Embrague (punto de agarre, deslizamiento)",
                    "Diferencial (ruidos en curvas)"
                ]
            }
        }
        
        self.brand_database = {
            "toyota": {
                "problems": [
                    "Problemas con cadena de distribución en motores 2.4L",
                    "Desgaste prematuro de pastillas de freno traseras",
                    "Corrosión en marcos de ventanas",
                    "Fallas en bobinas de encendido"
                ],
                "tips": [
                    "Cambiar aceite cada 5,000 km",
                    "Revisar cadena de distribución cada 100,000 km"
                ]
            },
            "honda": {
                "problems": [
                    "Problemas de transmisión CVT",
                    "Corrosión en bajos del chasis",
                    "Fallas en compresores de A/C"
                ],
                "tips": [
                    "Cambiar líquido CVT cada 40,000 km",
                    "Aplicar tratamiento anticorrosivo"
                ]
            },
            "ford": {
                "problems": [
                    "Problemas eléctricos en módulos",
                    "Desgaste prematuro de embrague",
                    "Fallas en sensores de oxígeno"
                ],
                "tips": [
                    "Revisar sistema eléctrico cada 30,000 km",
                    "Usar repuestos originales"
                ]
            }
        }

    def get_vehicle_info(self, make, model, year):
        brand_info = self.brand_database.get(make.lower(), {
            "problems": ["Revisar historial de mantenimiento", "Inspección profesional recomendada"],
            "tips": ["Seguir cronograma del fabricante", "Usar repuestos de calidad"]
        })
        
        return {
            "make": make.title(),
            "model": model.title(),
            "year": year,
            "common_problems": brand_info["problems"],
            "maintenance_tips": brand_info["tips"]
        }

    def interactive_inspection(self, vehicle_info):
        print_section("INSPECCIÓN INTERACTIVA")
        print(f"Vehículo: {vehicle_info['year']} {vehicle_info['make']} {vehicle_info['model']}")
        
        total_items = sum(len(cat["items"]) for cat in self.inspection_checklist.values())
        completed_items = 0
        
        for category_key, category in self.inspection_checklist.items():
            print(f"\n{category['title']}")
            print("=" * len(category['title']))
            
            for i, item in enumerate(category["items"], 1):
                print(f"\n{i}. {item}")
                
                while True:
                    response = input("   ✅ Completado? (s/n/info): ").lower().strip()
                    
                    if response in ['s', 'si', 'y', 'yes']:
                        print("   ✅ Marcado como completado")
                        completed_items += 1
                        break
                    elif response in ['n', 'no']:
                        print("   ⏳ Pendiente de completar")
                        break
                    elif response == 'info':
                        self.show_item_details(item)
                    else:
                        print("   Por favor responde 's' (sí), 'n' (no) o 'info' (más información)")
            
            progress = (completed_items / total_items) * 100
            print(f"\n📊 Progreso: {completed_items}/{total_items} ({progress:.1f}%)")
            
            if category_key != list(self.inspection_checklist.keys())[-1]:
                input("\nPresiona Enter para continuar con la siguiente sección...")
        
        return completed_items, total_items

    def show_item_details(self, item):
        details = {
            "Pintura y carrocería": "Buscar rayones profundos, abolladuras, óxido, diferencias de color que indiquen reparaciones",
            "Neumáticos": "Verificar desgaste uniforme, profundidad mínima 1.6mm, presión según especificaciones",
            "Sistema de iluminación": "Probar todas las luces: faros altos/bajos, intermitentes, frenos, reversa",
            "Niveles de fluidos": "Verificar aceite motor, refrigerante, líquido frenos, dirección asistida",
            "Sistema de frenos": "Probar efectividad, escuchar ruidos, verificar que no tire hacia un lado"
        }
        
        for key, detail in details.items():
            if key.lower() in item.lower():
                print(f"   ℹ️  {detail}")
                return
        
        print(f"   ℹ️  Revisar cuidadosamente: {item}")

def main():
    clear_screen()
    print_header()
    
    bot = DemoCarInspectionBot()
    
    # Entrada de datos del vehículo
    print("\n📝 INFORMACIÓN DEL VEHÍCULO")
    print("-" * 30)
    
    while True:
        make = input("Marca del vehículo: ").strip()
        if make:
            break
        print("Por favor ingresa la marca del vehículo")
    
    while True:
        model = input("Modelo del vehículo: ").strip()
        if model:
            break
        print("Por favor ingresa el modelo del vehículo")
    
    while True:
        year = input("Año del vehículo: ").strip()
        if year and year.isdigit() and 1900 <= int(year) <= 2025:
            break
        print("Por favor ingresa un año válido (1900-2025)")
    
    # Obtener información del vehículo
    vehicle_info = bot.get_vehicle_info(make, model, year)
    
    clear_screen()
    print_header()
    
    # Mostrar información del vehículo
    print_section("INFORMACIÓN DEL VEHÍCULO")
    print(f"Marca: {vehicle_info['make']}")
    print(f"Modelo: {vehicle_info['model']}")
    print(f"Año: {vehicle_info['year']}")
    
    # Mostrar problemas comunes
    print_section("⚠️ PROBLEMAS COMUNES A REVISAR")
    for i, problem in enumerate(vehicle_info['common_problems'], 1):
        print(f"{i}. {problem}")
    
    # Mostrar consejos de mantenimiento
    print_section("🔧 CONSEJOS DE MANTENIMIENTO")
    for i, tip in enumerate(vehicle_info['maintenance_tips'], 1):
        print(f"{i}. {tip}")
    
    input("\nPresiona Enter para comenzar la inspección...")
    
    # Realizar inspección interactiva
    clear_screen()
    print_header()
    
    completed, total = bot.interactive_inspection(vehicle_info)
    
    # Mostrar resultados finales
    clear_screen()
    print_header()
    
    print_section("📊 RESULTADO DE LA INSPECCIÓN")
    
    percentage = (completed / total) * 100
    print(f"Puntos completados: {completed}/{total} ({percentage:.1f}%)")
    
    if percentage == 100:
        print("🎉 ¡INSPECCIÓN COMPLETA! El vehículo ha sido revisado exhaustivamente.")
    elif percentage >= 80:
        print("✅ Inspección mayormente completa. Revisar puntos pendientes.")
    elif percentage >= 60:
        print("⚠️ Inspección parcial. Se recomienda completar más puntos.")
    else:
        print("❌ Inspección insuficiente. Se requiere revisión más detallada.")
    
    print(f"\n📋 Resumen para: {vehicle_info['year']} {vehicle_info['make']} {vehicle_info['model']}")
    print(f"Fecha de inspección: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Generar reporte
    report = {
        "vehicle": vehicle_info,
        "inspection_date": __import__('datetime').datetime.now().isoformat(),
        "completed_items": completed,
        "total_items": total,
        "completion_percentage": percentage
    }
    
    save_report = input("\n¿Deseas guardar el reporte? (s/n): ").lower().strip()
    if save_report in ['s', 'si', 'y', 'yes']:
        filename = f"inspeccion_{make}_{model}_{year}.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
        print(f"✅ Reporte guardado como: {filename}")
    
    print("\n🚗 ¡Gracias por usar el Asistente de Inspección Vehicular!")
    print("Recuerda: Una inspección regular mantiene tu vehículo seguro y confiable.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Inspección cancelada por el usuario.")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error durante la inspección: {e}")
        sys.exit(1)