from triforce.things import IRI, Literal


def run(subject, predicate, value):
    """Encodes a subject, predicate, value as an n-triple string.

    Encoding is done per the EBNF grammar and specification outlined on
    https://www.w3.org/TR/n-triples

    Args:
        subject (str): The subject as a string absolute IRI
        predicate (str): The predicate as a string absolute IRI
        value (object): The object literal

    Returns:
        str: The n-triple encoded as a string
    """
    if not isinstance(subject, IRI):
        subject = IRI(subject)
    if not isinstance(predicate, IRI):
        predicate = IRI(predicate)
    if not (isinstance(value, Literal) or isinstance(value, IRI)):
        value = Literal(value)

    return '%s %s %s .' % (subject, predicate, value)
