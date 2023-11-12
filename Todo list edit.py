<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Todo List</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }

        #todo-list {
            max-width: 400px;
            margin: 20px auto;
        }

        li {
            list-style-type: none;
            margin-bottom: 10px;
        }

        input[type="text"] {
            width: 60%;
            padding: 5px;
        }

        button {
            margin-left: 5px;
        }
    </style>
</head>
<body>

<div id="todo-list">
    <h2>Todo List</h2>
    <ul id="tasks"></ul>
    <input type="text" id="taskInput" placeholder="New task">
    <button onclick="addTask()">Add</button>
</div>

<script>
    function addTask() {
        var taskInput = document.getElementById("taskInput");
        var tasksList = document.getElementById("tasks");

        if (taskInput.value.trim() !== "") {
            var li = document.createElement("li");
            li.innerHTML = taskInput.value + ' <button onclick="editTask(this)">Edit</button>';
            tasksList.appendChild(li);
            taskInput.value = "";
        }
    }

    function editTask(button) {
        var li = button.parentElement;
        var taskText = li.firstChild.nodeValue.trim();
        var newText = prompt("Edit task:", taskText);

        if (newText !== null) {
            li.firstChild.nodeValue = newText + ' <button onclick="editTask(this)">Edit</button>';
        }
    }
</script>

</body>
</html>
