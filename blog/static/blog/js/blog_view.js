
var username = sessionStorage.getItem('username');

if (username) {
    document.querySelector('.card-list').textContent = "Recommended for" + sessionStorage.getItem('username') + '!';
}