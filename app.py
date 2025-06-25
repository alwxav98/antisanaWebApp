<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Análisis de Problemas - Antisana</title>
  <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.3/dist/leaflet.css"/>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap" rel="stylesheet">
  <style>
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    body {
      font-family: 'Inter', sans-serif;
      background-color: #f9f9f9;
      color: #333;
    }

    nav {
      background-color: #003366;
      color: white;
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 1rem 2rem;
    }

    nav .brand {
      font-weight: bold;
      font-size: 20px;
    }

    nav .menu a {
      color: white;
      text-decoration: none;
      margin-left: 20px;
      font-weight: 500;
      transition: color 0.2s;
    }

    nav .menu a:hover {
      color: #ffcc00;
    }

    .content {
      max-width: 900px;
      margin: 40px auto;
      padding: 20px;
      background: white;
      border-radius: 8px;
      box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }

    .content h1 {
      color: #005cbf;
      font-size: 26px;
      margin-bottom: 20px;
    }

    .content p {
      font-size: 16px;
      line-height: 1.8;
      margin-bottom: 20px;
    }

    .content ul {
      margin-left: 20px;
      margin-bottom: 20px;
    }

    .content ul li {
      margin-bottom: 10px;
    }

    .back-button {
      display: inline-block;
      margin-top: 20px;
      text-decoration: none;
      color: white;
      background-color: #007BFF;
      padding: 10px 20px;
      border-radius: 5px;
      font-weight: bold;
    }

    .back-button:hover {
      background-color: #0056b3;
    }

    @media (max-width: 768px) {
      nav {
        flex-direction: column;
        align-items: flex-start;
      }

      nav .menu {
        margin-top: 0.5rem;
      }

      .content {
        margin: 20px;
      }
    }
  </style>
</head>
<body>

  <!-- Navegación -->
  <nav>
    <div class="brand">🌐 Proyecto Antisana</div>
    <div class="menu">
      <a href="/">🏠 Inicio</a>
      <a href="/mapa">🗺️ Mapa</a>
      <a href="/analisis">📉 Análisis</a>
      <a href="/solucion">💡 Solución</a>
      <a href="/visualizacion">📊 Visualización</a>
    </div>
  </nav>

  <!-- Contenido -->
  <div class="content">
    <h1>📉 Análisis del Problema de Incompletitud de Datos</h1>

    <p>
      Durante el monitoreo hidrometeorológico del Antisana, se ha identificado una problemática recurrente:
      muchos de los sensores instalados para recolectar datos como precipitación, caudal y nivel de agua
      no proporcionan información completa o continua.
    </p>

    <p>
      Estos vacíos en los datos pueden deberse a fallas técnicas, interrupciones en la alimentación eléctrica,
      problemas de conectividad, condiciones climáticas extremas o incluso errores de almacenamiento.
    </p>

    <p>
      La existencia de datos faltantes impide realizar análisis confiables y afecta la toma de decisiones en
      relación con la gestión del recurso hídrico. Por ello, este sistema plantea como objetivo principal:
    </p>

    <ul>
      <li>🔍 Detectar brechas en los datos provenientes de sensores.</li>
      <li>📈 Visualizar gráficamente los períodos sin información.</li>
      <li>🧠 Proponer soluciones tecnológicas como sensores redundantes, interpolación de datos o mantenimiento predictivo.</li>
      <li>⚙️ Implementar herramientas que permitan predecir datos perdidos usando modelos estadísticos o de IA.</li>
    </ul>

  </div>

</body>
</html>
