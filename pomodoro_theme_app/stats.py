"""
Statistiche persistenti tra le sessioni, salvate in un file JSON locale.
Nota: su hosting effimeri (es. Streamlit Community Cloud) il file può
essere resettato a ogni redeploy, ma persiste durante la vita dell'istanza.
"""
import json
import os
from datetime import date

STATS_PATH = os.path.join(os.path.dirname(__file__), "data", "stats.json")

DEFAULT_STATS = {
    "themes": {},        # es: {"f1": {"pomodori_totali": 12, "milestone_completate": 2}}
    "streak_giorni": 0,
    "ultimo_giorno_attivo": None,
    "storico_giornaliero": {},   # {"2026-07-10": 4, ...} pomodori completati per giorno
    "quiz": {"corrette": 0, "totali": 0},
    "album": [],                 # lista di curiosità sbloccate (uniche)
}


def _ensure_dir():
    os.makedirs(os.path.dirname(STATS_PATH), exist_ok=True)


def load_stats():
    _ensure_dir()
    if not os.path.exists(STATS_PATH):
        return json.loads(json.dumps(DEFAULT_STATS))
    try:
        with open(STATS_PATH, "r") as f:
            loaded = json.load(f)
    except (json.JSONDecodeError, OSError):
        return json.loads(json.dumps(DEFAULT_STATS))
    # backfill eventuali chiavi mancanti (es. dopo un aggiornamento dell'app)
    merged = json.loads(json.dumps(DEFAULT_STATS))
    merged.update(loaded)
    return merged


def save_stats(stats):
    _ensure_dir()
    with open(STATS_PATH, "w") as f:
        json.dump(stats, f, indent=2)


def register_pomodoro(stats, theme_key):
    theme_stats = stats["themes"].setdefault(
        theme_key, {"pomodori_totali": 0, "milestone_completate": 0}
    )
    theme_stats["pomodori_totali"] += 1

    today = date.today().isoformat()
    stats["storico_giornaliero"][today] = stats["storico_giornaliero"].get(today, 0) + 1

    if stats["ultimo_giorno_attivo"] != today:
        stats["streak_giorni"] = (
            stats["streak_giorni"] + 1 if _was_yesterday(stats["ultimo_giorno_attivo"]) else 1
        )
        stats["ultimo_giorno_attivo"] = today

    save_stats(stats)
    return stats


def register_milestone(stats, theme_key):
    theme_stats = stats["themes"].setdefault(
        theme_key, {"pomodori_totali": 0, "milestone_completate": 0}
    )
    theme_stats["milestone_completate"] += 1
    save_stats(stats)
    return stats


def register_quiz_answer(stats, correct):
    stats["quiz"]["totali"] += 1
    if correct:
        stats["quiz"]["corrette"] += 1
    save_stats(stats)
    return stats


def unlock_fact(stats, fact_text, theme_label):
    entry = {"testo": fact_text, "tema": theme_label}
    if entry not in stats["album"]:
        stats["album"].append(entry)
        save_stats(stats)
    return stats


def recent_daily_history(stats, days=14):
    """Ritorna una lista di (data, conteggio) per gli ultimi N giorni, per il grafico."""
    from datetime import timedelta
    today = date.today()
    result = []
    for i in range(days - 1, -1, -1):
        d = (today - timedelta(days=i)).isoformat()
        result.append((d, stats["storico_giornaliero"].get(d, 0)))
    return result


def _was_yesterday(iso_date_str):
    if not iso_date_str:
        return False
    from datetime import datetime, timedelta
    try:
        d = datetime.fromisoformat(iso_date_str).date()
    except ValueError:
        return False
    return d == date.today() - timedelta(days=1)
