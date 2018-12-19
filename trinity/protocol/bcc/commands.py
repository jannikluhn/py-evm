from typing import (
    Tuple,
    Union,
)

from rlp import sedes

from mypy_extensions import (
    TypedDict,
)

from eth_typing import (
    Hash32,
)

from p2p.protocol import (
    Command,
)

from trinity.rlp.sedes import (
    HashOrNumber,
)

from eth.beacon.types.blocks import BaseBeaconBlock
from eth.beacon.types.attestations import Attestation


RequestMessage = TypedDict("RequestMessage", {
    "request_id": int,
})


ResponseMessage = TypedDict("ResponseMessage", {
    "request_id": int,
})

StatusMessage = TypedDict("StatusMessage", {
    'protocol_version': int,
    'network_id': int,
    'genesis_hash': Hash32,
    'head_slot': int,
})


class Status(Command):
    _cmd_id = 0
    structure = [
        ('protocol_version', sedes.big_endian_int),
        ('network_id', sedes.big_endian_int),
        ('genesis_hash', sedes.binary),
        ('head_slot', sedes.big_endian_int),
    ]


GetBeaconBlocksMessage = TypedDict("GetBeaconBlocksMessage", {
    "request_id": int,
    "block_slot_or_root": Union[int, Hash32],
    "max_blocks": int,
})


class GetBeaconBlocks(Command):
    _cmd_id = 1
    structure = [
        ('request_id', sedes.big_endian_int),
        ('block_slot_or_root', HashOrNumber()),
        ('max_blocks', sedes.big_endian_int),
    ]


BeaconBlocksMessage = TypedDict("BeaconBlocksMessage", {
    'request_id': int,
    'blocks': Tuple[BaseBeaconBlock, ...],
})


class BeaconBlocks(Command):
    _cmd_id = 2
    structure = [
        ('request_id', sedes.big_endian_int),
        ('blocks', sedes.CountableList(BaseBeaconBlock)),
    ]


class AttestationRecords(Command):
    _cmd_id = 3
    structure = sedes.CountableList(Attestation)
