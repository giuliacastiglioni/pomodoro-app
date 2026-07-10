"""
Genera scene SVG semplici e originali (nessuna immagine esterna, quindi
nessun problema di copyright) che si "riempiono" in base al progresso
della sessione di studio in corso. L'output viene appiattito su una riga
sola per evitare che Streamlit interpreti l'indentazione come blocco di
codice invece che come markup SVG (vedi html_utils).
"""
from html_utils import flatten_html


def _track_scene(theme, progress):
    """Pista ovale F1 con auto che avanza lungo il tracciato."""
    primary, secondary, accent = theme["primary"], theme["secondary"], theme["accent"]
    # posizione lungo un percorso ellittico approssimato con angolo
    import math
    angle = progress * 2 * math.pi - math.pi / 2
    cx, cy, rx, ry = 250, 110, 200, 70
    car_x = cx + rx * math.cos(angle)
    car_y = cy + ry * math.sin(angle)
    rotation = math.degrees(angle) + 90

    return f"""
    <svg viewBox="0 0 500 220" xmlns="http://www.w3.org/2000/svg">
      <ellipse cx="{cx}" cy="{cy}" rx="{rx+20}" ry="{ry+20}" fill="none"
               stroke="{accent}22" stroke-width="26"/>
      <ellipse cx="{cx}" cy="{cy}" rx="{rx+20}" ry="{ry+20}" fill="none"
               stroke="{accent}" stroke-width="2" stroke-dasharray="6,6"/>
      <line x1="{cx}" y1="{cy-ry-32}" x2="{cx}" y2="{cy-ry-8}" stroke="{accent}" stroke-width="6"/>
      <text x="{cx}" y="{cy-ry-40}" text-anchor="middle" fill="{accent}" font-size="14"
            font-weight="bold">🏁 START/FINISH</text>
      <g transform="translate({car_x},{car_y}) rotate({rotation})">
        <rect x="-14" y="-7" width="28" height="14" rx="4" fill="{primary}" stroke="{accent}" stroke-width="1.5"/>
        <circle cx="-8" cy="-7" r="3" fill="{secondary}"/>
        <circle cx="8" cy="-7" r="3" fill="{secondary}"/>
        <circle cx="-8" cy="7" r="3" fill="{secondary}"/>
        <circle cx="8" cy="7" r="3" fill="{secondary}"/>
      </g>
    </svg>
    """


def _pitch_scene(theme, progress):
    """Campo da calcio visto dall'alto, con pallone che avanza verso la porta avversaria."""
    primary, secondary, accent = theme["primary"], theme["secondary"], theme["accent"]
    ball_x = 40 + progress * 420

    return f"""
    <svg viewBox="0 0 500 220" xmlns="http://www.w3.org/2000/svg">
      <rect x="10" y="10" width="480" height="200" fill="none" stroke="{accent}" stroke-width="3"/>
      <line x1="250" y1="10" x2="250" y2="210" stroke="{accent}" stroke-width="2"/>
      <circle cx="250" cy="110" r="35" fill="none" stroke="{accent}" stroke-width="2"/>
      <rect x="10" y="60" width="45" height="100" fill="none" stroke="{accent}" stroke-width="2"/>
      <rect x="445" y="60" width="45" height="100" fill="none" stroke="{primary}" stroke-width="2"/>
      <rect x="2" y="85" width="10" height="50" fill="{accent}"/>
      <rect x="488" y="85" width="10" height="50" fill="{primary}"/>
      <circle cx="{ball_x}" cy="110" r="9" fill="white" stroke="{secondary}" stroke-width="1.5"/>
      <path d="M {ball_x-4} 106 l 8 4 l -3 6 h -2 z" fill="{secondary}"/>
    </svg>
    """


def _court_scene(theme, progress):
    """Campo da basket con la palla che si avvicina al canestro."""
    primary, secondary, accent = theme["primary"], theme["secondary"], theme["accent"]
    ball_x = 40 + progress * 400

    return f"""
    <svg viewBox="0 0 500 220" xmlns="http://www.w3.org/2000/svg">
      <rect x="10" y="10" width="480" height="200" fill="none" stroke="{accent}" stroke-width="3"/>
      <circle cx="250" cy="110" r="40" fill="none" stroke="{accent}" stroke-width="2"/>
      <line x1="250" y1="10" x2="250" y2="210" stroke="{accent}" stroke-width="2"/>
      <rect x="460" y="70" width="6" height="80" fill="{accent}"/>
      <rect x="440" y="90" width="20" height="40" fill="none" stroke="{accent}" stroke-width="2"/>
      <circle cx="450" cy="110" r="14" fill="none" stroke="{primary}" stroke-width="3"/>
      <circle cx="{ball_x}" cy="110" r="10" fill="{primary}" stroke="{secondary}" stroke-width="1"/>
      <line x1="{ball_x-10}" y1="110" x2="{ball_x+10}" y2="110" stroke="{secondary}" stroke-width="1"/>
      <line x1="{ball_x}" y1="100" x2="{ball_x}" y2="120" stroke="{secondary}" stroke-width="1"/>
    </svg>
    """


def _tennis_scene(theme, progress):
    """Campo da tennis visto dall'alto, con la pallina che rimbalza tra i due fondocampo."""
    primary, secondary, accent = theme["primary"], theme["secondary"], theme["accent"]
    import math
    # la pallina oscilla avanti e indietro lungo il campo mentre il progresso avanza
    t = progress * 6 * math.pi
    ball_x = 250 + 190 * math.sin(t)
    ball_y = 110 + 8 * math.sin(t * 2)

    return f"""
    <svg viewBox="0 0 500 220" xmlns="http://www.w3.org/2000/svg">
      <rect x="30" y="20" width="440" height="180" fill="none" stroke="{accent}" stroke-width="3"/>
      <rect x="30" y="45" width="440" height="130" fill="none" stroke="{accent}" stroke-width="1.5" opacity="0.7"/>
      <line x1="250" y1="20" x2="250" y2="200" stroke="{accent}" stroke-width="1" stroke-dasharray="4,4" opacity="0.6"/>
      <line x1="30" y1="110" x2="470" y2="110" stroke="{primary}" stroke-width="3"/>
      <line x1="140" y1="45" x2="140" y2="175" stroke="{accent}" stroke-width="1.5" opacity="0.7"/>
      <line x1="360" y1="45" x2="360" y2="175" stroke="{accent}" stroke-width="1.5" opacity="0.7"/>
      <circle cx="{ball_x:.1f}" cy="{ball_y:.1f}" r="8" fill="{primary}" stroke="{secondary}" stroke-width="1.2"/>
    </svg>
    """


_SCENE_MAP = {
    "f1": _track_scene,
    "calcio": _pitch_scene,
    "basket": _court_scene,
    "tennis": _tennis_scene,
}


def render_scene(theme_key, theme, progress):
    builder = _SCENE_MAP.get(theme_key, _track_scene)
    return flatten_html(builder(theme, max(0.0, min(1.0, progress))))
