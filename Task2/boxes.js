function allowDrop(event) {
    event.preventDefault();
}

function drag(event) {
    // sets the data to the id of the target.
    event.dataTransfer.setData("text", event.target.id);

}

function drop(event) {
    event.preventDefault();
    // gets the id of the targeted element
    let data = event.dataTransfer.getData("text");
    event.target.appendChild(document.getElementById(data));

    let source = document.getElementById("source");
    let target1 = document.getElementById("target1");
    let target2 = document.getElementById("target2");
    let status_source = document.getElementById("status-source");
    let status_target1 = document.getElementById("status-target1");
    let status_target2 = document.getElementById("status-target2");

    // Set the different paragraphs so that 
    //they show how many pictures there are in the different boxes
    status_source.innerHTML = "source " + source.children.length;
    status_target1.innerHTML = "target1 " + target1.children.length;
    status_target2.innerHTML = "target2 " + target2.children.length;

}

function init() {
    // Gets the number of pictures in the different boxes on page load.
    document.getElementById("status-source").innerHTML = "source " + document.getElementById("source").children.length;
    document.getElementById("status-target1").innerHTML = "target1 " + document.getElementById("target1").children.length;
    document.getElementById("status-target2").innerHTML = "target2 " + document.getElementById("target2").children.length;

}

window.onload = init;