
document.getElementById('signin_btn').addEventListener('click', function () {
    event.preventDefault()
    
    const username = document.getElementById('user_name').value;
    const password = document.getElementById('user_pw').value;
    const csrfToken = document.querySelector('[name="csrfmiddlewaretoken"]').value;

    fetch('/submit_signin/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken,
        },
        body: JSON.stringify({user_name: username, user_pw: password})
    })
    .then(response => response.json())
    .then(data => {
        if (data.message === 'Login successful !') {
            alert("Hello, " + data.user_name + "!");
            sessionStorage.setItem('username', data.user_name);
            window.location.href = data.previous_url;
        } else {
            alert("User not found");
            document.getElementById('user_name').value = '';
            document.getElementById('user_pw').value = '';
        }
    })
    .catch(() => {
        alert("Error");
    });
});
