Dynamically create class views from models in Django
####################################################

:date: 2013-12-02 15:00
:tags: django, python
:category: django
:slug: dynamically-create-class-views-from-models-in-django
:author: Alessandro De Noia


Let's say you have a lot of models in your Django apps and you want to create a ListView (or another class based view, in my case I'm returning the model objects as JSON) for each of those.
Let's say you want to limit the models to a specific set as well.


Your settings.py file should contain a tuple of models tuple:

**settings.py**


.. code-block:: python
    ALLOWED_MODELS = (
        # add more models with the syntax ('app_label', 'model_name')
        ('news', 'news'),
        ('news', 'event'),
        ('artist', 'artist'),
    )


Here is where the magic happens, the models are loaded using the Django get_model function and the views classes are created using [type](http://docs.python.org/2/library/functions.html#type)

**views.py**


.. code-block:: python

    from django.views.generic.list import BaseListView
    from django.db.models import get_model
    from django.conf import settings
    from django.core import serializers
    from django.conf.urls import url, patterns
    from django.http import HttpResponse

    class JsonResponseMixin(object):
        """
        Return json
        """
        def render_to_response(self, context):
            queryset = self.model.objects.all()
            data = serializers.serialize('json', queryset)
            return HttpResponse(data, content_type='application/json')

    def create_class_views():
        """
        Dynamically create the views from the models defined in  ALLOWED_MODELS
        :return:
        """
        views = []
        for i in settings.ALLOWED_MODELS:
           model = get_model(i[0], i[1])
           url = r'^%s/$' % i[1]
           class_name = "%s%s" % (i[1].capitalize(), 'View')
           view_class = type (
                                class_name,
                                (JsonResponseMixin, BaseListView),
                                dict(
                                    model = model,
                                    url = url,
                                    view_name = i[0]
                                )
           )
           views.append(view_class)
        return views

    def create_urls():
        """
        Dynamically create the urls for the view created in create_class_views()
        :return:
        """
        urls = []
        for view in create_class_views():
            urls.append(url(view.url, view.as_view(), name=view.view_name))
            urlpatterns = patterns('', *urls)
        return urlpatterns


**urls.py**

.. code-block:: python

    from .views import create_urls

    urlpatterns = create_urls()


Now your views are accessible from 127.0.0.1:800/{modelname}