# -*- coding: utf-8 -*-
"""Los datos de prueba por industria: el vocabulario con que el simulador escribe la
documentación de una organización del sector.

    python3 tests/sintetico/simulador.py <carpeta> --dia 1 --sector cooperativas

Ocho entornos, en siete industrias de Suramérica: entidades financieras (bancos y
cooperativas de ahorro y crédito), retail, minería, construcción e infraestructura,
petróleo y gas, telecomunicaciones y logística. No hay una empresa con nombre detrás
de ninguno: es documentación representativa del sector, y así se presenta.

**El motor es uno; los hechos y el papel, de cada entorno.** Las reglas que deciden
qué hito venció, qué se prometió y cuándo, qué factura no tiene acta, son las mismas en
los cuatro, y la clave se deduce de los hechos igual que siempre. Cada entorno sortea sus
propios hechos con su semilla (`SEMILLA`), y cada uno los nombra a su manera: un hito de
minería es «Licencia y permisos obtenidos», no «Integración con el core».

Nada de aquí es de una organización real: ni las personas, ni los proveedores, ni las
cifras.

Una regla para cada perfil: `ENTREGABLES_PROV` no puede solaparse con `FASES`. El acta
de recibo se empareja por contención, y dos cosas distintas que se llaman casi igual en
el mismo proyecto cruzan sus cuentas. `selftest()` lo comprueba.

Los dos controles negativos llevan nombres de proyecto y producto comunes. Se llamaron
«Control negativo de portafolio» hasta el 14 de octubre de 2026: el agente leía en el
nombre de la carpeta que ahí no debía encontrar nada.
"""

# Qué nombra cada lista, y por qué existe:
# · FASES: los hitos se llaman como se llaman en la industria. «Hito 1 · 433 días sin
#   evidencia» dejaba ilegible la tabla que más importa del informe, y lo dijo el propio
#   agente al leer el material.
# · AVANCES: lo que un informe de avance dice de verdad. «Avance del periodo» no da
#   materia prima para un análisis de causa.
# · PROVEEDORES y ENTREGABLES_PROV: contrato contra acta de recibo contra factura, donde
#   aparece el dinero pagado por algo que nadie aceptó. Cuatro señales viven aquí.
# · SUPUESTOS: enunciados que alguien puede verificar o no; uno sin verificar es un riesgo
#   que nadie registró.
BANCOS = {
    "ETIQUETA": "Entidades financieras de Suramérica · bancos",
    "AREAS": ["Banca de Personas", "Banca Empresas", "Medios de Pago", "Tecnología",
              "Riesgo y Cumplimiento", "Canales Digitales", "Operaciones", "Tesorería",
              "Banca Hipotecaria", "Banca PyME"],
    "COMITES": ["Comité de Transformación Digital", "Comité de Arquitectura",
                "Comité de Riesgos", "Comité de Medios de Pago", "Comité de Banca Empresas"],
    "TEMAS_PRY": [
        ("Originación digital", "crédito de consumo"), ("Core de depósitos", "cuenta de ahorros"),
        ("Migración a la nube", None), ("Open Banking", "APIs de datos"),
        ("Débito contactless", "tarjeta débito"), ("Prevención de lavado de activos", None),
        ("Billetera y QR", "pagos QR"), ("Onboarding PyME", "cuenta PyME"),
        ("Motor de decisión", None), ("Nómina electrónica", "nómina empresarial"),
        ("Portal de proveedores", None), ("Cobranza digital", "recaudos"),
        ("Firma electrónica", None), ("Tarjeta de crédito digital", "tarjeta de crédito"),
        ("Remesas", "remesas familiares"), ("Microseguros", "microseguros"),
        ("Banca abierta fase 2", None), ("Conciliación automática", None),
        ("Canal WhatsApp", None), ("Scoring alternativo", None),
    ],
    "TEMAS_PRD": [
        "Pagos QR comercios", "Nómina empresarial", "Crédito hipotecario digital",
        "Cuenta PyME", "Tarjeta de crédito digital", "Recaudos y cobros", "Microseguros",
        "Remesas familiares", "Cuenta de ahorros joven", "Crédito de libre inversión",
        "Datáfono móvil", "Factoring digital", "Seguro de desempleo", "CDT digital",
        "Cuenta de nómina", "Adquirencia comercios", "Billetera empresarial",
        "Crédito rotativo", "Pagos recurrentes", "Corresponsal bancario",
    ],
    "FASES": ("Diseño funcional aprobado", "Ambiente de pruebas certificado",
              "Integración con el core", "Piloto con usuarios internos",
              "Salida a producción", "Estabilización y cierre"),
    "AVANCES": (
        "Se ajustó el plan de pruebas con el área de seguridad",
        "Se acordó con arquitectura cómo se revisan los requisitos no funcionales",
        "Dos historias quedaron fuera del alcance del sprint por dependencia con el core",
        "Se reprogramó la salida por ventana de cambio del área de operaciones",
        "El equipo perdió dos semanas por rotación de un desarrollador clave",
        "Se levantó un hallazgo de seguridad en la revisión de arquitectura",
        "La prueba de carga no alcanzó el umbral pactado y se repite",
        "Se recibió la aprobación regulatoria pendiente desde el trimestre anterior",
    ),
    "RIESGOS": (
        "Dependencia del calendario de liberaciones del core",
        "Disponibilidad del equipo de seguridad para la revisión final",
        "Concentración del conocimiento en una sola persona",
        "Cambio regulatorio en discusión que puede mover el alcance",
        "El proveedor no ha confirmado la fecha de la última entrega",
    ),
    "PROVEEDORES": ("Consultora Andina S.A.S.", "Integra Sistemas Ltda.", "Datacore Colombia",
                    "Núcleo Financiero S.A.", "Talento Digital S.A.S.", "Redes del Norte Ltda."),
    "ENTREGABLES_PROV": ("Licenciamiento del motor", "Bolsa de horas de desarrollo",
                         "Parametrización del tarifario", "Mesa de ayuda del primer trimestre",
                         "Traspaso de conocimiento"),
    "SUPUESTOS": ("El segmento paga por esto", "El canal actual soporta el volumen",
                  "La regulación vigente lo permite", "El proveedor cumple el tiempo pactado",
                  "La demanda declarada se sostiene sin campaña"),
    "SEGMENTOS": ["Personas", "PyME", "Empresas", "Microcomercio", "Base de la pirámide"],
    "CONTROL_PRY": "Renovación de cajeros automáticos",
    "CONTROL_PRD": "Ahorro programado",
}

