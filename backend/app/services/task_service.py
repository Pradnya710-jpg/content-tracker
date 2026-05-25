# Task service — all business logic lives here, not in routes
#
# get_all_tasks(db)                 → list[Task]
# create_task(db, data: TaskCreate) → Task   (assigns createdAt server-side)
# update_task(db, id, data: TaskUpdate) → Task
#     uses model_dump(exclude_unset=True) so partial payloads work
#     enforces ROLE_CONFIG.canAdvance when state is changing
# delete_task(db, id)               → None
#     Admin-only enforcement goes here
