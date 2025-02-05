from itertools import chain
from fasthtml.common import *
from functools import partial
from monsterui.all import *
from fasthtml.components import Uk_theme_switcher
_A = partial(A, target='_blank')
def Markdown(s, **kw): return Div(render_md(s, class_map_mods={'ul':'uk-list uk-list-bullet space-y-2 mb-6 ml-6 text-lg'}), **kw)

ghurl = 'https://github.com/AnswerDotAI/fasthtml'
fhurl = 'https://fastht.ml'
docs = 'https://docs.fastht.ml'

def BstPage(selidx, title, h2s, *c):
    navitems = [('About', '/'), ('Vision', '/vision'), ('Foundations', '/foundation'),
                ('Technology', '/tech'), ('Components', '/components'), ('Limits', '#', {'disabled':True})]
    logo = 'assets/logo.svg'
    _NavBarP = partial(P, cls=TextT.lg)
    return (
        Title(title),
        Container(
            # NavBar
            NavBarContainer(
                NavBarLSide(
                    NavBarNav(
                        Li(A(Img(src=logo), href=fhurl)),
                        *[Li(A(_NavBarP(k), href=v), cls='uk-active' if selidx==i else '') for i, (k,v) in enumerate(navitems[:-1])],
                        Li(A(_NavBarP('Limits', href='#'), disabled=True, uk_tooltip='No limits!')))),
                NavBarRSide(
                    NavBarNav(
                        Li(A(_NavBarP("Theme"))),DropDownNavContainer(Div(Uk_theme_switcher(), cls='p-6 uk-drop-close'), cls='w-96'),
                        Li(_A(_NavBarP('Docs'), href=docs)), 
                        Li(_A(_NavBarP(UkIcon('github')), href=ghurl)))),
                cls='bg-green-400/70 rounded-lg rounded-tl-3xl shadow-md p-2 px-4'),
            # Main Content
            Container(
                Grid(
                    Div(NavContainer(*[Li(A(h2, href=f'#sec{i+1}')) for i,h2 in enumerate(h2s)],
                        sticky=True, uk_scrollspy_nav=True), cls='hidden md:block col-span-1'),
                    Div(H1(title, cls='mb-12'), *c, cls='col-span-12 md:col-span-5'),
                    cols=6)),
            # Footer
            DividerLine(),
            Grid(
                    P("© 2024 onwards AnswerDotAI, Inc", cls=TextPresets.muted_lg),
                    DivCentered(A(Img(src=logo, height=24), href=fhurl)),
                    DivRAligned(A("Home"), 
                                _A("Docs",href='https://docs.fastht.ml/'), 
                                _A("Company", href='https://www.answer.ai/'), cls=TextPresets.muted_lg+'space-x-4'),
                ),
                cls='py-8 mb-4' + ContainerT.xl))

def Sections(h2s, texts):
    colors = 'yellow', 'pink', 'teal', 'blue'
    div_cls = 'py-2 px-3 mt-4 mb-2 bg-{}-400/70 shadow-md rounded-lg rounded-tl-3xl' #bg-{}-100
    return chain([Div(H2(h2, id=f'sec{i+1}', cls=div_cls.format(colors[i%4])), Div(txt, cls='px-2'))
                  for i,(h2,txt) in enumerate(zip(h2s, texts))])
