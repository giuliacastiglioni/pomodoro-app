"""
Genera una card di riepilogo (PNG) a fine milestone (es. GP completato,
partita finita), in stile coerente col tema attivo.
"""
from PIL import Image, ImageDraw, ImageFont
import io


def _font(size, bold=False):
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold
        else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]
    for path in candidates:
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            continue
    return ImageFont.load_default()


def _hex_to_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def generate_recap_card(theme, pomodori_completati, minuti_totali, milestone_count):
    W, H = 1000, 600
    primary = _hex_to_rgb(theme["primary"])
    secondary = _hex_to_rgb(theme["secondary"])
    accent = _hex_to_rgb(theme["accent"])

    img = Image.new("RGB", (W, H), secondary)
    draw = ImageDraw.Draw(img)

    # Fascia diagonale decorativa in stile "bandiera a scacchi / campo"
    for i in range(-H, W, 60):
        draw.polygon(
            [(i, H), (i + 30, H), (i + 30 + H, 0), (i + H, 0)],
            fill=primary if (i // 60) % 2 == 0 else secondary,
        )
    # overlay semi-trasparente per leggibilità
    overlay = Image.new("RGBA", (W, H), secondary + (210,))
    img = Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB")
    draw = ImageDraw.Draw(img)

    title_font = _font(46, bold=True)
    subtitle_font = _font(28, bold=True)
    body_font = _font(24)

    draw.text((50, 50), theme["label"], font=title_font, fill=accent)
    draw.text((50, 120), theme["milestone_message"], font=subtitle_font, fill=primary)

    stats_lines = [
        f"Pomodori completati: {pomodori_completati}",
        f"Minuti di focus: {minuti_totali}",
        f"{theme['milestone_label']} completate: {milestone_count}",
    ]
    y = 230
    for line in stats_lines:
        draw.text((50, y), line, font=body_font, fill=accent)
        y += 45

    draw.rectangle([(50, y + 20), (W - 50, y + 24)], fill=primary)
    draw.text(
        (50, y + 50),
        "Generato con il tuo Pomodoro Tematico",
        font=_font(18),
        fill=accent,
    )

    buf = io.BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)
    return buf
