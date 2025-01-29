# FLGMet-Obs (Station d'observation Météo automatique adaptée à l'aéronautique)

**FLGMet-Obs : L’Observation Météo au Sol, Pilier de l’Aéronautique !**  
Découvrez un projet unique dédié à l’**observation météorologique au sol**, conçu pour optimiser la sécurité et l’efficacité des opérations aéronautiques ! **FLGMet-Obs** met à votre disposition des technologies de pointe et des données ultra-précises pour analyser les conditions terrestres essentielles aux décollages, atterrissages et manœuvres au sol.  

Imaginez accéder à des **relevés en temps réel** : température, vitesse et direction du vent, visibilité, pression atmosphérique… Autant de paramètres critiques mesurés par des capteurs intelligents, des stations météo connectées et des réseaux de passionnés. Ces données, vitales pour les pilotes, les contrôleurs aériens ou les préparateurs de vol, sont visualisables sur une interface interactive, avec des alertes personnalisables pour anticiper les risques (brouillard, rafales, etc.).  

Il est important de noter que toutt repose sur les normes OMM et OACI.

Rejoignez une communauté où chaque observation au sol compte : que vous soyez spotteur d’orages, technicien aéroportuaire ou simple passionné, votre contribution éclaire les décisions qui font voler l’aéronautique plus haut. **Parce qu’un ciel maîtrisé commence par une terre observée !** 🌦️🛫

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
