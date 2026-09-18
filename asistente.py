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

    def buscar_faq(self, mensaje_normalizado):
        for clave, respuesta in self.preguntas_frecuentes.items():
            if clave in mensaje_normalizado:
                return respuesta

        return "No entendi tu mensaje."

    def responder(self, mensaje):
        self.historial.append(mensaje)
        mensaje_normalizado = mensaje.casefold()

        if mensaje_normalizado.startswith("me llamo"):
            nombre = mensaje[8:].strip()
            self.nombre_usuario = nombre[:1].upper() + nombre[1:].lower()
            respuesta = f"Hola, {self.nombre_usuario}! Bienvenido a {self.nombre_negocio}."
        elif "hola" in mensaje_normalizado or "buenas" in mensaje_normalizado:
            nombre_usuario = f", {self.nombre_usuario}" if self.nombre_usuario else ""
            respuesta = f"Hola{nombre_usuario}! Bienvenido a {self.nombre_negocio}."
        else:
            respuesta = self.buscar_faq(mensaje_normalizado)

        self.historial.append(respuesta)
        return respuesta
