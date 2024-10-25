# MDV - Modelo Predicción para Ventas

![Logo de la Empresa](logo.jpg)

**Segmenta, Analiza y encuentra Oportunidades en el Mercado de la Tecnología**

Este proyecto es una aplicación web diseñada para predecir tendencias de ventas en sectores específicos del mercado de la tecnología, permitiendo analizar el comportamiento del mercado y detectar oportunidades basadas en datos históricos.

## Tabla de Contenidos

- [Descripción](#descripción)
- [Características](#características)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Configuración de Apache en Debian](#configuración-de-apache-en-debian)
- [Uso](#uso)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)

---

## Descripción

MDV - Modelo Predicción para Ventas permite segmentar datos de mercado y realizar predicciones de ventas usando técnicas de machine learning. Esta herramienta está orientada a emprendedores y empresarios que operan en el sector B2B, proporcionando análisis predictivo para ajustar las estrategias de ventas.

## Características

- Segmentación del mercado en sectores específicos de la tecnología.
- Predicciones de tendencias de ventas a corto y mediano plazo.
- Gráficos visuales de las predicciones.
- Soporte para CORS, permitiendo la integración entre frontend y backend.
- Desplegable de sectores personalizable en el frontend.

## Requisitos

- **Python** >= 3.7
- **Flask** >= 1.1.2
- **Apache** con módulo **mod_wsgi** (para despliegue en servidor)
- Librerías: `flask`, `flask-cors`, `numpy`, `pandas`, `matplotlib`, `prophet`

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/usuario/mdv-prediccion-ventas.git
   cd mdv-prediccion-ventas
