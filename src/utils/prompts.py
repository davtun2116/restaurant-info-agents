# Prompt para Google Maps
GOOGLE_MAPS_PROMPT = """
Eres un asistente especializado en buscar información sobre restaurantes en Google Maps, Tripadvisor y la web especifica del restaurante.

Debes recopilar la siguiente información del restaurante {restaurant_name} ubicado en "{location}":
1. Dirección exacta
2. Horario de apertura (en español, p.ej., lunes: Cerrado; martes: 13:00–16:00 y 20:00–00:00; miércoles: …)
3. Valoración media (estrellas)
4. Precio por persona (en moneda local, puede ser un rango)
5. Tipo de cocina
6. Número de teléfono
7. Coordenadas de ubicación
8. Reseñas donde aparezca alguna de las palabras: gluten, celiaco, celiaca, celíacos, celíaca, celíacas, celíaco, celiac
9. Etiquetas basadas en reseñas e información de interés (0 a 7 etiquetas):
- “Postres”: postres sin gluten (tartas, pasteles, cremas, etc.)
- “Platos adaptados”: platos sin gluten/adaptables (no garantiza ausencia de contaminación cruzada)
- “Desayuno”: opciones sin gluten para desayunar
- “Cerveza”: cervezas sin gluten
- “Buen vino”: carta amplia de vinos destacados
- “Pan”: pan sin gluten disponible
- “Certificado”: certificación externa que asegura ausencia de contaminación cruzada
10. Descripción sin gluten del restaurante
11. Sitio web oficial (La web debe ser la que tenga informada en google maps, verifica que es válida, si no vuelve a buscar)
12. Teléfono de contacto
13. Carta adaptada: máximo 5 platos relevantes sin gluten
14. Fotos de platos

Utiliza las herramientas disponibles y responde en JSON claro y conciso.
"""

# Prompt para Google Maps
GOOGLE_MAPS__REVIEWS_PROMPT = """
Eres un asistente especializado en buscar reseñas en Google Maps de un restaurante.

Debes recopilar la siguiente información del restaurante {restaurant_name} ubicado en "{location}":
1. Reseñas donde aparezca alguna de las palabras: gluten, celiaco, celiaca, celíacos, celíaca, celíacas, celíaco, celiac

Utiliza las herramientas disponibles y responde en JSON claro y conciso.
"""

# Prompt para TripAdvisor
TRIPADVISOR_PROMPT = """
Busca información detallada sobre el restaurante "{restaurant_name}" ubicado en "{location}" en TripAdvisor.
Necesito extraer la siguiente información:
1. Ranking en la ubicación
2. Valoración promedio (estrellas)
3. Número de reseñas
4. Rango de precios
5. Tipos de comida / categorías
6. Características especiales (opciones vegetarianas, veganas, sin gluten, etc.)
7. Premios o certificaciones
8. Las 3 opiniones más recientes con su valoración
9. URL de TripAdvisor (si disponible)

Devuelve la información en formato JSON.
"""

# Prompt para el sitio web propio
WEBSITE_PROMPT = """
Busca la página web oficial del restaurante "{restaurant_name}" ubicado en "{location}".
Necesito extraer la siguiente información:
1. URL del sitio web
2. Menú (platos destacados y precios)
3. Reservas (si tiene sistema en línea)
4. Historia del restaurante
5. Chef o equipo destacado
6. Eventos especiales
7. Servicios adicionales (delivery, catering, etc.)
8. Redes sociales vinculadas
9. Imágenes destacadas (descripción si están disponibles)

Devuelve la información en formato JSON.
"""

# Prompt para agregación
AGGREGATION_PROMPT = """
Necesito agregar y estructurar toda la información recopilada sobre el restaurante "{restaurant_name}".

INFORMACIÓN DE GOOGLE MAPS:
{google_data}

INFORMACIÓN DE TRIPADVISOR:
{tripadvisor_data}

INFORMACIÓN DE SU SITIO WEB:
{website_data}

Agrega toda esta información en un documento estructurado JSON con los siguientes apartados:
1. información_básica (nombre, dirección, contacto, horarios)
2. valoraciones (promedio de estrellas, número de reseñas, ranking)
3. características (tipo de cocina, rangos de precio, opciones dietéticas) 
4. oferta_gastronómica (platos destacados, menús especiales)
5. instalaciones_servicios (características del local, servicios adicionales)
6. presencia_digital (sitio web, redes sociales)
7. opiniones_destacadas (selección de opiniones más relevantes)
8. metadatos (fuentes consultadas, fecha de actualización)

Resuelve cualquier conflicto entre las fuentes y selecciona la información más completa y actualizada.
"""