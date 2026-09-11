from pathlib import Path
p=Path('index.html')
s=p.read_text()
marker='/* About card layout repair */'
if marker not in s:
    css=r'''
/* About card layout repair */
.about-card{display:flex;flex-direction:column;min-height:184px;padding:20px 20px 18px}
.about-card strong{font-size:24px;line-height:1.04;max-width:100%}
.about-card small{line-height:1.45;max-width:95%}
.about-card:nth-child(3),.about-card:nth-child(4){padding-bottom:84px}
.api-console{left:20px;right:20px;bottom:18px;min-height:66px;padding:11px 12px;font-size:9px;line-height:1.6;overflow:hidden}
.api-console span{display:block;color:#9b9490;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.crm-row{left:20px;right:20px;bottom:18px;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:6px}
.crm-pill{min-width:0;height:32px;padding:0 7px;justify-content:center;overflow:hidden;white-space:nowrap;text-overflow:ellipsis}
.crm-pill img{flex:0 0 15px;width:15px;height:15px}
.about-card:nth-child(4) strong{font-size:23px;max-width:90%}
.about-card:nth-child(4) small{max-width:92%}
@media(max-width:1100px){.about{grid-template-columns:1fr 1fr;gap:38px}.about-card{min-height:178px}.about-card strong{font-size:22px}.about-card:nth-child(4) strong{font-size:21px}.crm-pill{font-size:8px;padding:0 5px}.crm-pill img{width:14px;height:14px;flex-basis:14px}}
@media(max-width:850px){.about{grid-template-columns:1fr}.about-live{margin-top:4px}.about-card{min-height:165px}.about-card:nth-child(3),.about-card:nth-child(4){padding-bottom:80px}.about-card:nth-child(4) strong{max-width:none}}
@media(max-width:550px){.about-card{min-height:152px}.about-card:nth-child(3),.about-card:nth-child(4){padding-bottom:78px}.api-console{left:18px;right:18px;bottom:15px}.crm-row{left:18px;right:18px;bottom:15px}.crm-pill{font-size:8px}}
'''
    s=s.replace('</style>',css+'</style>',1)
p.write_text(s)
print('patched about card layout')
