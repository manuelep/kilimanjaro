#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime, date

def prettydelta(dt, T=lambda x: x, use_suffix=True):

    if not use_suffix:
        suffix = ''
    elif dt.days < 0:
        suffix = ' from now'
        dt = -dt
    else:
        suffix = ' ago'

    if dt.days >= 2 * 365:
        return T('%d years' + suffix) % int(dt.days // 365)
    elif dt.days >= 365:
        return T('1 year' + suffix)
    elif dt.days >= 60:
        return T('%d months' + suffix) % int(dt.days // 30)
    elif dt.days >= 27:  # 4 weeks ugly
        return T('1 month' + suffix)
    elif dt.days >= 14:
        return T('%d weeks' + suffix) % int(dt.days // 7)
    elif dt.days >= 7:
        return T('1 week' + suffix)
    elif dt.days > 1:
        return T('%d days' + suffix) % dt.days
    elif dt.days == 1:
        return T('1 day' + suffix)
    elif dt.seconds >= 2 * 60 * 60:
        return T('%d hours' + suffix) % int(dt.seconds // 3600)
    elif dt.seconds >= 60 * 60:
        return T('1 hour' + suffix)
    elif dt.seconds >= 2 * 60:
        return T('%d minutes' + suffix) % int(dt.seconds // 60)
    elif dt.seconds >= 60:
        return T('1 minute' + suffix)
    elif dt.seconds >= 10:
        return T('%d seconds' + suffix) % dt.seconds
    elif dt.seconds > 1:
        ts = dt.total_seconds()
        return T('%.3f seconds' + suffix) % ts
    elif dt.seconds == 1:
        return T('1 second' + suffix)
    else:
        ms = dt.total_seconds() * 1000
        return T('%.3f milliseconds' + suffix) % ms

def prettydate(d, utc=False, **kw):
    """ Courtesy of: https://github.com/web2py/web2py/blob/master/gluon/tools.py#L5536 """
    now = datetime.utcnow() if utc else datetime.now()

    if isinstance(d, datetime):
        dt = now - d
    elif isinstance(d, date):
        dt = now.date() - d
    else:
        raise NotImplementedError

    return prettydelta(dt, **kw)
