export default function ajaxUpdate(url, formData, csrfToken) {

    if (confirm('Are you sure you want to update this item?')) {
        fetch(url, {
            method: 'PATCH',
            headers: {
                'X-CSRFToken': csrfToken,
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData)
        })
        .then(response => {
            if (!response.ok) {
                return response.json().then(errorData => {
                    form.querySelector('.form-errors').innerText = JSON.stringify(errorData.errors);
                    throw new Error('Network response was not ok');
                });
            }
            return response.json();
        })
        .then(data => {
            alert('The data was successfully updated!');
            window.location.reload();
        })
        .catch(error => {
            console.error('Error:', error);
            alert('An error occurred while updating the data.');
        });
    }
}