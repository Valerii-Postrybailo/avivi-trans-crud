import ajaxDelete from './delete.js'
import getCookie from './get_csrf_token.js'
import ajaxUpdate from './patch.js'
        

document.addEventListener('DOMContentLoaded', function () {
    document.body.addEventListener('click', function (event) {
        const target = event.target;

        if (target.classList.contains('delete-btn')) {
            event.preventDefault();

            const url = target.getAttribute('data-url');
            const csrfToken = getCookie('csrftoken');

            ajaxDelete(url, csrfToken);
        }
    });
});

document.addEventListener('DOMContentLoaded', function () {
    const updateButtons = document.querySelectorAll('.update-bot-button');
    updateButtons.forEach(button => {
        button.addEventListener('click', function (event) {
            event.preventDefault();
            const form = button.closest('form');
            const url =  this.getAttribute('data-url');
            const csrfToken = getCookie('csrftoken');
            
            const formData = {
                bot_name: form.querySelector('.bot-name').value,
                api_key: form.querySelector('.api-key').value,
                webhook_url: form.querySelector('.webhook-url').value
            };
            ajaxUpdate(url, formData, csrfToken)
        });
    });
});