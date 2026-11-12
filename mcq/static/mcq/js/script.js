
const fileInput = document.getElementById("document");
const fileName = document.getElementById("file-name");
const generateBtn = document.getElementById("generate-btn");
const message = document.getElementById("message");

fileInput.addEventListener("change", function () {
    const file = fileInput.files[0];

    if (file) {
        fileName.textContent = "Selected: " + file.name;
    } else {
        fileName.textContent = "No file selected";
    }
});

generateBtn.addEventListener("click", function () {
    const file = fileInput.files[0];

    if (!file) {
        message.textContent = "Please select a document first.";
        return;
    }

    message.textContent =
        "File selected successfully! Backend upload coming next.";
});
