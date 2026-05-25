"""Seed the tasks table from specs/seed-data.json.

Idempotent: records whose id already exists in the database are skipped,
so running this script multiple times never creates duplicates.

Usage:
    uv run python seed.py
"""
import asyncio
import json
from datetime import date
from pathlib import Path

from sqlalchemy import func, select

from app.core.database import AsyncSessionLocal
from app.models.task import AssignedRole, Task, TaskState
import app.models  # noqa: F401 — registers all models with Base.metadata

SEED_FILE = Path(__file__).parent.parent / "specs" / "seed-data.json"


async def seed() -> None:
    records = json.loads(SEED_FILE.read_text(encoding="utf-8"))
    print(f"Loaded {len(records)} records from {SEED_FILE.name}\n")

    inserted = 0
    skipped = 0

    async with AsyncSessionLocal() as db:
        for rec in records:
            existing = await db.get(Task, rec["id"])
            if existing is not None:
                print(f"  SKIP   id={rec['id']:>2}  {rec['title']!r}")
                skipped += 1
                continue

            task = Task(
                id=rec["id"],
                title=rec["title"],
                description=rec["description"],
                assigned_role=AssignedRole(rec["assigned_role"]),
                state=TaskState(rec["state"]),
                created_at=date.fromisoformat(rec["created_at"]),
            )
            db.add(task)
            print(f"  INSERT id={rec['id']:>2}  {rec['title']!r}")
            inserted += 1

        await db.commit()

        # Verify total row count
        result = await db.execute(select(func.count()).select_from(Task))
        total = result.scalar_one()

    print(f"\n{inserted} inserted, {skipped} skipped.")
    print(f"Total tasks in database: {total}")


if __name__ == "__main__":
    asyncio.run(seed())