RETAIL = {
    "ETIQUETA": "Empresas de retail de Suramérica · supermercados y tiendas",
    "AREAS": ["Comercial", "Abastecimiento", "Logística", "Tiendas", "Comercio electrónico",
              "Mercadeo", "Tecnología", "Finanzas", "Talento humano", "Servicio al cliente"],
    "COMITES": ["Comité de Expansión", "Comité de Transformación Digital",
                "Comité de Cadena de Abastecimiento", "Comité Comercial", "Comité de Arquitectura"],
    "TEMAS_PRY": [
        ("Tienda en línea", "venta en línea"), ("Programa de fidelización", "puntos de fidelización"),
        ("Centro de distribución norte", None), ("Reposición automática", None),
        ("Cajas de autopago", "autopago en tienda"), ("Pago con QR en caja", "pago con QR"),
        ("Precios dinámicos", None), ("Marca propia de alimentos", "marca propia"),
        ("Domicilios en dos horas", "entrega rápida"), ("Migración del ERP", None),
        ("Etiquetas electrónicas de precio", None), ("Pronóstico de demanda", None),
        ("Aplicación de clientes", "app de clientes"), ("Recogida en tienda", "compra y recoge"),
        ("Portal de proveedores", None), ("Mercado de terceros", "marketplace"),
        ("Crédito en tienda", "tarjeta de la tienda"), ("Remodelación de treinta tiendas", None),
        ("Control de mermas", None), ("Inventario con RFID", None),
    ],
    "TEMAS_PRD": [
        "Venta en línea", "Puntos de fidelización", "Autopago en tienda", "Pago con QR",
        "Marca propia", "Entrega rápida", "App de clientes", "Compra y recoge", "Marketplace",
        "Tarjeta de la tienda", "Suscripción de despensa", "Garantía extendida",
        "Tarjeta regalo", "Club de mascotas", "Lista de regalos", "Recargas en caja",
        "Ofertas personalizadas", "Venta corporativa", "Devoluciones sin recibo",
        "Kits escolares",
    ],
    "FASES": ("Diseño de la experiencia aprobado", "Ambiente de pruebas certificado",
              "Integración con el ERP", "Piloto en tiendas", "Despliegue en la cadena",
              "Estabilización y cierre"),
    "AVANCES": (
        "Se ajustó el plan de pruebas con el área de seguridad",
        "Se acordó con arquitectura cómo se revisan los requisitos no funcionales",
        "La validación con dos tiendas se extendió una semana por el conteo de inventario",
        "Se reprogramó el despliegue por el congelamiento de temporada de fin de año",
        "El equipo perdió dos semanas por rotación de un desarrollador clave",
        "Se levantó un hallazgo de seguridad en los medios de pago",
        "La prueba de carga de temporada no alcanzó el umbral pactado y se repite",
        "Se recibió el concepto de Jurídica sobre los términos de uso",
    ),
    "RIESGOS": (
        "Congelamiento de cambios en temporada alta",
        "Disponibilidad de los jefes de tienda para el piloto",
        "Concentración del conocimiento en una sola persona",
        "Cambio en la regulación de datos personales que puede mover el alcance",
        "El proveedor no ha confirmado la fecha de la última entrega",
    ),
    "PROVEEDORES": ("Retail Andino Consultores S.A.S.", "Logística del Valle Ltda.",
                    "Sistemas Comerciales del Norte", "Integra Comercio S.A.S.",
                    "Tecnología para Tiendas Ltda.", "Datos y Demanda S.A.S."),
    "ENTREGABLES_PROV": ("Licenciamiento de la plataforma", "Bolsa de horas de desarrollo",
                         "Configuración del catálogo", "Soporte del primer trimestre",
                         "Capacitación a jefes de sección"),
    "SUPUESTOS": ("El cliente paga por la entrega rápida", "Las tiendas soportan el volumen",
                  "La regulación de datos lo permite", "El proveedor cumple el tiempo pactado",
                  "La demanda se sostiene sin descuento"),
    "SEGMENTOS": ["Hogares", "Jóvenes", "Pequeños negocios", "Empresas", "Clientes frecuentes"],
    "CONTROL_PRY": "Iluminación LED en bodegas",
    "CONTROL_PRD": "Bolsas reutilizables",
}

