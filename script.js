document.getElementById('imageInput').addEventListener('change', previewImage);
document.getElementById('applyFilterBtn').addEventListener('click', applyFilter);

function previewImage() {
    const file = document.getElementById('imageInput').files[0];
    const reader = new FileReader();
    
    reader.onload = function(e) {
        const img = new Image();
        img.src = e.target.result;
        img.onload = function() {
            document.getElementById('imagePreview').innerHTML = '';
            document.getElementById('imagePreview').appendChild(img);
        };
    };
    
    if (file) {
        reader.readAsDataURL(file);
    }
}

function applyFilter() {
    const fileInput = document.getElementById('imageInput');
    const filter = document.getElementById('filterSelect').value;
    
    if (!fileInput.files[0]) {
        alert("Please upload an image first!");
        return;
    }

    const formData = new FormData();
    formData.append('image', fileInput.files[0]);
    formData.append('filter', filter);

    // Show loading spinner
    document.getElementById('loadingSpinner').style.display = 'block';

    fetch('http://127.0.0.1:5000/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        // Hide loading spinner
        document.getElementById('loadingSpinner').style.display = 'none';

        // Redirect to the result page with the filtered image
        window.location.href = `result.html?filename=${data.filename}`;
    })
    .catch(error => {
        console.error("Error:", error);
        document.getElementById('loadingSpinner').style.display = 'none';
        alert("Error applying filter. Please try again.");
    });
}
