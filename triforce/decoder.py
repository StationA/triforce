from parsimonious import Grammar


GRAMMAR = Grammar('''
    triple = subject WS+ predicate WS+ value WS* "." WS*
    subject = IRIREF / BLANK_NODE_LABEL
    predicate = IRIREF / BLANK_NODE_LABEL
    value = IRIREF / BLANK_NODE_LABEL / literal
    literal = STRING_LITERAL_QUOTE (("^^" IRIREF) / LANGTAG)?
    LANGTAG = "@" ~r"[a-zA-Z]+" ("-" ~r"[a-zA-Z0-9]+")*
    IRIREF = "<" (~r"[^\\x00-\\x20\<\>\\"\\{\\}\\|\\^`\\\\]" / UCHAR)* ">"
    STRING_LITERAL_QUOTE = "\\"" (~r"[^\\x22\\x5C\\x0A\\x0D]" / ECHAR / UCHAR)* "\\""
    BLANK_NODE_LABEL = "_:" (PN_CHARS_U / ~r"[0-9]") (PN_CHARS / ".")* PN_CHARS?
    UCHAR = ("\\\\u" HEX HEX HEX HEX) / ("\\\\U" HEX HEX HEX HEX HEX HEX HEX HEX)
    ECHAR = "\\\\" ~r"[tbnrf\\"'\\\\]"
    PN_CHARS_BASE = ~r"[A-Z]" / ~r"[a-z]" / ~r"[\\u00C0-\\u00D6]" /
                    ~r"[\\u00D8-\\u00F6]" / ~r"[\\u00F8-\\u02FF]" /
                    ~r"[\\u0370-\\u037D]" / ~r"[\\u037F-\\u1FFF]" /
                    ~r"[\\u200C-\\u200D]" / ~r"[\\u2070-\\u218F]" /
                    ~r"[\\u2C00-\\u2FEF]" / ~r"[\\u3001-\\uD7FF]" /
                    ~r"[\\uF900-\\uFDCF]" / ~r"[\\uFDF0-\\uFFFD]" /
                    ~r"[\\u10000-\\uEFFFF]"
    PN_CHARS_U = PN_CHARS_BASE / "_" / ":"
    PN_CHARS = PN_CHARS_U / "-" / ~r"[0-9]" / "\\u00B7" /
               ~r"[\\u0300-\\u036F]" / ~r"[\\u203F-\\u2040]"
    HEX = ~r"[0-9]" / ~r"[A-F]" / ~r"[a-f]"
    WS = ~r"\\s"
''')


def run(ntriple):
    return GRAMMAR.parse(ntriple)
