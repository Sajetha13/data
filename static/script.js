// Sample extracted data (replace with your actual extracted data)
const extractedData = {
    name: "John Doe",
    age: "30",
    caste: "General",
    qualification: "Bachelor of Science in Computer Science"
};

// Injecting data into HTML
document.getElementById('name').innerText = extractedData.name;
document.getElementById('age').innerText = extractedData.age;
document.getElementById('caste').innerText = extractedData.caste;
document.getElementById('qualification').innerText = extractedData.qualification;

// Optional: Add download functionality for PDF (you can use libraries like jsPDF)
document.getElementById('downloadButton').onclick = function() {
    // Example code to generate PDF
    alert('Download functionality not implemented yet.');
};
