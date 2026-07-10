"""
Configurazione dei temi per il Pomodoro Tematico.
Per aggiungere un nuovo tema basta aggiungere una nuova entry al dict THEMES:
non serve toccare la logica dell'app.
"""

THEMES = {
    "f1": {
        "label": "🏎️ Formula 1",
        "primary": "#E10600",      # rosso F1
        "secondary": "#15151E",    # nero paddock
        "accent": "#FFFFFF",
        "unit_name": "Settore",
        "unit_name_plural": "Settori",
        "units_per_session": 3,          # 1 pomodoro = 1 giro = 3 settori
        "session_label": "Giro",
        "milestone_label": "Gran Premio",
        "milestone_sessions": 4,         # dopo 4 pomodori = 1 GP completato
        "break_label": "Pit Stop",
        "long_break_label": "Bandiera a scacchi",
        "start_cta": "Semaforo spento, si parte!",
        "sound": "pit_stop",
        "facts": [
            "Il record di pole position appartiene a Lewis Hamilton, con oltre 100 pole in carriera.",
            "Un pit stop ai vertici dura oggi meno di 2 secondi per il cambio delle quattro gomme.",
            "Monza è conosciuta come il 'Tempio della Velocità' per le sue lunghe rettilinee.",
            "La power unit ibrida della F1 moderna recupera energia sia in frenata che dai gas di scarico (MGU-K e MGU-H).",
            "Il Gran Premio di Monaco è l'unico che si corre ancora su un tracciato cittadino praticamente invariato dal 1929.",
            "Il DRS (Drag Reduction System) può essere attivato solo in zone specifiche del tracciato e solo se si è entro 1 secondo dall'auto davanti.",
            "Max Verstappen ha vinto il titolo mondiale per la prima volta nel 2021, all'ultimo giro dell'ultima gara.",
            "Le monoposto di F1 possono generare una forza di carico aerodinamico tale da poter, in teoria, guidare a testa in giù a velocità elevate.",
        ],
        "milestone_message": "Hai tagliato il traguardo! Gran Premio completato 🏁",
    },
    "calcio": {
        "label": "⚽ Calcio",
        "unit_name": "Minuto",
        "unit_name_plural": "Minuti",
        "units_per_session": 45,         # 1 pomodoro = 1 tempo di gioco (45')
        "session_label": "Tempo",
        "milestone_label": "Partita",
        "milestone_sessions": 2,         # 2 pomodori = partita completa (2 tempi)
        "break_label": "Intervallo",
        "long_break_label": "Triplice fischio",
        "start_cta": "Fischio d'inizio!",
        "sound": "whistle",
        # tema "genitore": la squadra si sceglie a parte (vedi TEAMS sotto)
        "has_teams": True,
        "default_team": "inter",
    },
    "basket": {
        "label": "🏀 WNBA",
        "primary": "#FF6B00",      # arancio basket
        "secondary": "#1D1160",    # viola WNBA
        "accent": "#FFFFFF",
        "unit_name": "Minuto",
        "unit_name_plural": "Minuti",
        "units_per_session": 10,         # 1 pomodoro = 1 quarto (10')
        "session_label": "Quarto",
        "milestone_label": "Partita",
        "milestone_sessions": 4,         # 4 quarti = partita
        "break_label": "Time-out",
        "long_break_label": "Buzzer finale",
        "start_cta": "Palla a due!",
        "sound": "buzzer",
        "facts": [
            "Paige Bueckers ha vinto il premio di National Player of the Year al suo primo anno a UConn, nel 2021.",
            "Bueckers è stata scelta come numero 1 assoluta al Draft WNBA, coronando un percorso da protagonista sin dai tempi del college.",
            "La WNBA è stata fondata nel 1996 ed è iniziata a giocare ufficialmente nel 1997.",
            "UConn, la squadra universitaria di Bueckers, è uno dei programmi di basket femminile più vincenti nella storia NCAA.",
            "Nel basket femminile il tiro da 3 punti è stato introdotto ufficialmente nella NCAA nel 1987.",
            "Il premio 'Sixth Woman of the Year' premia la miglior giocatrice che parte dalla panchina in WNBA.",
        ],
        "milestone_message": "Buzzer finale: partita completata! 🏀",
    },
    "tennis": {
        "label": "🎾 Tennis",
        "primary": "#C6E200",       # giallo pallina
        "secondary": "#0B3D2E",     # verde campo
        "accent": "#FFFFFF",
        "unit_name": "Game",
        "unit_name_plural": "Game",
        "units_per_session": 6,          # 1 pomodoro = 1 set (6 game)
        "session_label": "Set",
        "milestone_label": "Match",
        "milestone_sessions": 3,         # 3 set vinti = match completato
        "break_label": "Cambio campo",
        "long_break_label": "Match Point",
        "start_cta": "Palla in gioco!",
        "sound": "bounce",
        "facts": [
            "Il tie-break fu introdotto per evitare set interminabili: si gioca quando il punteggio arriva a 6-6 nei game.",
            "Wimbledon è l'unico Slam ancora giocato sull'erba tra i quattro tornei del Grande Slam.",
            "Il punteggio del tennis (15, 30, 40) deriva probabilmente da un antico sistema francese legato al quadrante di un orologio.",
            "Novak Djokovic, Rafael Nadal e Roger Federer si sono spartiti la maggior parte degli Slam nel ventennio 2003-2023.",
            "Nel 2026 Jannik Sinner guida il ranking ATP, portando l'Italia ad avere il maggior numero di giocatori italiani in top 100 di sempre.",
            "Il Roland Garros si gioca sulla terra rossa, superficie che rallenta la palla e favorisce scambi più lunghi.",
            "Il 'Golden Slam' (vincere i 4 Slam più l'oro olimpico nello stesso anno) è stato completato solo da Steffi Graf nel 1988.",
        ],
        "milestone_message": "Match Point: partita vinta! 🎾",
    },
}

