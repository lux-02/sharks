document.addEventListener('DOMContentLoaded', function() {
    var signOutBtn = document.getElementById('signOutBtn');

    if (signOutBtn) {
        signOutBtn.addEventListener('click', function(event) {
            event.preventDefault();

            fetch('/signout/')
            .then(function(response) {
                if (response.status === 200) {
                    sessionStorage.removeItem('username');
                    window.location.href = '/index/';
                } else {
                    console.error('Logout failed or error occurred');
                }
            })
            .catch(function(error) {
                console.error('Logout failed or error occurred', error);
            });
        });
    }
});
