"""
Elenco degli "avatar" selezionabili: atleti reali usati solo come nome/numero
di maglia per personalizzare l'esperienza (nessuna immagine realistica delle
persone viene generata, solo badge stilizzati con iniziali e numero).

Dati aggiornati a luglio 2026 (stagione F1 2026, Serie A 2025/26, WNBA 2026).
Le rose sportive cambiano spesso: se qualche informazione risulta superata,
basta aggiornare la voce corrispondente qui sotto.
"""

# --- Formula 1: i piloti delle 5 scuderie attualmente in testa al mondiale
# costruttori 2026 (Mercedes, Ferrari, McLaren, Red Bull, Alpine). ---
F1_AVATARS = [
    {"name": "Kimi Antonelli", "team": "Mercedes", "number": "12", "color": "#00A19C"},
    {"name": "George Russell", "team": "Mercedes", "number": "63", "color": "#00A19C"},
    {"name": "Lewis Hamilton", "team": "Ferrari", "number": "44", "color": "#E10600"},
    {"name": "Charles Leclerc", "team": "Ferrari", "number": "16", "color": "#E10600"},
    {"name": "Lando Norris", "team": "McLaren", "number": "4", "color": "#FF8000"},
    {"name": "Oscar Piastri", "team": "McLaren", "number": "81", "color": "#FF8000"},
    {"name": "Max Verstappen", "team": "Red Bull", "number": "1", "color": "#1E41FF"},
    {"name": "Isack Hadjar", "team": "Red Bull", "number": "6", "color": "#1E41FF"},
    {"name": "Pierre Gasly", "team": "Alpine", "number": "10", "color": "#00A1E8"},
    {"name": "Franco Colapinto", "team": "Alpine", "number": "43", "color": "#00A1E8"},
]

# --- Calcio: alcuni giocatori chiave per squadra (stagione 2025/26). ---
CALCIO_AVATARS = {
    "inter": [
        {"name": "Lautaro Martínez", "role": "Capitano · Attaccante", "number": "10"},
        {"name": "Marcus Thuram", "role": "Attaccante", "number": "9"},
        {"name": "Nicolò Barella", "role": "Centrocampista", "number": "23"},
        {"name": "Alessandro Bastoni", "role": "Difensore", "number": "95"},
        {"name": "Hakan Çalhanoğlu", "role": "Centrocampista", "number": "20"},
        {"name": "Federico Dimarco", "role": "Difensore", "number": "32"},
    ],
    "milan": [
        {"name": "Mike Maignan", "role": "Capitano · Portiere", "number": "16"},
        {"name": "Theo Hernández", "role": "Difensore", "number": "19"},
        {"name": "Rafael Leão", "role": "Attaccante", "number": "10"},
        {"name": "Christian Pulisic", "role": "Attaccante"},
    ],
    "juventus": [
        {"name": "Kenan Yıldız", "role": "Attaccante", "number": "10"},
        {"name": "Andrea Cambiaso", "role": "Difensore"},
        {"name": "Manuel Locatelli", "role": "Centrocampista"},
        {"name": "Francisco Conceição", "role": "Attaccante"},
    ],
    "napoli": [
        {"name": "Giovanni Di Lorenzo", "role": "Capitano · Difensore", "number": "22"},
        {"name": "Scott McTominay", "role": "Centrocampista"},
        {"name": "Stanislav Lobotka", "role": "Centrocampista", "number": "68"},
        {"name": "Matteo Politano", "role": "Attaccante", "number": "21"},
    ],
    "roma": [
        {"name": "Stephan El Shaarawy", "role": "Capitano · Attaccante", "number": "92"},
        {"name": "Paulo Dybala", "role": "Attaccante", "number": "21"},
        {"name": "Bryan Cristante", "role": "Centrocampista", "number": "4"},
    ],
}

# --- Basket femminile: alcune delle stelle WNBA 2026. ---
BASKET_AVATARS = [
    {"name": "Paige Bueckers", "team": "Dallas Wings", "number": "5"},
    {"name": "Azzi Fudd", "team": "Dallas Wings", "number": "35"},
    {"name": "A'ja Wilson", "team": "Las Vegas Aces", "number": "22"},
    {"name": "Caitlin Clark", "team": "Indiana Fever", "number": "22"},
    {"name": "Angel Reese", "team": "Atlanta Dream"},
    {"name": "Breanna Stewart", "team": "New York Liberty", "number": "30"},
]

# --- Tennis: alcuni dei migliori giocatori/giocatrici ATP e WTA (luglio 2026). ---
TENNIS_AVATARS = [
    {"name": "Jannik Sinner", "team": "ATP · n.1 mondo", "color": "#0072CE"},
    {"name": "Carlos Alcaraz", "team": "ATP · n.2 mondo", "color": "#FF4B00"},
    {"name": "Alexander Zverev", "team": "ATP · n.3 mondo", "color": "#DA291C"},
    {"name": "Novak Djokovic", "team": "ATP · top 10", "color": "#0C3C74"},
    {"name": "Aryna Sabalenka", "team": "WTA · n.1 mondo", "color": "#FFD100"},
    {"name": "Iga Świątek", "team": "WTA · top 5", "color": "#D2001C"},
    {"name": "Jasmine Paolini", "team": "WTA · top 15", "color": "#008C45"},
    {"name": "Elena Rybakina", "team": "WTA · top 5", "color": "#00A19C"},
]