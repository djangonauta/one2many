#!/usr/bin/env python3

import invoke


@invoke.task(default=True)
def run_server(ctx):
    ctx.run('./manage.py runserver 0.0.0.0:8000 --settings=projeto.settings', pty=True)
