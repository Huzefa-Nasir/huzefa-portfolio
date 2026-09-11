from pathlib import Path

p=Path('index.html')
s=p.read_text()
old='<div class="mini"><div><strong>100+</strong><span>automations</span></div><div><strong>Advanced</strong><span>Zapier & n8n</span></div><div><strong>Custom</strong><span>APIs & webhooks</span></div><div><strong>Broad</strong><span>CRM experience</span></div></div>'
new='''<div class="about-film-shell reveal-scale"><div class="about-film-top"><span>2024 → 2026</span><b>Automation story · 13 sec</b></div><div class="about-film-stage"><video id="aboutFilm" muted loop playsinline preload="none" poster="about-automation-story-poster.jpg" aria-label="Animated story showing Huzefa's automation work growing from one workflow to more than one hundred"><source data-src="about-automation-story.mp4" type="video/mp4"></video><div class="about-film-badge"><i></i><span>Built as a motion piece — not a stock reel</span></div></div><div class="about-film-foot"><span>From one trigger to 100+ automations.</span><strong>Build · debug · automate</strong></div></div>'''
if old not in s and 'id="aboutFilm"' not in s:
    raise SystemExit('About stats block not found')
s=s.replace(old,new,1)
css='''
/* Premium About motion film */
.about-film-shell{border:1px solid var(--line);border-radius:22px;overflow:hidden;background:#101012;box-shadow:0 24px 70px #0005;align-self:center}.about-film-top,.about-film-foot{display:flex;align-items:center;justify-content:space-between;gap:14px;padding:13px 15px;background:#111013}.about-film-top{border-bottom:1px solid #ffffff0c}.about-film-foot{border-top:1px solid #ffffff0c}.about-film-top span{font:700 9px 'Space Grotesk';letter-spacing:.14em;color:var(--o)}.about-film-top b,.about-film-foot span{font-size:10px;color:#9e9794}.about-film-foot strong{font:700 10px 'Space Grotesk';color:#fff;text-transform:uppercase;letter-spacing:.06em}.about-film-stage{position:relative;aspect-ratio:16/9;background:#09090a;overflow:hidden}.about-film-stage video{display:block;width:100%;height:100%;object-fit:cover;background:#09090a}.about-film-badge{position:absolute;left:14px;bottom:14px;display:flex;align-items:center;gap:8px;padding:8px 10px;border:1px solid #ffffff18;border-radius:999px;background:#09090ae8;backdrop-filter:blur(10px);font-size:9px;color:#d6d1cd}.about-film-badge i{width:7px;height:7px;border-radius:50%;background:var(--g);box-shadow:0 0 11px #b9ff6680}
@media(max-width:850px){.about-film-shell{margin-top:6px}.about-film-stage{aspect-ratio:16/9}}
@media(max-width:550px){.about-film-shell{border-radius:17px}.about-film-top,.about-film-foot{padding:10px 11px;gap:8px;align-items:flex-start}.about-film-foot{flex-direction:column}.about-film-badge{left:9px;bottom:9px;font-size:8px;padding:7px 9px}.about-film-top b{font-size:9px}}
@media(prefers-reduced-motion:reduce){.about-film-badge i{box-shadow:none}}
'''
if '/* Premium About motion film */' not in s:
    s=s.replace('</style>',css+'</style>',1)
marker="const heroArt=document.querySelector('.hero-art');"
js="""const aboutFilm=document.getElementById('aboutFilm');if(aboutFilm){const src=aboutFilm.querySelector('source[data-src]');const reduced=matchMedia('(prefers-reduced-motion: reduce)').matches;const loadAboutFilm=()=>{if(!src||src.src||reduced)return;src.src=src.dataset.src;aboutFilm.load()};if('IntersectionObserver'in window&&!reduced){const filmObserver=new IntersectionObserver(entries=>entries.forEach(e=>{if(e.isIntersecting){loadAboutFilm();aboutFilm.play().catch(()=>{});}else{aboutFilm.pause()}}),{rootMargin:'180px'});filmObserver.observe(aboutFilm)}else if(!reduced){loadAboutFilm()}};"""
if 'const aboutFilm=document.getElementById' not in s:
    if marker not in s: raise SystemExit('JS marker not found')
    s=s.replace(marker,js+marker,1)
p.write_text(s)
print('patched About video section')
