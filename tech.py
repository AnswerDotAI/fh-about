from app import *

def page():
    h2s = 'Python', 'HTMX', 'Uvicorn', 'Starlette', 'SQLite'
    txts = [Markdown(s1), Markdown(s2), Markdown(s3), Markdown(s4), Markdown(s5)]
    secs = Sections(h2s, txts)
    return BstPage(3, "FastHTML's tech stack", *secs)

s1 = """
Many of the largest software systems in the world are built using Python, such as much of the code for YouTube, Instagram, Dropbox, and many others. In 2019, Dropbox announced that python was their "most widely used language both for backend services and the desktop client app", with 4 million lines of code.

If you're already a Python programmer, then you'll know how easy it is to turn your ideas into code using this language. As well as being used for large-scale systems, Python is also popular for the day-to-day work of scientists, engineers, data analysts, and so forth.

One particular challenge for Python programmers has been that to create a modern web application, they have had to also learn JavaScript, along with a framework like React, Angular, or Vue. Even after learning all this, they still have to deal with the complexity of writing, debugging, and maintaining a multi-language system with complex interactions between the two languages and across the client-server boundary.

With FastHTML, you'll often find you never have to write any JavaScript at all. Not only does development and debugging become much easier, but many features suddenly become easier to implement. For instance, when we wanted to add caching to speed up our [home page](https://fastht.ml), we simply added a standard decorator to the function that creates it. No need for special infrastructure, because the implementation is all in one place. ASGI makes this particularly powerful---it can handle caching, sessions, authentication, host-based redirects, sub-routing, and more, all in one place. All of this is directly accessible from FastHTML.
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

As we discussed in the [HTMX foundations](http://localhost:5001/foundation#sec2) section, HTMX removes four critical constraints of HTML. It allows any event on any DOM element to call any HTTP method on any path and place the response anywhere in the DOM. If you haven't written a hypermedia-based application before, then we strongly recommend reading the [Hypermedia Systems book](https://hypermedia.systems/). It explains how to build hypermedia applications using HTMX; the techniques you learn there will be directly applicable to FastHTML.
"""

s3 = """
[Uvicorn](https://www.uvicorn.org/) is, according to its website, "an ASGI web server". What does that even mean? As [we've discussed](/foundations#sec1), ASGI is a Python API that converts HTTP requests and responses into Python function calls. Uvicorn is a web server which a web browser can talk to, and it in turn talks to an ASGI application, returning its results back to the browser.


"""

s4 = """
"""

s5 = """
"""
