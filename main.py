#!/usr/bin/env python
"""
Application to execute Rundeck job
"""
import click
from app.command import rundeck

app_cli = click.CommandCollection(sources=[rundeck.cli])

if __name__ == "__main__":
    app_cli()
