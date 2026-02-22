def generar_perfil_profesional() -> None:
    """
    Genera e imprime el perfil profesional actualizado a Julio 2026.
    Muestra datos de contacto, roles y stack tecnológico clasificado.
    """
    # --- DATOS PERSONALES ---
    nombre: str = "Rodrigo García Pérez"
    rol_principal: str = "Data Engineer & IT Project Manager"
    
    contacto: dict = {
        "Email": "Rodrigo-gp95@hotmail.com",
        "Teléfono": "+525578218631",
        "LinkedIn": "linkedin.com/in/rodrigo-garcia-perez-",
        "Ubicación": "Chimalhuacán, Estado de México"
    }

    # --- HABILIDADES TÉCNICAS ---
    habilidades: dict = {
        "⚙️ Lenguajes y Bases de Datos": [
            "SQL Avanzado (Window Functions, CTEs)", 
            "Python (requests, pandas, boto3)", 
            "PostgreSQL"
        ],
        "☁️ Cloud & DevOps (AWS)": [
            "AWS (IAM, S3, EC2, RDS, Lambda, API Gateway)", 
            "Docker", 
            "Terraform (IaC)", 
            "CI/CD con GitHub Actions"
        ],
        "🏗️ Modern Data Stack": [
            "Apache Airflow (Orquestación)", 
            "dbt (Transformación)", 
            "Amazon Redshift (Data Warehousing)"
        ],
        "📊 Gestión y Arquitectura": [
            "Metodología PMBOK", 
            "Modelado y optimización de datos", 
            "Documentación técnica",
            "Dashboards ejecutivos"
        ]
    }

    # --- GENERACIÓN DEL REPORTE EN CONSOLA ---
    print("\n" + "="*50)
    print(f"👨‍💻 {nombre} | {rol_principal}")
    print("="*50)
    
    print("\n📍 Información de Contacto:")
    print(f"   ✉️ {contacto['Email']} | 📞 {contacto['Teléfono']}")
    print(f"   🌐 {contacto['LinkedIn']} | 🏠 {contacto['Ubicación']}")
    
    print("\n🚀 Stack Tecnológico y Competencias:")
    for categoria, herramientas in habilidades.items():
        print(f"\n  {categoria}:")
        for herramienta in herramientas:
            print(f"    ✔ {herramienta}")
            
    print("\n" + "="*50 + "\n")

# --- PUNTO DE ENTRADA DEL SCRIPT ---
if __name__ == "__main__":
    generar_perfil_profesional()