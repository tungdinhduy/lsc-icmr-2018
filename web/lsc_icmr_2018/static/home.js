function appendLocation() {
    var textbox = document.createElement("input");
    textbox.type = "text";
    textbox.placeholder = "new location ...";
    parent = document.getElementById("locations");
    parent.appendChild(textbox)
}