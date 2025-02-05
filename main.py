import vision, overview, foundations, tech, components
from fasthtml.common import *
from monsterui.all import *

hdrs = (
    *Theme.blue.headers(highlightjs=True),
    Script(src="https://cdn.jsdelivr.net/gh/highlightjs/cdn-release@11.9.0/build/languages/html.min.js"),
    *Socials(title='About FastHTML', description='Learn the foundations of FastHTML', site_name='about.fastht.ml',
             twitter_site='@answerdotai', image=f'/assets/og-sq.png', url=''),
)

app,rt = fast_app(pico=False, hdrs=hdrs, live=False)

app.get('/')(overview.page)
app.get('/components')(components.page)
app.get('/foundation')(foundations.page)
app.get('/tech')(tech.page)
app.get('/vision')(vision.page)

serve()
