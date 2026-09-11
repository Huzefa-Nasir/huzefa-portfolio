from pathlib import Path
p=Path('index.html')
s=p.read_text()
marker='/* About card overflow final fix */'
if marker not in s:
    css='''\n/* About card overflow final fix */\n.about-card:nth-child(3),.about-card:nth-child(4){padding-bottom:18px!important;min-height:184px}\n.about-card:nth-child(3) .api-console,.about-card:nth-child(4) .crm-row{position:static!important;left:auto!important;right:auto!important;bottom:auto!important;width:100%!important;margin-top:auto!important}\n.about-card:nth-child(3) .api-console{min-height:0!important;padding:11px 12px!important;overflow:hidden}\n.about-card:nth-child(3) small,.about-card:nth-child(4) small{margin-bottom:14px}\n.about-card:nth-child(4) .crm-row{display:grid!important;grid-template-columns:repeat(3,minmax(0,1fr));gap:6px}\n.about-card:nth-child(4) .crm-pill{width:100%;min-width:0;justify-content:center}\n@media(max-width:850px){\n  .about-card:nth-child(3),.about-card:nth-child(4){min-height:170px;padding-bottom:18px!important}\n}\n@media(max-width:550px){\n  .about-card:nth-child(3),.about-card:nth-child(4){min-height:auto!important;padding-bottom:18px!important}\n  .about-card:nth-child(3) .api-console,.about-card:nth-child(4) .crm-row{margin-top:14px!important}\n  .about-card:nth-child(3) small,.about-card:nth-child(4) small{margin-bottom:0}\n}\n'''
    s=s.replace('</style>',css+'</style>',1)
p.write_text(s)
print('About card overflow fixed')
