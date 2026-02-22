def generar_perfil_profesional() -> None:
    # --- Datos personales ---
    nombre: str = "Rodrigo García Pérez"
    rol_principal: str = "Cloud Data Engineer"
    
    contacto: dict = {
        "Teléfono": "+525578218631",
        "Email": "rodrigo-gp839@outlook.com",
        "LinkedIn": "linkedin.com/in/rodrigo-garcia-perez-",
        "Ubicación": "Chimalhuacán, Estado de México"
    }

    # --- Experiencia ---
    experiencia: list = [
        {
            "rol": "Becario TI / DBA",
            "empresa": "Lockton México",
            "periodo": "Ene 2025 - Jun 2026",
            "logros": [
                "Realización y administración de bases de datos SQL.",
                "Automatización de consultas (40% reducción de tiempo).",
                "Integración de >10 fuentes de datos para inteligencia de negocios."
            ]
        }
    ]

    # --- Formación ---
    formacion: list = [
        "Maestría en Dirección de Proyectos | UNITEC (Ene 2026 - Abr 2027)",
        "Ingeniería en Sistemas Computacionales | UNITEC (Sep 2021 - Dic 2025)"
    ]

    # --- Habilidades técnicas ---
    habilidades: dict = {
        "⚙️ LENGUAJES Y BASES DE DATOS": [
            "SQL Avanzado: Window Functions, CTEs y optimización de consultas.",
            "Python: Extracción de APIs (requests), análisis (pandas) y cloud (boto3).",
            "Bases de Datos: Administración y arquitectura en PostgreSQL y SQL Server."
        ],
        "☁️ CLOUD & DEVOPS": [
            "AWS: Diseño de arquitecturas con S3, EC2, RDS, Lambda y IAM.",
            "IaC & Contenedores: Despliegue con Terraform y empaquetado con Docker.",
            "CI/CD: Automatización de pipelines con GitHub Actions."
        ],
        "🏗️ MODERN DATA STACK": [
            "Orquestación: Automatización de flujos de datos con Apache Airflow.",
            "Transformación: Modelado dimensional en el DWH con dbt.",
            "Data Warehousing: Almacenamiento analítico en Amazon Redshift."
        ],
        "📊 GESTIÓN Y LIDERAZGO": [
            "Metodología PMBOK: Gestión de alcance, tiempo y riesgos del proyecto.",
            "Traducción de Negocio: Dashboards ejecutivos y documentación técnica."
        ]
    }

    # --- Generación de reporte en consola ---
    print("\n" + "="*70)
    print(f"👨‍💻 {nombre} | {rol_principal}")
    print("="*70)
    
    print("\n CONTACTO:")
    print(f"   ✉️ {contacto['Email']} | 📞 {contacto['Teléfono']}")
    
    print("\n💼 EXPERIENCIA:")
    for exp in experiencia:
        print(f"   > {exp['rol']} en {exp['empresa']} ({exp['periodo']})")
        for logro in exp['logros']:
            print(f"     - {logro}")

    print("\n🎓 FORMACIÓN ACADÉMICA:")
    for grado in formacion:
        print(f"   > {grado}")
    
    print("\n TECH STACK DETALLADO (JULIO 2026):")
    for categoria, herramientas in habilidades.items():
        print(f"\n  {categoria}:")
        for herramienta in herramientas:
            print(f"    ✔ {herramienta}")
            
    print("\n" + "="*70 + "\n")

# --- Punto de entrada del script ---
if __name__ == "__main__":
    generar_perfil_profesional()