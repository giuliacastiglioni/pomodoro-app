"""
Badge avatar stilizzato: cerchio con iniziali, numero di maglia/gara e
colori del tema. Deliberatamente non è un ritratto realistico: è un modo
sicuro (nessun problema di riproduzione dell'immagine di persone reali) ed
elegante per personalizzare l'esperienza con un nome scelto dall'utente.
L'SVG viene appiattito su una riga sola (vedi html_utils) per evitare che
Streamlit lo interpreti come blocco di codice invece che come markup.
"""

from html_utils import flatten_html


def _initials(name):
    parts = [p for p in name.replace("'", " ").split(" ") if p]
    letters = [p[0].upper() for p in parts if p[0].isalpha()]
    return "".join(letters[:2]) if letters else "?"


def render_avatar_badge(name, subtitle, number, primary, secondary, accent, icon="●"):
    initials = _initials(name)
    number_svg = ""
    if number:
        number_svg = f"""
        <text x="150" y="98" text-anchor="middle" font-size="20" font-weight="800"
              fill="{accent}" opacity="0.85">#{number}</text>
        """
    svg = f"""
    <svg viewBox="0 0 300 176" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <linearGradient id="badgeGrad" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stop-color="{primary}"/>
          <stop offset="100%" stop-color="{secondary}"/>
        </linearGradient>
        <pattern id="stripes" width="22" height="22" patternTransform="rotate(35)" patternUnits="userSpaceOnUse">
          <rect width="22" height="22" fill="transparent"/>
          <rect width="7" height="22" fill="{accent}" opacity="0.05"/>
        </pattern>
        <filter id="cardShadow" x="-20%" y="-20%" width="140%" height="140%">
          <feDropShadow dx="0" dy="3" stdDeviation="4" flood-color="{secondary}" flood-opacity="0.45"/>
        </filter>
      </defs>
      <rect x="3" y="3" width="294" height="170" rx="20" fill="url(#badgeGrad)"
            stroke="{accent}" stroke-width="2" filter="url(#cardShadow)"/>
      <rect x="3" y="3" width="294" height="170" rx="20" fill="url(#stripes)"/>
      <circle cx="150" cy="64" r="46" fill="{secondary}66"/>
      <circle cx="150" cy="64" r="42" fill="{secondary}" stroke="{accent}" stroke-width="3"/>
      <text x="150" y="78" text-anchor="middle" font-size="34" font-weight="800"
            fill="{accent}" font-family="Arial, sans-serif">{initials}</text>
      {number_svg}
      <circle cx="258" cy="26" r="18" fill="{secondary}" stroke="{accent}" stroke-width="1.5" opacity="0.9"/>
      <text x="258" y="33" text-anchor="middle" font-size="17" font-family="Arial, sans-serif">{icon}</text>
      <text x="150" y="134" text-anchor="middle" font-size="19" font-weight="700"
            fill="{accent}" font-family="Arial, sans-serif">{name}</text>
      <text x="150" y="156" text-anchor="middle" font-size="13"
            fill="{accent}" opacity="0.8" font-family="Arial, sans-serif">{subtitle}</text>
    </svg>
    """
    return flatten_html(svg)