# Squadre selezionabili per il tema "calcio". Ogni voce fornisce solo i dati
# che cambiano da squadra a squadra (colori, nome, curiosità); la meccanica
# resta quella definita in THEMES["calcio"].
TEAMS = {
    "inter": {
        "label": "🖤💙 Inter",
        "primary": "#010E80",
        "secondary": "#000000",
        "accent": "#F5C400",
        "facts": [
            "L'Inter è l'unico club italiano ad aver sempre militato in Serie A dalla fondazione della competizione.",
            "Il triplete stagione 2009-10 (Scudetto, Coppa Italia, Champions League) resta unico nella storia del club, sotto la guida di José Mourinho.",
            "Giuseppe Meazza, a cui è dedicato lo stadio di San Siro, ha vestito la maglia nerazzurra per oltre un decennio.",
            "Il soprannome 'Beneamata' venne coniato dal giornalista Gianni Brera per descrivere l'affetto dei tifosi interisti.",
            "Javier Zanetti ha collezionato più di 600 presenze con la maglia dell'Inter, record assoluto per il club.",
            "L'Inter è stata fondata nel 1908 da un gruppo di soci dissidenti del Milan Cricket and Football Club.",
        ],
    },
    "milan": {
        "label": "🔴⚫ Milan",
        "primary": "#FB090B",
        "secondary": "#000000",
        "accent": "#FFFFFF",
        "facts": [
            "Il Milan è, insieme al Real Madrid, uno dei club con più Coppe dei Campioni/Champions League vinte nella storia.",
            "Il club fu fondato nel 1899 da un gruppo di uomini d'affari inglesi, da cui il nome in inglese 'Milan' anziché 'Milano'.",
            "Paolo Maldini ha giocato per il Milan per l'intera carriera, oltre 25 anni ai massimi livelli.",
            "Lo stadio San Siro è condiviso con l'Inter dal 1947 ed è ufficialmente intitolato a Giuseppe Meazza.",
            "Il Milan vinse tre Palloni d'Oro consecutivi con giocatori diversi tra il 1988 e il 1990 (Van Basten e Gullit).",
        ],
    },
    "juventus": {
        "label": "⚪⚫ Juventus",
        "primary": "#000000",
        "secondary": "#1A1A1A",
        "accent": "#FFFFFF",
        "facts": [
            "La Juventus è il club italiano con più scudetti vinti nella storia della Serie A.",
            "Le strisce bianconere furono adottate nel 1903, ispirate alla maglia del Notts County, club inglese.",
            "Alessandro Del Piero ha giocato oltre 700 partite con la maglia della Juventus, record del club.",
            "Lo Juventus Stadium, oggi Allianz Stadium, è stato il primo stadio di proprietà di un club in Serie A.",
            "Gianluigi Buffon ha difeso i pali della Juventus per la maggior parte della sua lunghissima carriera.",
        ],
    },
    "napoli": {
        "label": "🩵 Napoli",
        "primary": "#12A0D7",
        "secondary": "#003366",
        "accent": "#FFFFFF",
        "facts": [
            "Diego Armando Maradona ha portato il Napoli a vincere i suoi primi due scudetti, nel 1987 e nel 1990.",
            "Il Napoli ha vinto lo scudetto 2022-23 sotto la guida tecnica di Luciano Spalletti, dopo 33 anni di attesa.",
            "Lo stadio del Napoli è stato intitolato a Diego Armando Maradona nel 2020.",
            "Il Napoli è stato fondato nel 1926 dalla fusione di due club calcistici partenopei.",
        ],
    },
    "roma": {
        "label": "🟠🔴 Roma",
        "primary": "#8E1F2F",
        "secondary": "#F0BC42",
        "accent": "#FFFFFF",
        "facts": [
            "La Roma è stata fondata nel 1927 dalla fusione di tre squadre calcistiche della capitale.",
            "Francesco Totti ha giocato per la Roma per l'intera carriera, diventandone il simbolo assoluto.",
            "Lo stadio Olimpico, che la Roma condivide con la Lazio, ha ospitato la finale dei Mondiali del 1990.",
            "La Roma ha vinto la UEFA Conference League nel 2022, primo trofeo europeo della sua storia.",
        ],
    },
}

