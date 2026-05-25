# Re-export all models so Alembic's env.py picks them up via `import app.models`
from app.models.task import AssignedRole, Task, TaskState, STATES_ORDER

__all__ = ["Task", "AssignedRole", "TaskState", "STATES_ORDER"]
