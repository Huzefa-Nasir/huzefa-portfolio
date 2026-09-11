from pathlib import Path
p=Path('index.html')
s=p.read_text()
needle='/* Packet polish: moving data should be the only active indicator */'
if needle not in s:
    css="""\n/* Packet polish: moving data should be the only active indicator */\n.arch-preview .start-beacon{animation:none!important;opacity:.28;filter:none}\n.arch-preview .route-packet{opacity:1}\n"""
    s=s.replace('</style>',css+'</style>',1)
p.write_text(s)
print('packet beacon polish applied')
