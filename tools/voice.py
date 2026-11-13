"""Озвучка Flash Lab: читает voice/lines.json и делает mp3 голосами Piper (русские голоса).
Запускается в GitHub Actions (workflow «Озвучка»). Готовые файлы кладутся в voice/<голос>/<хеш>.mp3,
список — в voice/index.json. Игра скачивает их с сайта (GitHub Pages)."""
import json, os, subprocess, sys, urllib.request, wave
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VOICE = os.path.join(ROOT, 'voice')
HF = 'https://huggingface.co/rhasspy/piper-voices/resolve/main/ru/ru_RU/{n}/medium/ru_RU-{n}-medium.onnx'
MODELS = {'irina': 'irina', 'irina2': 'irina', 'denis': 'denis', 'dmitri': 'dmitri', 'ruslan': 'ruslan'}
PITCH = {'irina2': 1.12}

def model(name):
    os.makedirs('/tmp/piper', exist_ok=True)
    p = f'/tmp/piper/ru_RU-{name}-medium.onnx'
    for ext in ('', '.json'):
        if not os.path.exists(p + ext):
            print('download', name + ext, flush=True)
            urllib.request.urlretrieve(HF.format(n=name) + ext, p + ext)
    return p

def main():
    from piper import PiperVoice
    lines = json.load(open(os.path.join(VOICE, 'lines.json'), encoding='utf-8'))
    loaded, done = {}, {}
    for ln in lines:
        v, t, h = ln['v'], ln['t'], ln['h']
        out = os.path.join(VOICE, v, h + '.mp3')
        done.setdefault(v, [])
        if os.path.exists(out):
            done[v].append(h)
            continue
        base = MODELS.get(v, 'denis')
        if base not in loaded:
            loaded[base] = PiperVoice.load(model(base))
        os.makedirs(os.path.dirname(out), exist_ok=True)
        wav = '/tmp/piper/line.wav'
        with wave.open(wav, 'wb') as wf:
            vo = loaded[base]
            if hasattr(vo, 'synthesize_wav'):
                vo.synthesize_wav(t, wf)
            else:
                vo.synthesize(t, wf)
        af = ['-af', f'asetrate=22050*{PITCH[v]},aresample=22050,atempo={1/PITCH[v]:.3f}'] if v in PITCH else []
        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', wav, *af, '-ac', '1', '-b:a', '48k', out], check=True)
        done[v].append(h)
        print('ok', v, h, t[:50], flush=True)
    json.dump({k: sorted(set(x)) for k, x in done.items()}, open(os.path.join(VOICE, 'index.json'), 'w'), ensure_ascii=False)
    print('всего фраз:', sum(len(x) for x in done.values()))

if __name__ == '__main__':
    sys.exit(main())