MINERIA = {
    "ETIQUETA": "Empresas mineras de Suramérica · oro y cobre",
    "AREAS": ["Mina", "Planta de procesamiento", "Mantenimiento", "Seguridad y Salud",
              "Medio Ambiente", "Relacionamiento comunitario", "Tecnología", "Logística",
              "Finanzas", "Geología"],
    "COMITES": ["Comité de Inversiones", "Comité de Operaciones", "Comité de Seguridad",
                "Comité Ambiental", "Comité de Tecnología"],
    "TEMAS_PRY": [
        ("Mantenimiento predictivo de camiones", "monitoreo de flota"),
        ("Ampliación de la relavera", None), ("Planta de tratamiento de agua", None),
        ("Despacho automático de flota", "despacho de flota"),
        ("Monitoreo de taludes", "alerta de taludes"), ("Sistema de gestión de seguridad", None),
        ("Red privada LTE en mina", None), ("Gemelo digital de la planta", "gemelo digital"),
        ("Trazabilidad del mineral", "trazabilidad"), ("Electrificación de equipos", None),
        ("Programa de relacionamiento comunitario", None), ("Control de polvo en vías", None),
        ("Laboratorio químico automatizado", None), ("Migración del ERP", None),
        ("Monitoreo de fatiga de operadores", "alerta de fatiga"),
        ("Planificación minera de largo plazo", None), ("Cierre del botadero sur", None),
        ("Energía solar para el campamento", None),
        ("Control de inventario de repuestos", "almacén de repuestos"),
        ("Perforación con datos en línea", None),
    ],
    "TEMAS_PRD": [
        "Monitoreo de flota", "Alerta de taludes", "Despacho de flota", "Gemelo digital",
        "Trazabilidad", "Alerta de fatiga", "Almacén de repuestos", "Reporte ambiental",
        "Permisos de trabajo digitales", "Inspección con drones", "Control de acceso a mina",
        "Tablero de producción", "Consumo de agua en línea", "Gestión de contratistas",
        "Muestreo de leyes", "Mantenimiento de molinos", "Reporte a la comunidad",
        "Huella de carbono", "Transporte de personal", "Venta de concentrado",
    ],
    "FASES": ("Ingeniería básica aprobada", "Ingeniería de detalle aprobada",
              "Licencia y permisos obtenidos", "Montaje e instalación",
              "Pruebas en operación", "Entrega a operaciones"),
    "AVANCES": (
        "Se actualizó el presupuesto de la obra con el área de compras",
        # Sin entregas de proveedor al azar: una frase así es un hecho que la clave no
        # modela (D022, y en minería quedó una: D055).
        "Se acordó con operaciones el plan de arranque de los equipos",
        "Las lluvias detuvieron el montaje durante diez días",
        "Se reprogramó la parada de planta por la ventana de mantenimiento",
        "El equipo perdió dos semanas por rotación de un ingeniero clave",
        "Se levantó un hallazgo en la auditoría de seguridad",
        "El primer ensayo de disponibilidad de los equipos no alcanzó lo pactado y se repite",
        "Se recibió el permiso ambiental pendiente desde el trimestre anterior",
    ),
    "RIESGOS": (
        "Ventana de parada de planta definida por operaciones",
        "Bloqueo de la vía de acceso a la mina",
        "Concentración del conocimiento en una sola persona",
        "Cambio en la licencia ambiental que puede mover el alcance",
        "El proveedor no ha confirmado la fecha de la última entrega",
    ),
    "PROVEEDORES": ("Ingeniería Minera del Sur S.A.S.", "Montajes Industriales Ltda.",
                    "Equipos Pesados Andinos", "Geotecnia Aplicada S.A.S.",
                    "Automatización de Procesos Ltda.", "Servicios Ambientales del Norte"),
    "ENTREGABLES_PROV": ("Licenciamiento del software", "Bolsa de horas de ingeniería",
                         "Calibración de sensores", "Soporte del primer trimestre",
                         "Capacitación a operadores"),
    "SUPUESTOS": ("Operaciones adopta la herramienta", "La red de la mina soporta el volumen",
                  "La licencia ambiental lo permite", "El proveedor cumple el tiempo pactado",
                  "El ahorro se sostiene sin inversión adicional"),
    "SEGMENTOS": ["Operadores", "Supervisores", "Mantenimiento", "Gerencia", "Comunidad"],
    "CONTROL_PRY": "Cambio de luminarias del campamento",
    "CONTROL_PRD": "Solicitud de dotación",
}

