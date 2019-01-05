#!/usr/bin/python3

from eth_abi import decode_abi, decode_single
from eth_hash.auto import keccak
from hexbytes import HexBytes


def get_topics(abi):
    return dict((
        i['name'], "0x" + keccak("{}({})".format(
            i['name'],
            ",".join(x['type'] for x in i['inputs'])
        ).encode()).hex()
    ) for i in abi if i['type'] == "event" and not i['anonymous'])


def decode_event(event, abi):
    if type(abi) is list:
        topics = get_topics(abi).items()
        topic = next(k for k, v in topics if v == event['topics'][0])
        abi = next(
            i for i in abi if i['type'] == "event" and i['name'] == topic
        )
    result = {'name': abi['name'], 'data': []}
    types = [
        i['type'] if i['type'] != "bytes" else "bytes[]"
        for i in abi['inputs'] if not i['indexed']
    ]
    if types and event['data'] == "0x":
        event['data'] += "0" * (len(types)*64)
    decoded = list(decode_abi(types, HexBytes(event['data'])))[::-1]
    topics = event['topics'][:0:-1]
    for i in abi['inputs']:
        if i['indexed']:
            value = decode_single(i['type'], HexBytes(topics.pop()))
        else:
            value = decoded.pop()
        if type(value) is bytes:
            value = "0x" + value.hex()
        result['data'].append({
            'name': i['name'],
            'type': i['type'],
            'value': value
        })
    return result
