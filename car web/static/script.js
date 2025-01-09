fetch('/predict', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
})
.then(response => {
    console.log("Raw server response:", response);
    if (!response.ok) {
        throw new Error('Network response was not ok');
    }
    return response.json();
})
.then(data => {
    console.log("Server returned:", data);
    if (data.error) {
        document.getElementById('result').innerText = `Error: ${data.error}`;
    } else {
        document.getElementById('result').innerText = `Predicted Price: ${data.predicted_price}`;
    }
})
.catch(error => {
    console.error('Error:', error);
    document.getElementById('result').innerText = 'Error predicting price. Please try again.';
});
