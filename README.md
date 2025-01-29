# FLGMet-Obs (Station d'observation Météo automatique adaptée à l'aéronautique)

Cette application fournit des données météo en temps réel à partir d'une station météo utilisant un ESP32 et des capteurs tels que SHT35, SPS30, etc. Les données sont envoyées via WebSocket à une interface web, et stockées dans une base de données PostgreSQL.

## Prérequis

- ESP32
- Django 4.1+
- PostgreSQL
- Python 3.7+

## Installation

### Backend

1. Installe les dépendances :

```bash
pip install -r requirements.txt
