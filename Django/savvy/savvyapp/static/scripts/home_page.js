document.addEventListener('DOMContentLoaded', (event) => {
    const postLink = document.getElementById('postLink');
    const overlay = document.getElementById('overlay');
    const postPopup = document.getElementById('postPopup');

    postLink.addEventListener('click', (e) => {
        e.preventDefault();
        overlay.style.display = 'block';
        postPopup.style.display = 'block';
    });

    overlay.addEventListener('click', () => {
        overlay.style.display = 'none';
        postPopup.style.display = 'none';
    });
});

setTimeout(function() {
    document.getElementById('messages').style.display = 'none';
}, 2000); 

document.getElementById('postForm').addEventListener('submit', function (e) {
    e.preventDefault();
    const content = document.getElementById('content').value;

    fetch('/api/posts/create/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify({ content })
    })
        .then(response => response.json())
        .then(post => {
            const postElement = document.createElement('li');
            postElement.className = 'post';
            postElement.textContent = post.content;
            document.getElementById('posts').prepend(postElement);
            document.getElementById('content').value = '';
        })
        .catch(error => console.error('Error:', error));
});

fetch('/api/posts/')
    .then(response => response.json())
    .then(posts => {
        posts.forEach(post => {
            const postElement = document.createElement('li');
            postElement.className = 'post';
            postElement.textContent = post.content;
            document.getElementById('posts').append(postElement);
        });
    })
    .catch(error => console.error('Error:', error));

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

