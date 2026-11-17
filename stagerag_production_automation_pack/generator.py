"""Synthetic record generator for StageRAG Production Automation Pack (privacy-safe, deterministic with seed)."""
from __future__ import annotations

SUPPORTED_SCHEMAS = ("default", 'generic')


def generate_records(rows: int, schema_name: str = "default", seed: int | None = None) -> list[dict]:
    if rows < 1:
        raise ValueError("rows must be >= 1")
    if schema_name not in SUPPORTED_SCHEMAS:
        raise ValueError(f"unsupported schema: {schema_name}")
    import random
    from datetime import datetime, timedelta

    rng = random.Random(seed) if seed is not None else random.Random()
    out = []
    for i in range(rows):
        out.append({
            "id": f"R{100000 + i}",
            "name": f"Sample {i}",
            "category": rng.choice(["alpha", "beta", "gamma", "delta"]),
            "value": round(rng.uniform(1, 1000), 2),
            "quantity": rng.randint(1, 500),
            "active": rng.choice([True, False]),
            "created_at": (datetime(2024, 1, 1) + timedelta(days=rng.randint(0, 700))).strftime("%Y-%m-%d"),
        })
    return out