COOPERATIVAS = {
    "ETIQUETA": "Entidades financieras de Suramérica · cooperativas de ahorro y crédito",
    "AREAS": ["Crédito", "Ahorro y aportes", "Servicio al asociado", "Tecnología",
              "Riesgo y Cumplimiento", "Canales digitales", "Operaciones", "Tesorería",
              "Cartera y cobranza", "Bienestar social"],
    "COMITES": ["Consejo de Administración", "Comité de Crédito", "Comité de Riesgos",
                "Comité de Tecnología", "Comité de Educación"],
    "TEMAS_PRY": [
        ("Crédito de libranza digital", "crédito de libranza"),
        ("Apertura de ahorro en línea", "ahorro a la vista"), ("Core cooperativo", None),
        ("Aportes sociales en línea", "aportes sociales"),
        ("Tarjeta débito para asociados", "tarjeta débito"),
        ("Prevención de lavado de activos", None), ("Pagos con QR", "pagos QR"),
        ("Microcrédito rural", "microcrédito"), ("Motor de crédito", None),
        ("Convenios de libranza con empresas", None), ("Corresponsales rurales", None),
        ("Cobranza digital", "recaudos"), ("Firma electrónica", None),
        ("Fondo de solidaridad en línea", "auxilios de solidaridad"),
        ("Remesas", "remesas familiares"), ("Seguros para asociados", "microseguros"),
        ("Asamblea virtual de delegados", None), ("Conciliación automática", None),
        ("Canal WhatsApp", None), ("Educación financiera digital", None),
    ],
    "TEMAS_PRD": [
        "Crédito de libranza", "Ahorro a la vista", "Aportes sociales", "Tarjeta débito",
        "Pagos QR", "Microcrédito", "Recaudos", "Auxilios de solidaridad",
        "Remesas familiares", "Microseguros", "CDAT digital", "Ahorro programado escolar",
        "Crédito educativo", "Crédito de vivienda", "Crédito para emprendimiento",
        "Billetera del asociado", "Convenios comerciales", "Crédito rotativo",
        "Ahorro navideño", "Seguro exequial",
    ],
    "FASES": ("Diseño funcional aprobado", "Ambiente de pruebas certificado",
              "Integración con el core cooperativo", "Piloto con asociados",
              "Salida a producción", "Estabilización y cierre"),
    "AVANCES": (
        "Se ajustó el plan de pruebas con el área de seguridad",
        "Se acordó con arquitectura cómo se revisan los requisitos no funcionales",
        "El Consejo de Administración pidió ajustar el reglamento antes del piloto",
        "Se reprogramó la salida por el cierre contable de fin de mes",
        "El equipo perdió dos semanas por rotación de un desarrollador clave",
        "Se levantó un hallazgo de seguridad en la revisión de arquitectura",
        "La prueba de carga no alcanzó el umbral pactado y se repite",
        "Se recibió el concepto pendiente del ente supervisor",
    ),
    "RIESGOS": (
        "Dependencia del proveedor del core cooperativo",
        "Aprobación del reglamento por el Consejo de Administración",
        "Concentración del conocimiento en una sola persona",
        "Cambio normativo del supervisor que puede mover el alcance",
        "El proveedor no ha confirmado la fecha de la última entrega",
    ),
    "PROVEEDORES": ("Soluciones Solidarias S.A.S.", "Sistemas Cooperativos Ltda.",
                    "Integración Financiera del Sur", "Red Rural de Pagos S.A.S.",
                    "Talento Solidario Ltda.", "Datos para Cooperativas S.A.S."),
    "ENTREGABLES_PROV": ("Licenciamiento del módulo", "Bolsa de horas de desarrollo",
                         "Parametrización de líneas de crédito", "Mesa de ayuda del primer trimestre",
                         "Capacitación a asesores"),
    "SUPUESTOS": ("Los asociados usan el canal digital", "El core soporta el volumen",
                  "El reglamento vigente lo permite", "El proveedor cumple el tiempo pactado",
                  "La demanda se sostiene sin campaña"),
    "SEGMENTOS": ["Asociados urbanos", "Asociados rurales", "Jóvenes", "Pensionados",
                  "Microempresarios"],
    "CONTROL_PRY": "Cambio de mobiliario de agencias",
    "CONTROL_PRD": "Kit de bienvenida del asociado",
}

