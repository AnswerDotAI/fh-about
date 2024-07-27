from fh_bootstrap import *
from itertools import chain
from markdown import markdown

md_exts='codehilite', 'smarty', 'extra', 'sane_lists'
def Markdown(s, exts=md_exts, **kw): return Div(NotStr(markdown(s, extensions=exts)), **kw)

ghurl = 'https://github.com/AnswerDotAI/fasthtml'
fhurl = 'https://fastht.ml'

def BstPage(selidx, title, *c):
    navitems = [('About', '/'), ('Vision', '/vision'), ('Foundations', '/foundation'),
                ('Technology', '/tech'), ('Components', '/components'), ('Limits', '#', {'disabled':True})]
    ra_items = (A('Docs', href='https://docs.fastht.ml', cls="nav-link"),
                Icon('fab fa-github', dark=False, sz='lg', href=ghurl, cls='ms-2 px-2'))
    ftlinks = [A(k, href=v, cls='nav-link px-2 text-muted')
        for k,v in dict(Home='https://www.fastht.ml', Docs='https://docs.fastht.ml', Company='https://www.answer.ai').items()]
    return (
        Title(title),
        Script('initTOC()'),
        Container(
            Navbar('nav', selidx, items=navitems, ra_items=ra_items, cls='navbar-light bg-secondary rounded-lg',
                image='assets/logo.svg', hdr_href=fhurl, placement=PlacementT.Default, expand=SizeT.Md, toggle_left=False),
            Toc(Container(H1(title, cls='pb-2 pt-1'), *c, cls='mt-3')),
            BstFooter('© 2024 onwards AnswerDotAI, Inc', File('assets/logo.svg'), img_href='http://www.fastht.ml', cs=ftlinks),
        typ=ContainerT.Xl, cls='mt-3', data_bs_spy='scroll', data_bs_target='#toc')
    )

def Sections(h2s, texts):
    colors = 'yellow', 'pink', 'teal', 'blue'
    div_cls = 'py-2 px-3 mt-4 bg-light-{} rounded-tl-lg'
    return chain([Div(H2(h2, id=f'sec{i+1}', cls=div_cls.format(colors[i%4])), Div(txt, cls='px-2'))
                  for i,(h2,txt) in enumerate(zip(h2s, texts))])
