#!/usr/bin/env python3
"""Skill'i ChatGPT, Gemini vb. için tek bir Markdown dosyasında birleştirir.

Kullanım:  python3 scripts/tek-dosya-olustur.py
Çıktılar:  dist/humanizer-tr-tek-dosya.md  (ChatGPT, Gemini vb. için)
           dist/humanizer-tr.zip              (Claude.ai'ye yüklemek için)

Skill dosyalarında bir değişiklik yaptıysanız bu script'i yeniden çalıştırıp
çıktıyı da commit'leyin.
"""
import re
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "humanizer-tr"
OUT = ROOT / "dist" / "humanizer-tr-tek-dosya.md"
REFS = ["ai-oruntuleri.md", "cumle-turleri.md", "baglaclar.md", "noktalama.md", "yazar-profili.md"]

HEADER = """# Humanizer TR: tek dosya sürümü

> Bu dosya, humanizer-tr Claude skill'inin ChatGPT, Gemini ve benzeri
> yapay zeka araçlarında kullanılabilmesi için tek dosyada birleştirilmiş
> hâlidir. Otomatik üretilir, elle düzenlemeyin
> (`scripts/tek-dosya-olustur.py`).
>
> **Yapay zekaya not:** Aşağıda `references/...` diye anılan dosyaların
> hepsi bu belgenin içinde, aynı adı taşıyan "Ek" başlıkları altında yer
> alır. Kullanıcı bir Türkçe metni insanlaştırmanı, doğallaştırmanı ya da
> Türkçeleştirmeni istediğinde bu belgedeki kurallara göre çalış.

"""

def strip_frontmatter(text: str) -> str:
    return re.sub(r"\A---\n.*?\n---\n", "", text, flags=re.S)

def demote(text: str) -> str:
    # Başlıkları bir seviye aşağı al ki ekler ana belgenin altında dursun.
    return re.sub(r"^(#{1,5}) ", lambda m: "#" + m.group(1) + " ", text, flags=re.M)

def main():
    parts = [HEADER, strip_frontmatter((SKILL / "SKILL.md").read_text(encoding="utf-8"))]
    for name in REFS:
        body = (SKILL / "references" / name).read_text(encoding="utf-8")
        parts.append(f"\n\n---\n\n# Ek: references/{name}\n\n" + demote(body))
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text("".join(parts), encoding="utf-8")
    print(f"{OUT.relative_to(ROOT)} yazıldı ({OUT.stat().st_size // 1024} KB)")

    # Claude.ai için zip: içinde yalnızca skill klasörü (testler hariç).
    z = ROOT / "dist" / "humanizer-tr.zip"
    with zipfile.ZipFile(z, "w", zipfile.ZIP_DEFLATED) as zf:
        for f in sorted(SKILL.rglob("*")):
            rel = f.relative_to(SKILL)
            if f.is_file() and rel.parts[0] != "evals" and f.name != ".DS_Store":
                zf.write(f, Path("humanizer-tr") / rel)
    print(f"{z.relative_to(ROOT)} yazıldı ({z.stat().st_size // 1024} KB)")

if __name__ == "__main__":
    main()
