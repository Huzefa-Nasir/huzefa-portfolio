from pathlib import Path
p=Path('index.html')
s=p.read_text()
marker='/* Mobile hero readability refinement */'
if marker not in s:
    css='''\n/* Mobile hero readability refinement */\n@media(max-width:550px){\n  .hero h1{font-size:clamp(48px,13.4vw,60px);line-height:1.07;letter-spacing:-.047em;margin:20px 0 27px;max-width:100%}\n  .hero h1 em{letter-spacing:-.035em}\n}\n@media(max-width:380px){\n  .hero h1{font-size:clamp(45px,13vw,52px);line-height:1.08;letter-spacing:-.04em}\n}\n'''
    s=s.replace('</style>',css+'</style>',1)
p.write_text(s)
print('mobile hero typography refined')