CONSTRUCCION = {
    "ETIQUETA": "Empresas de construcción e infraestructura de Suramérica · vías y edificaciones",
    "AREAS": ["Proyectos", "Ingeniería", "Interventoría", "Compras", "Seguridad y Salud en el Trabajo",
              "Medio Ambiente", "Gestión predial", "Tecnología", "Finanzas", "Calidad"],
    "COMITES": ["Comité de Obra", "Comité de Inversiones", "Comité de Contratación",
                "Comité de Seguridad", "Comité Técnico"],
    "TEMAS_PRY": [
        ("Variante vial del sur", None), ("Edificio de oficinas Torre Norte", "arriendo de oficinas"),
        ("Puente vehicular sobre el río", None), ("Planta de tratamiento de agua", None),
        ("Vivienda de interés social etapa 2", "vivienda VIS"), ("Ampliación del aeropuerto regional", None),
        ("Modelado BIM de proyectos", "modelos BIM"), ("Control de avance con drones", None),
        ("Bodega logística modular", "bodegas en arriendo"), ("Doble calzada del corredor central", None),
        ("Colegio público por concesión", None), ("Hospital de segundo nivel", None),
        ("Gestión predial digital", None), ("Portal de contratistas", None),
        ("Patio de prefabricados", "prefabricados"), ("Renovación de redes de acueducto", None),
        ("Centro comercial de barrio", "locales comerciales"), ("Túnel de conexión urbana", None),
        ("Sistema de costos de obra", None), ("Vivienda campestre", "lotes campestres"),
    ],
    "TEMAS_PRD": [
        "Arriendo de oficinas", "Vivienda VIS", "Modelos BIM", "Bodegas en arriendo", "Prefabricados",
        "Locales comerciales", "Lotes campestres", "Mantenimiento vial", "Alquiler de maquinaria",
        "Interventoría externa", "Diseño y construcción", "Administración delegada",
        "Concreto premezclado", "Venta de vivienda sobre planos", "Remodelación corporativa",
        "Parqueaderos", "Vivienda para arriendo", "Señalización vial", "Obras de urbanismo",
        "Postventa de vivienda",
    ],
    "FASES": ("Diseños de detalle aprobados", "Licencias y permisos obtenidos", "Cimentación terminada",
              "Estructura terminada", "Entrega de obra al cliente", "Liquidación del contrato"),
    "AVANCES": (
        "Se ajustó el programa de obra con el contratista de estructura",
        "Se acordó con la interventoría cómo se miden las cantidades de obra",
        "Las lluvias detuvieron el movimiento de tierras durante nueve días",
        "Se reprogramó el vaciado por la llegada tardía del acero",
        "El equipo perdió dos semanas por rotación del residente de obra",
        "Se levantó un hallazgo de seguridad en el trabajo en alturas",
        "El ensayo de resistencia del concreto no alcanzó el valor pactado y se repite",
        "Se recibió el concepto de la autoridad ambiental sobre el plan de manejo",
    ),
    "RIESGOS": (
        "Lluvias por encima del promedio en la temporada",
        "Compra de predios pendiente en el trazado",
        "Concentración del conocimiento en una sola persona",
        "Cambio en la norma de sismorresistencia que puede mover el alcance",
        "El proveedor no ha confirmado la fecha de la última entrega",
    ),
    "PROVEEDORES": ("Constructora del Valle S.A.S.", "Estructuras Metálicas del Norte Ltda.",
                    "Concretos Andinos S.A.S.", "Geotecnia y Suelos Ltda.",
                    "Interventorías Técnicas S.A.S.", "Maquinaria Pesada del Sur"),
    "ENTREGABLES_PROV": ("Suministro de acero de refuerzo", "Bolsa de horas de ingeniería",
                         "Alquiler de equipos de izaje", "Estudio de suelos",
                         "Capacitación a maestros de obra"),
    "SUPUESTOS": ("Los predios se compran a tiempo", "El clima permite el programa de obra",
                  "La licencia se expide sin objeciones", "El proveedor cumple el tiempo pactado",
                  "El precio del acero se sostiene"),
    "SEGMENTOS": ["Hogares", "Empresas", "Entidades públicas", "Inversionistas", "Comunidad"],
    "CONTROL_PRY": "Pintura de la sede administrativa",
    "CONTROL_PRD": "Dotación de cascos",
}

