export default function ajaxDelete(url, csrfToken) {
    if (confirm('Are you sure you want to delete this item?')) {
        fetch(url, {
            method: 'DELETE',
            headers: {
                'X-CSRFToken': csrfToken,
                'Content-Type': 'application/json',
            },
        })
        .then(response => {
            if (response.ok) {
                alert('Item was successfully deleted');
                window.location.reload()
            } else {
                alert('An error occurred while deleting the item.');
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }
}