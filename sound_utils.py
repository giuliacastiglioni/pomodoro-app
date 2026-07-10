"""
Genera effetti sonori sintetizzati (nessun asset esterno necessario).
Ogni suono è un piccolo file WAV creato al volo con onde sinusoidali.
"""
import io
import wave
import numpy as np

SAMPLE_RATE = 44100


def _tone(freq, duration, volume=0.5, fade=0.01):
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), False)
    wave_data = np.sin(freq * t * 2 * np.pi)
    # fade in/out per evitare click
    fade_samples = int(SAMPLE_RATE * fade)
    if fade_samples > 0 and fade_samples * 2 < len(wave_data):
        envelope = np.ones_like(wave_data)
        envelope[:fade_samples] = np.linspace(0, 1, fade_samples)
        envelope[-fade_samples:] = np.linspace(1, 0, fade_samples)
        wave_data *= envelope
    return wave_data * volume


def _to_wav_bytes(signal):
    signal = np.clip(signal, -1, 1)
    audio = (signal * 32767).astype(np.int16)
    buf = io.BytesIO()
    with wave.open(buf, "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(SAMPLE_RATE)
        wf.writeframes(audio.tobytes())
    return buf.getvalue()


def pit_stop_sound():
    """Sequenza rapida acuta stile 'via libera' box F1."""
    beeps = [_tone(880, 0.08), _tone(0, 0.03), _tone(1046, 0.08),
             _tone(0, 0.03), _tone(1318, 0.15)]
    return _to_wav_bytes(np.concatenate(beeps))


def whistle_sound():
    """Fischio d'arbitro: tono acuto sostenuto con leggero tremolo."""
    duration = 0.6
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), False)
    freq_mod = 3000 + 100 * np.sin(2 * np.pi * 12 * t)
    signal = np.sin(2 * np.pi * freq_mod * t / SAMPLE_RATE * SAMPLE_RATE) * 0.4
    # ricostruzione più semplice e stabile: tono fisso acuto con tremolo d'ampiezza
    base = np.sin(2 * np.pi * 3100 * t)
    tremolo = 0.85 + 0.15 * np.sin(2 * np.pi * 18 * t)
    signal = base * tremolo * 0.4
    fade_samples = int(SAMPLE_RATE * 0.02)
    signal[:fade_samples] *= np.linspace(0, 1, fade_samples)
    signal[-fade_samples:] *= np.linspace(1, 0, fade_samples)
    return _to_wav_bytes(signal)


def buzzer_sound():
    """Buzzer da fine quarto: tono basso e ronzante."""
    duration = 0.5
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), False)
    signal = np.sign(np.sin(2 * np.pi * 220 * t)) * 0.35  # onda quadra = suono "buzzer"
    fade_samples = int(SAMPLE_RATE * 0.02)
    signal[:fade_samples] *= np.linspace(0, 1, fade_samples)
    signal[-fade_samples:] *= np.linspace(1, 0, fade_samples)
    return _to_wav_bytes(signal)


def bounce_sound():
    """Pallina da tennis che rimbalza: due colpi secchi ravvicinati e attutiti."""
    thud1 = _tone(180, 0.05, volume=0.5, fade=0.005)
    gap1 = _tone(0, 0.08)
    thud2 = _tone(160, 0.045, volume=0.4, fade=0.005)
    gap2 = _tone(0, 0.05)
    thud3 = _tone(150, 0.035, volume=0.3, fade=0.005)
    return _to_wav_bytes(np.concatenate([thud1, gap1, thud2, gap2, thud3]))


def milestone_sound():
    """Piccolo jingle di completamento, usato per tutti i temi al traguardo finale."""
    notes = [523, 659, 784, 1046]
    beeps = []
    for f in notes:
        beeps.append(_tone(f, 0.12, volume=0.4))
        beeps.append(_tone(0, 0.02))
    return _to_wav_bytes(np.concatenate(beeps))


SOUND_MAP = {
    "pit_stop": pit_stop_sound,
    "whistle": whistle_sound,
    "buzzer": buzzer_sound,
    "bounce": bounce_sound,
}


def get_break_sound(sound_key):
    return SOUND_MAP.get(sound_key, pit_stop_sound)()