OIL_GAS = {
    "ETIQUETA": "Empresas de petróleo y gas de Suramérica · exploración, producción y transporte",
    "AREAS": ["Exploración", "Producción", "Perforación", "Mantenimiento", "HSE", "Ambiental",
              "Relacionamiento con comunidades", "Tecnología", "Cadena de suministro", "Finanzas"],
    "COMITES": ["Comité de Inversiones", "Comité de Operaciones", "Comité de HSE",
                "Comité de Integridad", "Comité de Tecnología"],
    "TEMAS_PRY": [
        ("Campaña de perforación del bloque sur", None), ("Facilidades de producción temprana", None),
        ("Gasoducto de interconexión", "transporte de gas"), ("Recobro mejorado con agua", None),
        ("Integridad de ductos", None), ("Monitoreo remoto de pozos", "monitoreo de pozos"),
        ("Planta de tratamiento de crudo", None), ("Gemelo digital de la estación", None),
        ("Reducción de quema de gas", "gas para generación"), ("Sísmica 3D del bloque norte", None),
        ("Mantenimiento predictivo de bombas", None), ("Estación de compresión", None),
        ("Tanques de almacenamiento", "almacenamiento para terceros"), ("Sistema de control de pozos", None),
        ("Paneles solares en campo", "energía solar en campo"), ("Plan de abandono de pozos", None),
        ("Laboratorio de fluidos", "análisis de fluidos"), ("Portal de contratistas de campo", None),
        ("Centro de control integrado", None), ("Programa de inversión social", None),
    ],
    "TEMAS_PRD": [
        "Transporte de gas", "Monitoreo de pozos", "Gas para generación", "Almacenamiento para terceros",
        "Energía solar en campo", "Análisis de fluidos", "Venta de crudo pesado", "Suministro de GLP",
        "Servicios de perforación", "Tratamiento de agua de producción", "Gas natural vehicular",
        "Venta de condensados", "Servicio de compresión", "Inspección de ductos",
        "Alquiler de capacidad de oleoducto", "Crudo liviano para mezcla", "Captura de carbono",
        "Venta de azufre", "Energía para comunidades", "Asfaltos",
    ],
    "FASES": ("Ingeniería básica aprobada", "Licencia ambiental otorgada", "Pozos perforados",
              "Montaje de facilidades", "Primer crudo o gas", "Cierre y entrega a operaciones"),
    "AVANCES": (
        "Se ajustó el plan de perforación con la geología del pozo vecino",
        "Se acordó con integridad cómo se inspeccionan las soldaduras",
        "Un bloqueo de la comunidad detuvo el transporte de equipos ocho días",
        "Se reprogramó la movilización del taladro por disponibilidad del contratista",
        "El equipo perdió dos semanas por rotación del supervisor de campo",
        "Se levantó un hallazgo de seguridad en espacios confinados",
        "La prueba hidrostática no alcanzó la presión pactada y se repite",
        "Se recibió la aprobación de la consulta previa pendiente desde el trimestre anterior",
    ),
    "RIESGOS": (
        "Bloqueos de la comunidad en la vía de acceso",
        "Precio del crudo por debajo del supuesto del caso de negocio",
        "Concentración del conocimiento en una sola persona",
        "Cambio en la licencia ambiental que puede mover el alcance",
        "El proveedor no ha confirmado la fecha de la última entrega",
    ),
    "PROVEEDORES": ("Servicios de Perforación del Sur S.A.S.", "Ingeniería de Ductos Ltda.",
                    "Montajes Petroleros Andinos", "Integridad y Corrosión S.A.S.",
                    "Automatización de Campo Ltda.", "Servicios Ambientales Petroleros"),
    "ENTREGABLES_PROV": ("Alquiler del taladro", "Bolsa de horas de ingeniería",
                         "Inspección con raspador inteligente", "Soporte del primer trimestre",
                         "Capacitación a operadores de campo"),
    "SUPUESTOS": ("El precio del crudo se sostiene", "La comunidad respalda el proyecto",
                  "La licencia ambiental lo permite", "El proveedor cumple el tiempo pactado",
                  "El yacimiento responde como dice el modelo"),
    "SEGMENTOS": ["Generadoras", "Distribuidoras de gas", "Refinerías", "Industria", "Comunidad"],
    "CONTROL_PRY": "Adecuación del casino del campamento",
    "CONTROL_PRD": "Solicitud de dotación de campo",
}

