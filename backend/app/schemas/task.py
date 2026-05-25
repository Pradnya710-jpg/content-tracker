# Pydantic v2 schemas for Task
#
# TaskCreate   — POST /api/tasks body (title, description, assignedRole, state)
#                id and createdAt are NOT sent — server assigns them
#
# TaskUpdate   — PUT /api/tasks/{id} body (all fields Optional)
#                Backend must accept any subset; service layer uses
#                model_dump(exclude_unset=True) to patch only supplied fields
#
# TaskResponse — wire shape returned by GET / POST / PUT
#                camelCase aliases required: assignedRole, createdAt
#                Use Field(alias=...) + ConfigDict(populate_by_name=True)
