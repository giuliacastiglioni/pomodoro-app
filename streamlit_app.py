import random
import time

import streamlit as st
import streamlit.components.v1 as components

from themes import THEMES, TEAMS, QUIZ, DEFAULT_SETTINGS
from avatars import F1_AVATARS, CALCIO_AVATARS, BASKET_AVATARS, TENNIS_AVATARS
from avatar_badge import render_avatar_badge
from sound_utils import get_break_sound, milestone_sound
from card_utils import generate_recap_card
from svg_scenes import render_scene
import stats as stats_mod

st.set_page_config(page_title="Pomodoro", page_icon="⏱️", layout="centered")

# ---------------------------------------------------------------------------
# Stato iniziale
# ---------------------------------------------------------------------------
_DEFAULTS = {
    "theme_key": "f1",
    "phase": "idle",              # idle | work | short_break | long_break
    "phase_end": None,
    "phase_duration": 0,
    "cycle_count": 0,             # pomodori completati dall'ultima milestone
    "pending_sound": None,
    "pending_fact": None,
    "show_recap": False,
    "show_confetti": False,
    "quiz_question": None,
    "quiz_answered": False,
    "quiz_selected": None,
    "avatar_index": 0,
    "persist_stats": None,
    "settings": None,
}
for key, default in _DEFAULTS.items():
    if key not in st.session_state:
        st.session_state[key] = default
if "team_key" not in st.session_state:
    st.session_state.team_key = THEMES["calcio"]["default_team"]
if st.session_state.settings is None:
    st.session_state.settings = dict(DEFAULT_SETTINGS)
if st.session_state.persist_stats is None:
    st.session_state.persist_stats = stats_mod.load_stats()


def resolve_active_theme():
    """Combina il tema base con i dati della squadra, se il tema li prevede."""
    base = THEMES[st.session_state.theme_key]
    if not base.get("has_teams"):
        return base, st.session_state.theme_key

    team = TEAMS[st.session_state.team_key]
    merged = dict(base)
    merged["label"] = team["label"]
    merged["primary"] = team["primary"]
    merged["secondary"] = team["secondary"]
    merged["accent"] = team["accent"]
    merged["facts"] = team["facts"]
    merged["milestone_message"] = f"Triplice fischio: partita del {team['label']} completata!"
    key = f"{st.session_state.theme_key}_{st.session_state.team_key}"
    return merged, key


theme, stats_key = resolve_active_theme()


def resolve_avatar_list():
    """Ritorna la lista di avatar disponibili per il tema/squadra corrente."""
    if st.session_state.theme_key == "f1":
        return F1_AVATARS
    if st.session_state.theme_key == "calcio":
        return CALCIO_AVATARS.get(st.session_state.team_key, [])
    if st.session_state.theme_key == "basket":
        return BASKET_AVATARS
    if st.session_state.theme_key == "tennis":
        return TENNIS_AVATARS
    return []


avatar_list = resolve_avatar_list()
if st.session_state.avatar_index >= len(avatar_list):
    st.session_state.avatar_index = 0
active_avatar = avatar_list[st.session_state.avatar_index] if avatar_list else None

