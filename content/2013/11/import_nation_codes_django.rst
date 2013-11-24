Import (ISO 3166-1) countries names and codes in a Django model
###############################################################

:date: 2013-11-13 20:50
:tags: django, python
:category: django
:slug: import-iso3166-country-names-django
:author: Alessandro De Noia


You may need to import all the countries and relative code defined in the standard
`ISO 3166-1 <http://en.wikipedia.org/wiki/ISO_3166-1>`_ into a Django model.
The function uses `requests <http://www.python-requests.org/>`_ and this
`country list <http://www.iso.org/iso/home/standards/country_codes/country_names_and_code_elements_txt.htm>`_ to populate the model.

**Django model**

.. code-block:: python

    from django.db import models

    class CountryCode(models.Model):
        name = models.CharField(max_length=100)
        code = models.CharField(max_length=2, unique=True)

        def __unicode__(self):
        return u'%s - %s' % (self.name, self.code)


**Function**

.. code-block:: python

    def populate_country_code(model):
        """
        :param model: Model holding the country code data, it must have at least two fields: name and code
        :type model: Django model
        :returns: boolean - state of import
        """
        try:
            r = requests.get('http://www.iso.org/iso/home/standards/country_codes/country_names_and_code_elements_txt.htm')
        except requests.RequestException:
            return False
        countries = r.text.split('\r\n')
        for country in countries[1:-2]:
            country = country.split(';')
            try:
                c = model(name=country[0].capitalize(), code=country[1])
                c.save()
            except model.DoesNotExist:
                return False
        return True