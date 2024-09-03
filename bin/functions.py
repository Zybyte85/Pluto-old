import os
import json

app_path = os.path.dirname(os.path.dirname(__file__))


def handle_button_click(button):
    button_text = button.text()  # Get the text of the button
    print("Button pressed:", button_text)


def load_json(filename="data/tasks.json"):
    with open(os.path.join(app_path, filename), "r") as file:
        return json.load(file)


def write_json(new_data, priority, filename="data/tasks.json"):
    with open(os.path.join(app_path, filename), "r+") as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data[priority].append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent=4)
        print("Wrote task to json file")


def load_tasks_from_dict(app_class, app, data):
    for y in data.keys():
        for i in range(data[y].__len__()):
            app_class.make_task(
                app,
                y,
                data[y][i]["text"],
                data[y][i]["due_date"],
                data[y][i]["due_time"],
                True,
            )
