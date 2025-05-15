// Confirm the script has loaded correctly in the console
console.log("Script loaded correctly.");

// Run this code after the HTML document is fully loaded
document.addEventListener("DOMContentLoaded", () => {
    // Select the file input element on the page
    const input = document.querySelector('input[type="file"]');

    // Create a new <img> element to show the image preview
    const preview = document.createElement("img");
    preview.className = "preview"; // Apply CSS class for styling

    // Add the preview image to the page (appended at the bottom of <body>)
    document.body.appendChild(preview);

    // Listen for changes to the file input (when a user selects an image)
    input.addEventListener("change", () => {
        const file = input.files[0]; // Get the first selected file

        if (file) {
            // If a file is selected, create a temporary URL and set it as the image source
            preview.src = URL.createObjectURL(file);
            preview.style.display = "block"; // Make sure the image is visible
        } else {
            // If no file is selected, hide the preview image
            preview.style.display = "none";
        }
    });
});
