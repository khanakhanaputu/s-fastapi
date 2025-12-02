import click


@click.command()
def hello():
    click.echo(
        """
Hello From CLI
               
Menu:
1. Create [Controller, Model, Service] [Name]
               """
    )


if __name__ == "__main__":
    hello()
