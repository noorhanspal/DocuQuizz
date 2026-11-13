const fileInput = document.getElementById("document");
const fileName = document.getElementById("file-name");

fileInput.addEventListener("change", function () {

    const file = fileInput.files[0];

    if (file) {
        fileName.textContent = "Selected: " + file.name;
    } else {
        fileName.textContent = "No file selected";
    }

});