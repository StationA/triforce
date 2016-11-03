try:
    from urlparse import urlparse
except ImportError:
    # Python 3 forward compatibility
    from urllib.parse import urlparse


BASE_XMLSCHEMA_URI = 'http://www.w3.org/2001/XMLSchema'


def _ensure_valid_iri(iri):
    parsed = urlparse(iri)
    assert parsed.netloc, 'IRIs must be absolute'
    return parsed.geturl()


class IRI(object):
    def __init__(self, absolute_iri):
        self.absolute_iri = _ensure_valid_iri(absolute_iri)

    def __repr__(self):
        return '<' + self.absolute_iri + '>'


class Literal(object):
    def __init__(self, value, langtag=None):
        self.value = value
        self.langtag = langtag

    def __repr__(self):
        encoded = '"%s"' % self.value
        if isinstance(self.value, str) and self.langtag is not None:
            encoded += '@%s' % self.langtag
        elif isinstance(self.value, int):
            encoded += '^^%s' % IRI(BASE_XMLSCHEMA_URI + '#integer')
        elif isinstance(self.value, float):
            encoded += '^^%s' % IRI(BASE_XMLSCHEMA_URI + '#double')
        return encoded
