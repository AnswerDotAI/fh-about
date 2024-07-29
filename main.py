from fh_bootstrap import *
import vision, overview, foundations, tech, components

hdrs = (
    Link(href='/assets/hl-styles.css', rel='stylesheet'),
    Link(href='/assets/styles.css', rel='stylesheet'),
    *Socials(title='About FastHTML', description='Learn the foundations of FastHTML', site_name='about.fastht.ml',
             twitter_site='@answerdotai', image=f'/assets/og-sq.png', url='')
)

app,rt = fast_app(pico=False, hdrs=bst_hdrs+hdrs, live=False)

@rt('/')
def get(): return overview.page()

@rt('/components')
def get(): return components.page()

@rt('/foundation')
def get(): return foundations.page()

@rt('/tech')
def get(): return tech.page()

@rt('/vision')
def get(): return vision.page()

serve()
