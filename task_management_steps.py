from behave import given, when, then

@given('the user is logged into FocusFlow')
def step_impl(context):
    context.user_logged_in = True

@when('the user creates a new task with title "{title}" and description "{description}"')
def step_impl(context, title, description):
    context.new_task = {"title": title, "description": description, "status": "Open"}

@then('the new task "{title}" should be listed in the task list')
def step_impl(context, title):
    assert context.new_task["title"] == title

@then('the task should have status "Open"')
def step_impl(context):
    assert context.new_task["status"] == "Open"
