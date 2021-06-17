#!/usr/bin/env python

ZERO = float(0)
ONE_HUNDRED = float(100)


def _assert(value, expected_type):
    if not isinstance(value, expected_type):
        raise ValueError


def get_percentage(part: float, whole: float) -> float:
    _assert(part, float)
    _assert(whole, float)

    return ZERO if whole == ZERO else whole * part / ONE_HUNDRED


def percentage_of(part: float, whole: float) -> float:
    _assert(part, float)
    _assert(whole, float)

    return ZERO if whole == ZERO else ONE_HUNDRED * part / whole


def increment(increment: float, whole: float) -> float:
    _assert(increment, float)
    _assert(whole, float)

    return ZERO if whole == ZERO else whole + get_percentage(increment, whole)


def decrement(decrement: float, whole: float) -> float:
    _assert(decrement, float)
    _assert(whole, float)

    return ZERO if whole == ZERO else whole - get_percentage(decrement, whole)
