# Tasks Cheklist.md

*(Analytical Part - Exploratory Testing, Happy Paths Only)*

**Testing Approach**

This testing apprach was inteded to focus only on happy paths and expected positive behavior using the exploratory testing techniques; It was explored from the a real user perspective, indentifiying the main flows an grouping them into meaningful functional sections (Task Creation, Task List Visualization, Task Completion, Filter and Sorting, Task Editing, Attachments Managment, Quick Add Task)

## Task Creation Functionality

* **Automated** : Core creation flow using required fields
* **Manual** : Exploratory validation of optional fields and UI behavior

**Checklist:**

* [ ] User can open the Create Task form.
* [ ] User can create a task using only Task Name (required field).
* [ ] User can create a task with all optional fields filled (Description, Due On, Priority, Client, Attachments).
* [ ] User can select a date using the date picker.
* [ ] User can select a time using the time picker.
* [ ] User can select a value from Priority Dropdown.
* [ ] User can select a value from Client Dropdown.
* [ ] User can upload attachments successfully until (until 20 files or 50mb size limit).
* [ ] User can save the task using the Save button.
* [ ] Newly created task appears in the Task list.
* [ ] Newly created task appears at the top of the list.



## Task List Visualization

* **Automated** : Task visibility and ordering
* **Manual** : Visual validation (colors, labels)

**Checklist:**

* [ ] User can access the Task Page.
* [ ] User can view a list of existing tasks.
* [ ] Tasks are displayed in a stacked list format.
* [ ] The most recently created task is shown on top
* [ ] Each task displays:
  * [ ] Task name
  * [ ] Due date and time
  * [ ] Priority with a correct color
  * [ ] Client as a clickable link
  * [ ] Checkbox for completion state

## Task Completion

**Checklist:**

* [ ] User can mark a task as Completed using the checkbox.
* [ ] Task status updates successfully to Completed.
* [ ] Completed task shows the correct visual indicator.
* [ ] Task remains visible in the task list after completion.



## Filters and Sorting Functionality

* **Automated** : Filter behavior
* **Manual** : Exploratory validation of sorting combinations

**Checklist:**

* [ ] User can filter tasks by All.
* [ ] User can filter task by Completed.
* [ ] User can filter task by Incomplete.
* [ ] User can sort task using:
  * [ ] Custom
  * [ ] Due Date
  * [ ] Date Created
  * [ ] Priority
* [ ] Filtered results show only expected tasks.
* [ ] User can find a task by text match.



## Task Editing Functionality

* **Automated** : Editing and saving changes
* **Manual** : Attachment management

**Checklist:**

* [ ] User can open an existing task for editing.
* [ ] User can update Task Name.
* [ ] User can update Description.
* [ ] User can update Due Date and Time.
* [ ] User can update Priority.
* [ ] User can update Client.
* [ ] User can save changes successfully.
* [ ] Updated information is reflected in the task list.
* [ ] Task position in the list remains unchanged after editing.



## Attachments Management

* **Manual preferred** (low ROI for automation)

**Checklist:**

* [ ] User can upload attachments to task.
* [ ] User can download an attachment.
* [ ] User can rename and attachment.
* [ ] User can delete and attachment.
* [ ] Attachment list updates correctly after each action.
* [ ] User can't attach more than 20 files.
* [ ] User can't attach more then 50mb of size.



## Quick Add Task Creation

* **Automated** : Inline creation happy path
* **Manual** : Exploratory UX validation

Checklist:

* [ ] User can create with a task using Quick Add.
* [ ] Task is created with only a Task Name.
* [ ] Task appears immediately in the task list.
* [ ] Task appear at the top of the list.
* [ ] Task is created without opening the full form.
