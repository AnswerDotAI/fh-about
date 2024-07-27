from app import *

def page():
    h2s = 'Python', 'HTMX', 'Uvicorn', 'Starlette', 'SQLite'
    txts = [Markdown(s1), Markdown(s2), Markdown(s3), Markdown(s4), Markdown(s5)]
    secs = Sections(h2s, txts)
    return BstPage(3, "FastHTML's tech stack", *secs)

s1 = """
"""

s2 = """
Nowadays most web applications are built using backend systems that return a combination of JSON and HTML data over HTTP. Javascript, normally using frameworks such as React, Angular, or Vue, is used to combine the JSON and HTML together for display in the browser. This is an *"API based"* approach to web development.

An alternative "hypermedia-based" approach, used by systems such as HTMX, simplifies things greatly by just returning HTML. FastHTML is designed to create hypermedia applications. Nearly all of the complexity of client-server programming vanishes when using this approach. When going to a page directly, the server will respond with a standard HTML web page:

```
<html>
  <head><title>FastHTML Page</title></head>
  <body>
    <p id="greet" hx-get="/change">Hello World!</p>
  </body>
</html>
```

This can be generated using this FastHTML code:

```python
@rt('/')
def get(): return Div(P('Hello World!'), hx_get="/change")
```

When clicking on this link, the server will respond with an "*HTML partial*"---that is, just a snippet of HTML which will be inserted into the existing page:

```
<p>Nice to be here!</p>
```

In this case, the returned element will replace the original `P` element (since that's the default behavior of HTMX). Our code to create this `/change` handler is:

```python
@rt('/change')
def get(): return P('Nice to be here!')
```

As we discussed in the [HTMX foundations](http://localhost:5001/foundation#sec2) section, HTMX removes four critical constraints of HTML. It allows any event on any DOM element to call any HTTP method on any path and place the response anywhere in the DOM.
"""

s3 = """"""

s4 = """"""

s5 = """"""

