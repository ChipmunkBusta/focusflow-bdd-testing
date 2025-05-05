Feature: Task Management

  Scenario: User adds a new task
    Given the user is logged into FocusFlow
    When the user creates a new task with title "Complete homework" and description "Finish math homework"
    Then the new task "Complete homework" should be listed in the task list
    And the task should have status "Open"
