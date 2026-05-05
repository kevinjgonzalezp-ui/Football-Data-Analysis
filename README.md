# ⚽ Análisis de Datos de Fútbol Profesional

## 📌 Introducción
Este proyecto tiene como objetivo analizar datos de partidos de fútbol de distintas ligas profesionales para identificar patrones en los resultados, la cantidad de goles y el rendimiento de los equipos.

Se combinan datos históricos de partidos con información actual obtenida a través de una API externa, permitiendo enriquecer el análisis y aportar una visión más completa.

---

## 📊 Fuentes de datos

### Dataset
- **Nombre:** club-football-match-data-2000-2025  
- Contiene información de partidos:
  - Equipos
  - Resultados (victoria local, visitante o empate)
  - Goles anotados
  - Estadísticas del partido

### API
- **Fuente:** https://www.football-data.org/  
- Se utilizó para obtener:
  - Competiciones (ligas)
  - Equipos actuales
  - Clasificación (standings) de la Premier League

---

## ❓ Preguntas de investigación

1. ¿Los equipos locales tienen ventaja sobre los visitantes?  
2. ¿Qué equipos anotan más goles?  
3. ¿Varía la cantidad de goles según la liga?  
4. ¿Cambia la distribución de resultados según la liga?  

---

## 🧪 Metodología

### 🔹 Data Cleaning
Se aplicaron varias técnicas de limpieza:

- Eliminación de valores nulos (`dropna`)
- Eliminación de duplicados (`drop_duplicates`)
- Conversión de tipos de datos (fechas)
- Selección de columnas relevantes
- Creación de nuevas variables

- Se creó la variable:
  - **TotalGoals = FTHome + FTAway**

### 🔹 Análisis
Se utilizaron técnicas de:
- Agrupación (`groupby`)
- Cálculo de promedios
- Conteo de resultados
- Comparaciones entre ligas y equipos

### 🔹 Integración de API
Se conectó con football-data.org para:

- Obtener competiciones disponibles
- Extraer equipos de la Premier League
- Analizar la clasificación actual (standings)

---

## 📈 Principales hallazgos

- Los equipos locales ganan con mayor frecuencia (~44%), lo que confirma la ventaja de jugar en casa.
- Existen equipos que destacan por su capacidad goleadora (ej: Barcelona, Real Madrid).
- El promedio de goles varía entre ligas, mostrando estilos de juego diferentes.
- La distribución de resultados (victorias/empates/derrotas) cambia según la competición.
- La Premier League cuenta con 20 equipos, validado mediante la API.
- Equipos como Arsenal y Manchester City destacan en la clasificación actual.

---

## 🧠 Conclusiones

El análisis confirma que:

- Existe una ventaja clara para los equipos locales.
- El rendimiento ofensivo varía entre equipos y ligas.
- Las distintas ligas presentan comportamientos únicos en términos de goles y resultados.
- La integración con API permite complementar el análisis histórico con datos actuales, enriqueciendo la interpretación de los resultados.

---

## 🚀 Trabajo futuro

- Incluir más ligas y competiciones
- Analizar métricas avanzadas (expected goals, posesión, etc.)
- Integrar más endpoints de la API
- Realizar modelos predictivos de resultados

---

## 🔗 Fuentes

- Dataset: (https://www.kaggle.com/datasets/adamgbor/club-football-match-data-2000-2025/discussion?sort=hotness)  
- API: https://www.football-data.org/  

---

## 🛠️ Tecnologías utilizadas

- Python
- Pandas
- Requests
- Jupyter Notebook

---

## 📌 Notas

- La API utilizada requiere autenticación mediante API Key.
- Se respetaron las buenas prácticas de uso de datos y APIs.