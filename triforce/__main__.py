import click

import triforce
from triforce import decoder, encoder


CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group('triforce', short_help='No-bullshit n-triples encoder/decoder',
             context_settings=CONTEXT_SETTINGS)
@click.version_option(version=triforce.__version__, prog_name='triforce')
def cli():
    pass


@cli.command('decode')
@click.argument('ntriple', required=True)
def run_decoder(ntriple):
    """Decodes an n-triple
    """
    spv = decoder.run(ntriple)
    print(spv)


@cli.command('encode')
@click.argument('subject', required=True)
@click.argument('predicate', required=True)
@click.argument('value', required=True)
def run_encoder(subject, predicate, value):
    """Encodes an n-triple
    """
    nt = encoder.run(subject, predicate, value)
    print(nt)


def main():
    cli()


if __name__ == '__main__':
    main()
