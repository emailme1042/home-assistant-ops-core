# /config/python_scripts/add_todo.py

task = data.get("task")
category = data.get("category")
if not task or not category:
    return

entity_map = {
    "Daily": "todo.daily_tasks",
    "Weekly": "todo.weekly_plan",
    "Admin": "todo.admin_assistant_tasks"
}
entity_id = entity_map.get(category)
if not entity_id:
    return

hass.services.call(
    "todo",
    "add_item",
    {"target": {"entity_id": entity_id}, "data": {"item": task}}
)
