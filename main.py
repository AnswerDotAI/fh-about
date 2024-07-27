from fh_bootstrap import *
import vision, overview, foundations, tech, components

hdrs = (Link(href='assets/hl-styles.css', rel='stylesheet'),)

app,rt = fast_app(pico=False, hdrs=bst_hdrs+hdrs, live=True)

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

run_uv()
