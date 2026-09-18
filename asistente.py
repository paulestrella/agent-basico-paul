class Asistente:
    def __init__(self, nombre_negocio):
        self.nombre_negocio = nombre_negocio
        self.historial = []
        self.nombre_usuario = None
        self.preguntas_frecuentes = {
            "horario": "Nuestro horario es de lunes a viernes, de 9:00 a 18:00.",
            "ubicacion": "Estamos ubicados en el centro de la ciudad.",
            "precios": "Puedes consultar nuestros precios en el negocio.",
        }
        self.precios_servicios = {
            "corte": 20.0,
            "manicure": 15.0,
            "pedicure": 18.0,
        }

    def buscar_faq(self, mensaje_normalizado):
        for clave, respuesta in self.preguntas_frecuentes.items():
            if clave in mensaje_normalizado:
                return respuesta

        return "No entendi tu mensaje."

    def calcular_presupuesto(self):
        servicio = input("¿Que servicio te interesa? ").strip().casefold()
        if servicio not in self.precios_servicios:
            return f"El servicio '{servicio}' no existe."

        try:
            cantidad = int(input("¿Cuantas veces quieres agendarlo? "))
        except ValueError:
            return "Por favor, introduce un numero valido."

        costo_total = self.precios_servicios[servicio] * cantidad
        return f"El costo total es de ${costo_total:.2f}."

    def mostar_historial(self):
        for quien, texto in self.historial:
            print(f"{quien}: {texto}")

    def responder(self, mensaje):
        self.historial.append(("Usuario", mensaje))
        mensaje_normalizado = mensaje.casefold()

        if any(palabra in mensaje_normalizado for palabra in ("adios", "salir", "chao")):
            nombre_usuario = f" {self.nombre_usuario}." if self.nombre_usuario else "."
            respuesta = f"Hasta luego{nombre_usuario} Gracias por visitar {self.nombre_negocio}."
        elif mensaje_normalizado.startswith("me llamo"):
            nombre = mensaje[8:].strip()
            self.nombre_usuario = nombre[:1].upper() + nombre[1:].lower()
            respuesta = f"Hola, {self.nombre_usuario}! Bienvenido a {self.nombre_negocio}."
        elif any(palabra in mensaje_normalizado for palabra in ("calcular", "presupuesto", "costo")):
            respuesta = self.calcular_presupuesto()
        elif "hola" in mensaje_normalizado or "buenas" in mensaje_normalizado:
            nombre_usuario = f", {self.nombre_usuario}" if self.nombre_usuario else ""
            respuesta = f"Hola{nombre_usuario}! Bienvenido a {self.nombre_negocio}."
        else:
            respuesta = self.buscar_faq(mensaje_normalizado)

        self.historial.append(("Asistente", respuesta))
        return respuesta
