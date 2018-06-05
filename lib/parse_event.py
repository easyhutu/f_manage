"""
CREATE: 2018/5/26
AUTHOR:　HEHAHUTU
"""


def event_key(parse: dict):
    if 'event' in parse.keys():
        event = parse.get('event')
        parse.pop('event')
        return event
    else:
        return None