# ---------------------------------------------------------------------------
# Stile dinamico in base al tema
# ---------------------------------------------------------------------------
st.markdown(
    f"""
    <style>
    .stApp {{
        background: radial-gradient(circle at 20% 0%, {theme['primary']}22 0%, transparent 45%),
                    linear-gradient(160deg, {theme['secondary']} 0%, #0a0a0f 100%);
    }}
    .theme-title {{
        color: {theme['accent']};
        font-size: 2.3rem;
        font-weight: 800;
        margin-bottom: 0;
        animation: fadeIn 0.6s ease-in;
    }}
    .theme-sub {{
        color: {theme['primary']};
        font-weight: 700;
        font-size: 1.05rem;
    }}
    .phase-badge {{
        display: inline-block;
        background: {theme['primary']};
        color: {theme['secondary']};
        padding: 5px 16px;
        border-radius: 20px;
        font-weight: 700;
        font-size: 0.9rem;
        letter-spacing: 0.5px;
    }}
    .ring-wrap {{
        width: 220px;
        height: 220px;
        border-radius: 50%;
        margin: 18px auto;
        display: flex;
        align-items: center;
        justify-content: center;
        background: conic-gradient({theme['primary']} calc(var(--pct) * 1%), {theme['secondary']}55 0);
        box-shadow: 0 0 30px {theme['primary']}44;
        transition: background 0.9s linear;
    }}
    .ring-inner {{
        width: 186px;
        height: 186px;
        border-radius: 50%;
        background: {theme['secondary']};
        display: flex;
        align-items: center;
        justify-content: center;
        flex-direction: column;
    }}
    .timer-display {{
        font-size: 2.9rem;
        font-weight: 800;
        color: {theme['accent']};
        font-family: 'Courier New', monospace;
    }}
    .fact-box {{
        background: {theme['primary']}22;
        border-left: 4px solid {theme['primary']};
        padding: 14px 18px;
        border-radius: 6px;
        color: {theme['accent']};
        font-style: italic;
        animation: fadeIn 0.5s ease-in;
    }}
    .quiz-box {{
        background: {theme['secondary']};
        border: 2px solid {theme['primary']};
        padding: 16px 18px;
        border-radius: 10px;
        color: {theme['accent']};
        margin-bottom: 10px;
    }}
    .album-card {{
        background: {theme['primary']}18;
        border: 1px solid {theme['primary']}55;
        border-radius: 10px;
        padding: 12px 16px;
        margin-bottom: 8px;
        color: {theme['accent']};
    }}
    @keyframes fadeIn {{
        from {{ opacity: 0; transform: translateY(6px); }}
        to {{ opacity: 1; transform: translateY(0); }}
    }}
    @keyframes glowPulse {{
        0%, 100% {{ box-shadow: 0 0 0px {theme['primary']}00; }}
        50% {{ box-shadow: 0 0 22px {theme['primary']}99; }}
    }}

    /* ---------------- Sidebar ---------------- */
    [data-testid="stSidebar"] {{
        background: linear-gradient(180deg, {theme['secondary']} 0%, #0a0a0f 100%);
        border-right: 1px solid {theme['primary']}33;
    }}
    [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3 {{
        color: {theme['accent']};
        letter-spacing: 0.5px;
    }}
    [data-testid="stSidebar"] label p {{
        color: {theme['accent']}cc !important;
        font-weight: 600 !important;
        font-size: 0.82rem !important;
        text-transform: uppercase;
        letter-spacing: 0.6px;
    }}
    [data-testid="stSidebar"] [data-testid="stVerticalBlockBorderWrapper"] {{
        background: {theme['primary']}14;
        border: 1px solid {theme['primary']}44 !important;
        border-radius: 16px !important;
        padding: 4px 6px;
        margin-bottom: 14px;
    }}
    [data-testid="stSidebar"] hr {{
        border-color: {theme['primary']}44;
    }}
    [data-testid="stSidebar"] [data-baseweb="select"] > div {{
        background: {theme['secondary']};
        border: 1.5px solid {theme['primary']}77 !important;
        border-radius: 10px !important;
        transition: border-color 0.2s ease, box-shadow 0.2s ease;
    }}
    [data-testid="stSidebar"] [data-baseweb="select"] > div:hover {{
        border-color: {theme['primary']} !important;
        box-shadow: 0 0 10px {theme['primary']}55;
    }}
    [data-testid="stSidebar"] [data-testid="stNumberInput"] input {{
        background: {theme['secondary']};
        color: {theme['accent']};
        border: 1.5px solid {theme['primary']}77 !important;
        border-radius: 10px !important;
    }}
    [data-testid="stSidebar"] [data-testid="stNumberInput"] button {{
        background: {theme['primary']}33 !important;
        border: 1px solid {theme['primary']}77 !important;
        color: {theme['accent']} !important;
        border-radius: 8px !important;
    }}
    [data-testid="stMetricValue"] {{
        color: {theme['accent']} !important;
        font-weight: 800 !important;
    }}
    [data-testid="stMetricLabel"] {{
        color: {theme['accent']}aa !important;
    }}

    /* ---------------- Pulsanti ---------------- */
    .stButton>button {{
        background: {theme['secondary']};
        color: {theme['accent']};
        border: 1.5px solid {theme['primary']}88;
        font-weight: 700;
        border-radius: 999px;
        padding: 0.55em 1.1em;
        letter-spacing: 0.3px;
        transition: transform 0.15s ease, box-shadow 0.2s ease, border-color 0.2s ease;
    }}
    .stButton>button:hover {{
        color: {theme['accent']};
        border-color: {theme['primary']};
        transform: translateY(-2px) scale(1.02);
        box-shadow: 0 6px 18px {theme['primary']}55;
    }}
    .stButton>button:active {{
        transform: translateY(0) scale(0.98);
    }}
    .stButton>button[kind="primary"] {{
        background: linear-gradient(135deg, {theme['primary']} 0%, {theme['primary']}cc 100%);
        color: {theme['secondary']};
        border: none;
        font-size: 1.05rem;
        animation: glowPulse 2.4s ease-in-out infinite;
    }}
    .stButton>button[kind="primary"]:hover {{
        transform: translateY(-2px) scale(1.03);
        box-shadow: 0 8px 24px {theme['primary']}88;
    }}
    .stDownloadButton>button {{
        border-radius: 999px;
        font-weight: 700;
        border: 1.5px solid {theme['primary']}88;
    }}
    [data-testid="column"] .stButton {{
        display: flex;
        justify-content: center;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------------------
# Sidebar: scelta tema + impostazioni + statistiche persistenti
# ---------------------------------------------------------------------------
with st.sidebar:
    st.markdown("## ⚙️ Impostazioni")

    with st.container(border=True):
        st.markdown("**🎨 Personalizza**")
        new_theme = st.selectbox(
            "Tema",
            options=list(THEMES.keys()),
            format_func=lambda k: THEMES[k]["label"],
            index=list(THEMES.keys()).index(st.session_state.theme_key),
        )
        if new_theme != st.session_state.theme_key and st.session_state.phase == "idle":
            st.session_state.theme_key = new_theme
            st.rerun()
        elif new_theme != st.session_state.theme_key:
            st.caption("⚠️ Metti in pausa/reset per cambiare tema durante una sessione.")

        if THEMES[st.session_state.theme_key].get("has_teams"):
            new_team = st.selectbox(
                "Squadra",
                options=list(TEAMS.keys()),
                format_func=lambda k: TEAMS[k]["label"],
                index=list(TEAMS.keys()).index(st.session_state.team_key),
            )
            if new_team != st.session_state.team_key and st.session_state.phase == "idle":
                st.session_state.team_key = new_team
                st.rerun()
            elif new_team != st.session_state.team_key:
                st.caption("⚠️ Metti in pausa/reset per cambiare squadra durante una sessione.")

        _current_avatar_list = (
            F1_AVATARS if st.session_state.theme_key == "f1"
            else CALCIO_AVATARS.get(st.session_state.team_key, []) if st.session_state.theme_key == "calcio"
            else TENNIS_AVATARS if st.session_state.theme_key == "tennis"
            else BASKET_AVATARS
        )
        if _current_avatar_list:
            avatar_labels = [f"{a['name']} ({a.get('team', a.get('role', ''))})" for a in _current_avatar_list]
            chosen_idx = st.selectbox(
                "Avatar",
                options=range(len(_current_avatar_list)),
                format_func=lambda i: avatar_labels[i],
                index=min(st.session_state.avatar_index, len(_current_avatar_list) - 1),
            )
            if chosen_idx != st.session_state.avatar_index:
                st.session_state.avatar_index = chosen_idx
                st.rerun()

    with st.container(border=True):
        st.markdown("**⏱️ Durate**")
        st.session_state.settings["work_minutes"] = st.number_input(
            "Minuti di studio", 1, 90, st.session_state.settings["work_minutes"]
        )
        st.session_state.settings["short_break_minutes"] = st.number_input(
            "Minuti pausa breve", 1, 30, st.session_state.settings["short_break_minutes"]
        )
        st.session_state.settings["long_break_minutes"] = st.number_input(
            "Minuti pausa lunga (milestone)", 1, 60, st.session_state.settings["long_break_minutes"]
        )

    with st.container(border=True):
        st.markdown("**📊 Statistiche**")
        all_stats = st.session_state.persist_stats
        c1, c2 = st.columns(2)
        c1.metric("Streak giorni", all_stats.get("streak_giorni", 0))
        quiz_stats = all_stats.get("quiz", {"corrette": 0, "totali": 0})
        c2.metric("Quiz corretti", f"{quiz_stats['corrette']}/{quiz_stats['totali']}")

    with st.container(border=True):
        st.markdown("**🏆 Dettaglio per tema**")
        for tkey, tdata in THEMES.items():
            if tdata.get("has_teams"):
                for team_key, team_data in TEAMS.items():
                    key = f"{tkey}_{team_key}"
                    tstats = all_stats["themes"].get(key, {"pomodori_totali": 0, "milestone_completate": 0})
                    if tstats["pomodori_totali"] == 0:
                        continue
                    st.caption(
                        f"{team_data['label']}: {tstats['pomodori_totali']} pomodori · "
                        f"{tstats['milestone_completate']} {tdata['milestone_label'].lower()} completate"
                    )
            else:
                tstats = all_stats["themes"].get(tkey, {"pomodori_totali": 0, "milestone_completate": 0})
                st.caption(
                    f"{tdata['label']}: {tstats['pomodori_totali']} pomodori · "
                    f"{tstats['milestone_completate']} {tdata['milestone_label'].lower()} completate"
                )

        history = stats_mod.recent_daily_history(all_stats, days=14)
        if any(v for _, v in history):
            st.caption("Pomodori — ultimi 14 giorni")
            st.bar_chart({d[-2:]: v for d, v in history})

# ---------------------------------------------------------------------------
# Tabs principali
# ---------------------------------------------------------------------------
tab_timer, tab_album = st.tabs(["⏱️ Timer", "📔 Album curiosità"])

# ---------------------------------------------------------------------------
# Logica timer (condivisa)
# ---------------------------------------------------------------------------
PHASE_LABELS = {
    "idle": "Pronto",
    "work": theme["session_label"],
    "short_break": theme["break_label"],
    "long_break": theme["long_break_label"],
}


def start_phase(phase, minutes):
    st.session_state.phase = phase
    st.session_state.phase_duration = minutes * 60
    st.session_state.phase_end = time.time() + minutes * 60


def handle_phase_end():
    finished_phase = st.session_state.phase

    if finished_phase == "work":
        st.session_state.cycle_count += 1
        st.session_state.persist_stats = stats_mod.register_pomodoro(
            st.session_state.persist_stats, stats_key
        )

        if st.session_state.cycle_count >= theme["milestone_sessions"]:
            st.session_state.persist_stats = stats_mod.register_milestone(
                st.session_state.persist_stats, stats_key
            )
            st.session_state.pending_sound = "milestone"
            st.session_state.show_recap = True
            st.session_state.show_confetti = True
            st.session_state.cycle_count = 0
            start_phase("long_break", st.session_state.settings["long_break_minutes"])
        else:
            st.session_state.pending_sound = theme["sound"]
            st.session_state.pending_fact = random.choice(theme["facts"])
            st.session_state.quiz_question = random.choice(QUIZ[st.session_state.theme_key])
            st.session_state.quiz_answered = False
            st.session_state.quiz_selected = None
            start_phase("short_break", st.session_state.settings["short_break_minutes"])
    else:
        st.session_state.phase = "idle"
        st.session_state.phase_end = None
        st.session_state.quiz_question = None


@st.fragment(run_every=1)
def _render_timer_tab():
    if st.session_state.phase != "idle" and st.session_state.phase_end:
        remaining = st.session_state.phase_end - time.time()
        if remaining <= 0:
            handle_phase_end()
            st.rerun()
    else:
        remaining = 0

    # -- Suono pendente --------------------------------------------------
    if st.session_state.pending_sound:
        sound_key = st.session_state.pending_sound
        audio_bytes = milestone_sound() if sound_key == "milestone" else get_break_sound(sound_key)
        st.audio(audio_bytes, format="audio/wav", autoplay=True)
        st.session_state.pending_sound = None

    # -- Confetti alla milestone ------------------------------------------
    if st.session_state.show_confetti:
        components.html(
            f"""
            <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.9.3/dist/confetti.browser.min.js"></script>
            <script>
            (function() {{
                var colors = ['{theme['primary']}', '{theme['accent']}'];
                confetti({{particleCount: 140, spread: 90, origin: {{y: 0.5}}, colors: colors}});
                setTimeout(function() {{
                    confetti({{particleCount: 80, spread: 120, origin: {{y: 0.3}}, colors: colors}});
                }}, 300);
            }})();
            </script>
            """,
            height=0,
        )
        st.session_state.show_confetti = False

    # -- Header ------------------------------------------------------------
    st.markdown(f"<div class='theme-title'>{theme['label']}</div>", unsafe_allow_html=True)
    st.markdown(
        f"<div class='theme-sub'>Ciclo verso: {theme['milestone_label']} "
        f"({st.session_state.cycle_count}/{theme['milestone_sessions']} pomodori)</div>",
        unsafe_allow_html=True,
    )

    if active_avatar:
        badge_primary = active_avatar.get("color", theme["primary"])
        st.markdown(
            render_avatar_badge(
                name=active_avatar["name"],
                subtitle=active_avatar.get("team", active_avatar.get("role", "")),
                number=active_avatar.get("number"),
                primary=badge_primary,
                secondary=theme["secondary"],
                accent=theme["accent"],
                icon=theme["label"].split(" ")[0],
            ),
            unsafe_allow_html=True,
        )

    # -- Anello timer --------------------------------------------------------
    mins, secs = divmod(max(0, int(remaining)), 60)
    phase_progress = 0.0
    if st.session_state.phase != "idle" and st.session_state.phase_duration > 0:
        phase_progress = 1 - (remaining / st.session_state.phase_duration)
        phase_progress = min(max(phase_progress, 0), 1)
    pct = phase_progress * 100

    st.markdown(f"<div class='phase-badge'>{PHASE_LABELS[st.session_state.phase]}</div>", unsafe_allow_html=True)
    st.markdown(
        f"""
        <div class="ring-wrap" style="--pct:{pct:.2f};">
          <div class="ring-inner">
            <div class="timer-display">{mins:02d}:{secs:02d}</div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.session_state.phase == "work":
        sub_unit = min(
            theme["units_per_session"],
            int(phase_progress * theme["units_per_session"]) + 1,
        )
        st.caption(
            f"{theme['unit_name']} {sub_unit}/{theme['units_per_session']} — {theme['start_cta']}"
        )
        st.markdown(render_scene(st.session_state.theme_key, theme, phase_progress), unsafe_allow_html=True)

    # -- Quiz + curiosità durante la pausa ------------------------------
    if st.session_state.phase in ("short_break", "long_break") and st.session_state.quiz_question:
        q = st.session_state.quiz_question
        st.markdown("<div class='quiz-box'>", unsafe_allow_html=True)
        st.markdown(f"**🎯 Quiz lampo:** {q['q']}")
        if not st.session_state.quiz_answered:
            cols = st.columns(len(q["options"]))
            for i, opt in enumerate(q["options"]):
                if cols[i].button(opt, key=f"quiz_opt_{i}_{q['q'][:10]}"):
                    st.session_state.quiz_selected = i
                    st.session_state.quiz_answered = True
                    correct = i == q["correct"]
                    st.session_state.persist_stats = stats_mod.register_quiz_answer(
                        st.session_state.persist_stats, correct
                    )
                    st.rerun()
        else:
            if st.session_state.quiz_selected == q["correct"]:
                st.success("Risposta corretta! 🎉")
            else:
                st.error(f"Non proprio — la risposta giusta era: {q['options'][q['correct']]}")
        st.markdown("</div>", unsafe_allow_html=True)

    if st.session_state.phase in ("short_break", "long_break") and st.session_state.pending_fact:
        st.markdown(
            f"<div class='fact-box'>💡 {st.session_state.pending_fact}</div>",
            unsafe_allow_html=True,
        )
        st.session_state.persist_stats = stats_mod.unlock_fact(
            st.session_state.persist_stats, st.session_state.pending_fact, theme["label"]
        )

    st.write("")

    # -- Controlli (centrati) -------------------------------------------
    pad_l, col1, col2, col3, pad_r = st.columns([2, 1, 1, 1, 2])
    with col1:
        if st.session_state.phase == "idle":
            if st.button("▶️ Avvia studio", type="primary"):
                start_phase("work", st.session_state.settings["work_minutes"])
                st.rerun()
        else:
            if st.button("⏸️ Pausa/Stop"):
                st.session_state.phase = "idle"
                st.session_state.phase_end = None
                st.rerun()
    with col2:
        if st.button("🔁 Reset ciclo"):
            st.session_state.phase = "idle"
            st.session_state.phase_end = None
            st.session_state.cycle_count = 0
            st.rerun()
    with col3:
        if st.session_state.phase in ("short_break", "long_break"):
            if st.button("⏭️ Salta pausa"):
                handle_phase_end()
                st.rerun()

    # -- Recap card alla milestone --------------------------------------
    if st.session_state.show_recap:
        avatar_note = f" — insieme a {active_avatar['name']}!" if active_avatar else ""
        st.success(theme["milestone_message"] + avatar_note)
        theme_stats = st.session_state.persist_stats["themes"].get(
            stats_key, {"pomodori_totali": 0, "milestone_completate": 0}
        )
        card_buf = generate_recap_card(
            theme,
            pomodori_completati=theme_stats["pomodori_totali"],
            minuti_totali=theme_stats["pomodori_totali"] * st.session_state.settings["work_minutes"],
            milestone_count=theme_stats["milestone_completate"],
        )
        st.image(card_buf, use_container_width=True)
        st.download_button(
            "📥 Scarica la card",
            data=card_buf.getvalue(),
            file_name=f"recap_{stats_key}.png",
            mime="image/png",
        )
        if st.button("Ok, continua"):
            st.session_state.show_recap = False
            st.rerun()


with tab_timer:
    _render_timer_tab()

# ---------------------------------------------------------------------------
# Tab Album: curiosità sbloccate finora
# ---------------------------------------------------------------------------
with tab_album:
    album = st.session_state.persist_stats.get("album", [])
    if not album:
        st.info("Completa qualche pomodoro per sbloccare le prime curiosità: appariranno qui come figurine da collezione! 🃏")
    else:
        st.caption(f"{len(album)} curiosità sbloccate finora")
        for entry in reversed(album):
            st.markdown(
                f"<div class='album-card'><b>{entry['tema']}</b><br>{entry['testo']}</div>",
                unsafe_allow_html=True,
            )
