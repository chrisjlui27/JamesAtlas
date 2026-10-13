"""Shared helpers for the rung-H witnesses: the ℍ reading (tools/quat.py) and exact quaternions."""
import os, sys, random, math
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
import forms as F  # noqa: E402
import quat as QT  # noqa: E402
from quat import Q, exp, log, close, PI, I, Jq, K  # noqa: E402,F401

RNG = random.Random(20261007)


def rand_q(lo=-2.0, hi=2.0):
    return QT.random_quaternion(RNG, lo, hi)


def unit():
    return QT.random_pure_unit(RNG)


def in_band(x: Q) -> bool:
    return x.imag_abs() < PI - 1e-6


def report(name, checks):
    fails = [(k, v) for k, v in checks if not v]
    for k, v in checks:
        print(f"  [{'ok' if v else 'FAIL'}] {k}")
    print(f"{name}: {len(checks) - len(fails)}/{len(checks)} checks pass")
    sys.exit(0 if not fails else 1)
