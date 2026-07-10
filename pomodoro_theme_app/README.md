# Pomodoro Tematico ⏱️

App Streamlit per studiare con il metodo Pomodoro, dove ogni pausa ha un
motivo valido legato al tuo tema preferito: Formula 1, calcio (con scelta
della squadra), basket femminile (Paige Bueckers / WNBA) o tennis (ATP/WTA).

## Come funziona

- Ogni **pomodoro** (sessione di studio) corrisponde a un'unità narrativa del
  tema: un giro in F1, un tempo di gioco nel calcio, un quarto nel basket.
- Il tema **calcio** è generico: scegli la squadra (Inter, Milan, Juventus,
  Napoli, Roma...) dalla sidebar e colori/curiosità si aggiornano di
  conseguenza, senza cambiare la meccanica del timer.
- **Avatar**: scegli il tuo pilota/giocatore/giocatrice preferito dalla sidebar.
  Per la F1 sono i 10 piloti delle 5 scuderie attualmente in testa al mondiale
  costruttori 2026 (Mercedes, Ferrari, McLaren, Red Bull, Alpine); per il
  calcio dipende dalla squadra scelta (rosa aggiornata 2025/26); per il
  basket alcune stelle WNBA 2026 (Paige Bueckers, Azzi Fudd, A'ja Wilson,
  Caitlin Clark, Angel Reese, Breanna Stewart). L'avatar è un **badge
  stilizzato** (iniziali, numero, colori) e non un'immagine realistica della
  persona — scelta voluta per restare originali e senza problemi di
  copyright/diritti d'immagine.
- **Timer ad anello animato** con i colori del tema, e sotto una **scena SVG**
  originale (pista F1 / campo da calcio / campo da basket) che si anima in
  base al progresso della sessione — nessuna immagine esterna, quindi
  nessun problema di copyright, tutto disegnato a codice.
- A fine sessione parte un **suono a tema** (sintetizzato) e durante la pausa
  ti aspetta un **quiz lampo** a scelta multipla sul tema, seguito da una
  **curiosità random**, che viene salvata nell'**Album curiosità** (seconda
  scheda dell'app) come una collezione di figurine.
- Al completamento di una **milestone** (Gran Premio / Partita) parte
  un'animazione di **coriandoli** e viene generata una **card di riepilogo**
  in PNG, scaricabile.
- Le statistiche (pomodori totali, milestone completate, punteggio quiz,
  streak di giorni attivi, e un **grafico degli ultimi 14 giorni**) sono
  persistenti tra le sessioni, salvate in `data/stats.json`.

- L'app parte con il **tema scuro** di default (config in `.streamlit/config.toml`)
  e i pulsanti di controllo (Avvia/Pausa/Reset/Salta pausa) sono centrati
  rispetto alla pagina.

## Setup

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Aggiungere un nuovo tema

Basta aggiungere una nuova voce al dizionario `THEMES` in `themes.py`:
colori, nome delle unità (es. "giro", "quarto"), numero di pomodori per
milestone, e una lista di curiosità. Non serve toccare `app.py`.

## Aggiungere una nuova squadra (tema calcio)

Aggiungi una voce al dizionario `TEAMS` in `themes.py` con `label`,
`primary`/`secondary`/`accent` (colori sociali) e una lista di `facts`.
Comparirà automaticamente nel selettore squadra in sidebar.

## Struttura del progetto

```
app.py            # UI e logica del timer (Streamlit)
themes.py         # config dei temi, squadre e banca domande quiz
avatars.py         # elenco piloti/giocatori/giocatrici selezionabili come avatar
avatar_badge.py     # generazione badge SVG stilizzato per l'avatar scelto
svg_scenes.py      # scene SVG animate (pista/campo/canestro), generate a codice
sound_utils.py     # generazione suoni sintetizzati (pit-stop, fischio, buzzer)
card_utils.py      # generazione card di riepilogo con PIL
stats.py           # persistenza statistiche, storico, quiz e album su file JSON
data/stats.json    # creato automaticamente al primo utilizzo
```

## Note

- Su hosting effimeri (es. Streamlit Community Cloud) `data/stats.json`
  persiste durante la vita dell'istanza ma può azzerarsi a un redeploy.
  Per persistenza definitiva servirebbe un database esterno (facilmente
  aggiungibile in un secondo momento).
- Le rose sportive (piloti F1, giocatori Serie A, roster WNBA) in `avatars.py`
  sono aggiornate a luglio 2026 ma cambiano nel tempo (trasferimenti,
  infortuni, nuove stagioni): basta modificare le liste in quel file quando
  serve un aggiornamento.
