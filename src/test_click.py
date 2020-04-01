#!/usr/bin/python
#-*-coding:UTF-8-*-
import click


@click.command()
@click.option('--count', default=1, help='Number of greeting.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')

def hello(count, name):
    """ Simple program that greets Name for a total of COUNT times."""
    for x in range(count):
        click.echo('Hello %s !' % name)

if __name__ == '__main__':
    hello()