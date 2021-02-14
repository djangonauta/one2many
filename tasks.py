#!/usr/bin/env python3

import invoke


@invoke.task(default=True)
def run_server(ctx):
    ctx.run('./projeto/manage.py runserver --settings=projeto.settings', pty=True)