TELECOMUNICACIONES = {
    "ETIQUETA": "Empresas de telecomunicaciones de Suramérica · redes móviles, fibra y servicios empresariales",
    "AREAS": ["Ingeniería de red", "Despliegue", "Operaciones de red", "Tecnología", "Regulatorio",
              "Compras", "Mercadeo", "Servicio al cliente", "Finanzas", "Seguridad de la información"],
    "COMITES": ["Comité de Red", "Comité de Inversiones", "Comité de Producto",
                "Comité de Cambios", "Comité Regulatorio"],
    "TEMAS_PRY": [
        ("Despliegue de 5G en ciudades intermedias", "planes 5G"), ("Fibra hasta el hogar fase 3", "internet por fibra"),
        ("Modernización de la red de transporte", None), ("Migración del core de voz a la nube", None),
        ("Torres compartidas en zonas rurales", "arriendo de torres"), ("Portabilidad numérica en línea", None),
        ("Centro de operaciones de red unificado", None), ("Facturación convergente", None),
        ("Red privada para empresas", "redes privadas"), ("Apagado de la red 3G", None),
        ("Conectividad para colegios públicos", None), ("Plataforma de internet de las cosas", "conectividad IoT"),
        ("Cable submarino regional", None), ("Autogestión en la aplicación móvil", None),
        ("Centros de datos de borde", "colocación en el borde"), ("Renovación de enlaces de microondas", None),
        ("Televisión por protocolo de internet", "televisión IP"), ("Antifraude de llamadas", None),
        ("Inventario de red georreferenciado", None), ("Plan de cobertura de carreteras", None),
    ],
    "TEMAS_PRD": [
        "Planes 5G", "Internet por fibra", "Arriendo de torres", "Redes privadas", "Conectividad IoT",
        "Colocación en el borde", "Televisión IP", "Planes prepago", "Planes empresariales",
        "Roaming regional", "Telefonía fija IP", "Seguridad gestionada", "Enlaces dedicados",
        "Nube para pymes", "Venta de equipos a plazos", "Seguro de equipos", "Mensajería masiva",
        "Wifi para eventos", "Servicio técnico a domicilio", "Recarga en tiendas",
    ],
    "FASES": ("Diseño de red aprobado", "Permisos de instalación obtenidos", "Sitios construidos",
              "Integración con la red", "Lanzamiento comercial", "Cierre y entrega a operaciones"),
    "AVANCES": (
        "Se ajustó el plan de sitios con el proveedor de infraestructura",
        "Se acordó con operaciones cómo se miden las pruebas de aceptación de cada sitio",
        "La alcaldía detuvo la instalación de antenas en dos barrios durante diez días",
        "Se reprogramó la llegada de los equipos de radio por demoras en la aduana",
        "El equipo perdió dos semanas por rotación del gerente de despliegue",
        "Se levantó un hallazgo de seguridad en trabajo en torres",
        "La prueba de velocidad en campo no alcanzó el valor pactado y se repite",
        "Se recibió el concepto del regulador sobre el uso del espectro",
    ),
    "RIESGOS": (
        "Permisos municipales para instalar antenas",
        "Subasta de espectro aplazada por el regulador",
        "Concentración del conocimiento en una sola persona",
        "Cambio en la norma de compartición de infraestructura que puede mover el alcance",
        "El proveedor no ha confirmado la fecha de la última entrega",
    ),
    "PROVEEDORES": ("Infraestructura de Torres del Sur S.A.S.", "Redes y Radio Andinas Ltda.",
                    "Fibra Óptica del Pacífico S.A.S.", "Integración de Red Ltda.",
                    "Obras Civiles de Telecomunicaciones", "Soporte de Red Continental"),
    "ENTREGABLES_PROV": ("Suministro de antenas y radios", "Bolsa de horas de ingeniería",
                         "Tendido de fibra óptica", "Soporte del primer trimestre",
                         "Capacitación a técnicos de campo"),
    "SUPUESTOS": ("Los permisos municipales salen a tiempo", "El espectro se asigna en la fecha prevista",
                  "La demanda de planes crece como dice el caso", "El proveedor cumple el tiempo pactado",
                  "El tipo de cambio de los equipos se sostiene"),
    "SEGMENTOS": ["Hogares", "Pymes", "Grandes empresas", "Gobierno", "Operadores mayoristas"],
    "CONTROL_PRY": "Cambio de mobiliario de la sala de espera",
    "CONTROL_PRD": "Solicitud de uniformes de técnicos",
}