# Mini-quiz mostrato durante le pause (una domanda a caso per pausa).
# "correct" è l'indice (0-based) dell'opzione giusta in "options".
QUIZ = {
    "f1": [
        {
            "q": "Quante gomme vengono cambiate in un pit stop standard?",
            "options": ["2", "4", "6"],
            "correct": 1,
        },
        {
            "q": "Cosa significa DRS?",
            "options": ["Drag Reduction System", "Direct Race Steering", "Driver Response System"],
            "correct": 0,
        },
        {
            "q": "In quale città si corre il GP più prestigioso su circuito cittadino?",
            "options": ["Singapore", "Monaco", "Baku"],
            "correct": 1,
        },
        {
            "q": "Quanti punti vale il primo posto in un GP (dal 2010)?",
            "options": ["20", "25", "30"],
            "correct": 1,
        },
        {
            "q": "Cosa indica la bandiera a scacchi?",
            "options": ["Pericolo in pista", "Fine della sessione/gara", "Pit stop obbligatorio"],
            "correct": 1,
        },
    ],
    "calcio": [
        {
            "q": "Quanto dura un tempo regolamentare di una partita di calcio?",
            "options": ["40 minuti", "45 minuti", "50 minuti"],
            "correct": 1,
        },
        {
            "q": "Da quale distanza si tira un calcio di rigore?",
            "options": ["9 metri", "11 metri", "13 metri"],
            "correct": 1,
        },
        {
            "q": "Quanti giocatori ha in campo una squadra (portiere incluso)?",
            "options": ["10", "11", "12"],
            "correct": 1,
        },
        {
            "q": "Cosa comporta il secondo cartellino giallo nella stessa partita?",
            "options": ["Nulla", "Espulsione", "Rigore per l'avversario"],
            "correct": 1,
        },
        {
            "q": "Come si chiama il torneo europeo per club più prestigioso?",
            "options": ["Europa League", "Champions League", "Conference League"],
            "correct": 1,
        },
    ],
    "basket": [
        {
            "q": "Quanti punti vale un canestro da oltre l'arco?",
            "options": ["2", "3", "4"],
            "correct": 1,
        },
        {
            "q": "Quanti giocatori per squadra sono in campo contemporaneamente?",
            "options": ["4", "5", "6"],
            "correct": 1,
        },
        {
            "q": "Quanti secondi ha una squadra per tirare a canestro (regola dei 24s)?",
            "options": ["24 secondi", "30 secondi", "18 secondi"],
            "correct": 0,
        },
        {
            "q": "Come si chiama il fallo commesso in attacco travolgendo un difensore fermo?",
            "options": ["Fallo antisportivo", "Fallo di sfondamento (charging)", "Fallo tecnico"],
            "correct": 1,
        },
        {
            "q": "In quale lega gioca Paige Bueckers a livello professionistico?",
            "options": ["WNBA", "EuroLega Femminile", "NCAA"],
            "correct": 0,
        },
    ],
    "tennis": [
        {
            "q": "A quanti game si vince un set (senza tie-break)?",
            "options": ["4", "6", "8"],
            "correct": 1,
        },
        {
            "q": "Su quale superficie si gioca il Roland Garros?",
            "options": ["Erba", "Terra rossa", "Cemento"],
            "correct": 1,
        },
        {
            "q": "Come si chiama il punteggio di parità a 40-40?",
            "options": ["Deuce", "Tie-break", "Match point"],
            "correct": 0,
        },
        {
            "q": "Quanti Slam compongono il Grande Slam nel tennis?",
            "options": ["3", "4", "5"],
            "correct": 1,
        },
        {
            "q": "A quanti punti scatta il tie-break nel punteggio dei game?",
            "options": ["5-5", "6-6", "7-7"],
            "correct": 1,
        },
    ],
}

DEFAULT_SETTINGS = {
    "work_minutes": 25,
    "short_break_minutes": 5,
    "long_break_minutes": 15,
}
