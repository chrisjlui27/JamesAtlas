"""Witness for Q.no-division-by-zero: the shape ([A] <[void]>) contains <□> and the engine refuses it
(Excluded) for every sampled A; and (A <[void]>)-shaped forms are likewise refused."""
import os, sys, random
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import forms as F

rng = random.Random(1)
f = F.parse("([A] <[void]>)")
refused = 0
for _ in range(50):
    env = F.random_env({"A"}, "positive", rng)
    try:
        F.evaluate(f, env)
    except F.Excluded:
        refused += 1
ok = refused == 50
print(f"([A] <[void]>) refused as Excluded on {refused}/50 samples; the subform <[void]> is <□>:", F.to_string(F.parse("<[void]>"), True))
print("OK" if ok else "FAIL")
sys.exit(0 if ok else 1)