LOGISTICA = {
    "ETIQUETA": "Empresas de logística de Suramérica · centros de distribución, transporte y última milla",
    "AREAS": ["Operaciones", "Centros de distribución", "Transporte", "Tecnología", "Comercial",
              "Compras", "Seguridad y Salud en el Trabajo", "Comercio exterior", "Finanzas", "Calidad"],
    "COMITES": ["Comité de Operaciones", "Comité de Inversiones", "Comité de Clientes",
                "Comité de Seguridad", "Comité de Tecnología"],
    "TEMAS_PRY": [
        ("Centro de distribución del norte", "almacenamiento para terceros"), ("Sistema de gestión de bodegas", None),
        ("Flota eléctrica de última milla", "entregas en el día"), ("Ruteo dinámico de vehículos", None),
        ("Cross docking en el puerto", "cross docking"), ("Seguimiento satelital de la flota", None),
        ("Clasificadora automática de paquetes", None), ("Portal de clientes con trazabilidad", None),
        ("Cadena de frío para farmacéuticos", "logística de frío"), ("Consolidación de cargas regionales", None),
        ("Puntos de recogida en estaciones", "puntos de recogida"), ("Facturación electrónica de fletes", None),
        ("Bodega aduanera en zona franca", "depósito aduanero"), ("Control de inventario con radiofrecuencia", None),
        ("Logística inversa para comercio electrónico", "devoluciones"), ("Patio de contenedores", None),
        ("Mantenimiento predictivo de montacargas", None), ("Integración con transportadores aliados", None),
        ("Tablero de nivel de servicio", None), ("Plan de continuidad de la operación", None),
    ],
    "TEMAS_PRD": [
        "Almacenamiento para terceros", "Entregas en el día", "Cross docking", "Logística de frío",
        "Puntos de recogida", "Depósito aduanero", "Devoluciones", "Transporte de carga masiva",
        "Paquetería empresarial", "Distribución a tiendas", "Agenciamiento aduanero", "Seguro de mercancía",
        "Empaque y etiquetado", "Transporte refrigerado", "Logística para eventos", "Arriendo de montacargas",
        "Gestión de inventario en sitio", "Carga consolidada internacional", "Mensajería urbana",
        "Almacenamiento de documentos",
    ],
    "FASES": ("Diseño de la operación aprobado", "Permisos de operación obtenidos", "Adecuación de la bodega terminada",
              "Pruebas con carga real", "Arranque de la operación", "Estabilización y entrega a operaciones"),
    "AVANCES": (
        "Se ajustó el plan de arranque con el cliente ancla",
        "Se acordó con operaciones cómo se mide el nivel de servicio de cada ruta",
        "Un paro de transportadores detuvo los despachos durante seis días",
        "Se reprogramó la llegada de las estanterías por demoras del importador",
        "El equipo perdió dos semanas por rotación del jefe de bodega",
        "Se levantó un hallazgo de seguridad en la operación de montacargas",
        "La prueba de exactitud de inventario no alcanzó el valor pactado y se repite",
        "Se recibió el concepto de la autoridad aduanera sobre la bodega",
    ),
    "RIESGOS": (
        "Paros de transportadores en las vías principales",
        "Temporada alta que no permite detener la operación",
        "Concentración del conocimiento en una sola persona",
        "Cambio en la norma de pesos y dimensiones que puede mover el alcance",
        "El proveedor no ha confirmado la fecha de la última entrega",
    ),
    "PROVEEDORES": ("Estanterías Industriales del Valle S.A.S.", "Sistemas de Bodega Andinos Ltda.",
                    "Flotas Eléctricas del Sur S.A.S.", "Integración Logística Ltda.",
                    "Montacargas y Equipos del Norte", "Soporte Logístico Continental"),
    "ENTREGABLES_PROV": ("Suministro de estanterías", "Bolsa de horas de ingeniería",
                         "Arriendo de vehículos eléctricos", "Soporte del primer trimestre",
                         "Capacitación a operarios de bodega"),
    "SUPUESTOS": ("El cliente ancla mantiene sus volúmenes", "Los permisos de operación salen a tiempo",
                  "La operación actual no se detiene durante el arranque", "El proveedor cumple el tiempo pactado",
                  "El precio del combustible se sostiene"),
    "SEGMENTOS": ["Comercio electrónico", "Retail", "Industria", "Farmacéuticas", "Importadores"],
    "CONTROL_PRY": "Pintura de la portería",
    "CONTROL_PRD": "Solicitud de chalecos reflectivos",
}

# Las ocho, y la industria a la que pertenece cada una. Los bancos conservan la semilla
# de siempre, así que corp-demo no cambia.
PERFILES = {"bancos": BANCOS, "cooperativas": COOPERATIVAS, "retail": RETAIL, "mineria": MINERIA,
            "construccion": CONSTRUCCION, "oil-gas": OIL_GAS, "telecomunicaciones": TELECOMUNICACIONES,
            "logistica": LOGISTICA}
INDUSTRIA = {"bancos": "Entidades financieras (bancos y cooperativas) de Suramérica",
             "cooperativas": "Entidades financieras (bancos y cooperativas) de Suramérica",
             "retail": "Empresas de retail de Suramérica",
             "mineria": "Empresas mineras de Suramérica",
             "construccion": "Empresas de construcción e infraestructura de Suramérica",
             "oil-gas": "Empresas de petróleo y gas de Suramérica",
             "telecomunicaciones": "Empresas de telecomunicaciones de Suramérica",
             "logistica": "Empresas de logística de Suramérica"}
SEMILLA = {"bancos": 0, "cooperativas": 362867, "retail": 104729, "mineria": 224737,
           "construccion": 512927, "oil-gas": 690143, "telecomunicaciones": 815681, "logistica": 937219}


def selftest() -> list:
    fallas = []
    llaves = set(BANCOS)
    for nombre, p in PERFILES.items():
        if set(p) != llaves:
            fallas.append(f"{nombre}: llaves distintas {set(p) ^ llaves}")
        for e in p["ENTREGABLES_PROV"]:
            for h in p["FASES"]:
                if e.lower() in h.lower() or h.lower() in e.lower():
                    fallas.append(f"{nombre}: «{e}» y «{h}» se cruzan")
        temas = [t for t, _ in p["TEMAS_PRY"]]
        if len(set(temas)) != len(temas) or len(set(p["TEMAS_PRD"])) != len(p["TEMAS_PRD"]):
            fallas.append(f"{nombre}: temas repetidos")
        # Un avance se escribe al azar: no puede afirmar el estado de un hito, porque
        # contradiría al cronograma sin que la clave lo sepa (14-oct, cooperativas y minería).
        for av in p["AVANCES"]:
            for h in p["FASES"]:
                if h.lower() in av.lower():
                    fallas.append(f"{nombre}: el avance «{av}» nombra el hito «{h}»")
        if p["CONTROL_PRY"] in temas or p["CONTROL_PRD"] in p["TEMAS_PRD"]:
            fallas.append(f"{nombre}: el control comparte nombre con un caso")
    return fallas


if __name__ == "__main__":
    import sys
    f = selftest()
    print("\n".join(f) or "sectores: sin errores")
    sys.exit(1 if f else 0)
