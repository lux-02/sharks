
var username = sessionStorage.getItem('username');

if (username) {
    document.querySelector('.card-list').textContent = sessionStorage.getItem('username') + "님께 추천해요 !";
}