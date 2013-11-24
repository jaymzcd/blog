Django proxy view for cross domain AJAX GET and POST requests
#############################################################
:date: 2013-07-05 13:42
:author: sdonk
:category: Django, Python
:slug: django-proxy-view-for-cross-domain-ajax-get-and-post-requests

A proxy can be useful, for example, if you need to execute cross domain
AJAX requests.
Using the Django `request object`_ is quite easy to intercept the
parameters of the request and write a few line to act as a proxy.
In the following example I'm using the `HTTP library requests`_ instead
of the most famous `Httplib2`_, because I like the syntax and its
simplicity.

To install requests you can either use `PIP`_:

.. code-block:: bash

    $: sudo pip install requests

or easy\_install:

.. code-block:: bash

    $: sudo easy_install requests

Add the following code the views.py file in one of your Django app,
let's say core:

.. code-block:: python

    from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed
    import requests

    def proxy(request):
        """
        Proxy to use cross domain Ajax GET and POST requests
        request: Django request object
        """
        if request.method == 'GET':
            request = request.GET
            r = requests.get
        elif request.method == 'POST':
            request = request.POST
            r = requests.post
        else:
            return HttpResponseNotAllowed("Permitted methods are POST and GET")
        params = request.dict()
        try:
            url = params.pop('url')
        except KeyError:
            return HttpResponseBadRequest("URL must be defined")
        response = r(url, params=params)
        return HttpResponse(response.text, status=int(response.status_code), mimetype=response.headers['content-type'])

Just add the proxy view to your project's urls.py (remember to change
the app name if it's different!):

.. code-block:: python

    from django.conf.urls import patterns, url

    urlpatterns = patterns('',
        url(r'^proxy/$', 'core.views.proxy', name='proxy'),
    )

All the POST and GET requests made to http://yourdomain/proxy/ will be
handled by the proxy.

.. _request object: https://docs.djangoproject.com/en/1.5/ref/request-response/#httprequest-objects
.. _HTTP library requests: http://docs.python-requests.org/en/latest/
.. _Httplib2: http://code.google.com/p/httplib2/
.. _PIP: http://www.pip-installer.org/en/latest/
