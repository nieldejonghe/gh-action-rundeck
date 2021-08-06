#!/usr/local/bin/python
"""
Execute Rundeck job and get output
"""
import click
import json
import time
from pyrundeck import Rundeck


@click.group()
def cli():
    pass


@cli.command()
@click.option("--rundeck-url",
              help="Rundeck URL.",
              required=True)
@click.option("--rundeck-token",
              help="Rundeck token.",
              required=True)
@click.option("--api-version",
              help="Rundeck API version.",
              default="31")
@click.option("--verify-ssl",
              help="Verify SSL.",
              default="true")
@click.option("--job-id",
              help="Rundeck job ID.",
              required = True)
@click.option("--options",
              help="Rundeck job options in json format.")
@click.option("--wait",
              help="Wait Rundeck job finish and print output.")
def execute_rundeck_job(rundeck_url, rundeck_token, api_version, verify_ssl, job_id, options=None, wait=None):
    """Exetute Rundeck job and get output."""

    if options:
        options = json.loads(options)

    rundeck = Rundeck(rundeck_url, token=rundeck_token, api_version=api_version, verify=(verify_ssl == 'true'))

    run = rundeck.run_job(job_id, options=options)
    print("Scheduled Rundeck job: %d" % run['id'])

    if wait is None:
        wait = 'true'

    if wait == 'true':
        while rundeck.execution_state(run['id'])['executionState'] == 'RUNNING':
            print("Rundeck job in progress: %d ..." % run['id'])
            time.sleep(5)

        for log_entry in rundeck.execution_output_by_id(run['id'])['entries']:
            print("%s %s %s" % (log_entry['absolute_time'], log_entry['level'], log_entry['log']))

        if rundeck.execution_state(run['id'])['executionState'] != 'SUCCEEDED':
            exit(1)

