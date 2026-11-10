import os

# SVG dosyalarının kaydedileceği klasörü oluştur
os.makedirs("cards", exist_ok=True)

# 1. HERO KARTI (En Üstteki Ana Profil Kartı)
hero_svg = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 200" width="100%" height="100%">
    <style>
        .bg { fill: #0d1117; rx: 15px; }
        .name { font: 700 48px system-ui, sans-serif; fill: #ffffff; opacity: 0; animation: fadeUp 1s 0.2s forwards; }
        .title { font: 400 22px system-ui, sans-serif; fill: #8b949e; opacity: 0; animation: fadeUp 1s 0.5s forwards; }
        .highlight { fill: #58a6ff; }
        @keyframes fadeUp {
            0% { opacity: 0; transform: translateY(20px); }
            100% { opacity: 1; transform: translateY(0); }
        }
    </style>
    <rect class="bg" width="100%" height="100%" />
    <text x="50" y="90" class="name">Merhaba, ben <tspan class="highlight">Eren Yaşar</tspan></text>
    <text x="50" y="135" class="title">Software Developer | Sürekli Öğrenen & Üreten</text>
    
    <!-- Animasyonlu dekoratif çizgi -->
    <rect x="50" y="160" width="0" height="3" fill="#58a6ff">
        <animate attributeName="width" from="0" to="100" dur="1s" begin="0.8s" fill="freeze" />
    </rect>
</svg>
"""

# 2. ORTAK KART ŞABLONU (Alt Yana Yana Dizilecek 3 Kart İçin)
def create_tile_svg(title, items, delay, icon_color):
    items_html = ""
    for i, item in enumerate(items):
        item_delay = delay + 0.3 + (i * 0.2)
        items_html += f'''
        <text x="30" y="{80 + (i * 35)}" class="item" style="animation-delay: {item_delay}s;">
            <tspan fill="{icon_color}">▹</tspan> {item}
        </text>
        '''
    
    return f"""
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 250" width="100%" height="100%">
        <style>
            .bg {{ fill: #161b22; rx: 15px; stroke: #30363d; stroke-width: 1; }}
            .title {{ font: 600 24px system-ui, sans-serif; fill: #ffffff; opacity: 0; animation: fadeUp 0.8s {delay}s forwards; }}
            .item {{ font: 400 16px system-ui, sans-serif; fill: #c9d1d9; opacity: 0; animation: fadeUp 0.8s forwards; }}
            @keyframes fadeUp {{
                0% {{ opacity: 0; transform: translateY(15px); }}
                100% {{ opacity: 1; transform: translateY(0); }}
            }}
        </style>
        <rect class="bg" width="100%" height="100%" />
        <text x="30" y="45" class="title">{title}</text>
        {items_html}
    </svg>
    """

# Kart içerikleri (Buraları kendi yeteneklerine/projelerine göre düzenleyebilirsin)
build_svg = create_tile_svg("💻 Yetenekler", ["Python & JavaScript", "React & Node.js", "Veritabanı Yönetimi", "API Geliştirme"], 0.4, "#3fb950")
learn_svg = create_tile_svg("🚀 Şu An Odaklandığım", ["Yapay Zeka Entegrasyonları", "İleri Seviye Algoritmalar", "Açık Kaynak Projeler", "Sistem Mimarisi"], 0.6, "#d2a8ff")
connect_svg = create_tile_svg("📫 İletişim", ["LinkedIn: /eren-yaşar", "GitHub: @erenyasar1", "Projelerime göz at!", ""], 0.8, "#ff7b72")

# Dosyaları diske yaz
with open("cards/hero.svg", "w", encoding="utf-8") as f: f.write(hero_svg)
with open("cards/build.svg", "w", encoding="utf-8") as f: f.write(build_svg)
with open("cards/learn.svg", "w", encoding="utf-8") as f: f.write(learn_svg)
with open("cards/connect.svg", "w", encoding="utf-8") as f: f.write(connect_svg)

print("Tüm animasyonlu SVG kartları başarıyla oluşturuldu!")
