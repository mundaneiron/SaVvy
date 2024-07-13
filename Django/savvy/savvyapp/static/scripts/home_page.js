// y2k
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

    document.getElementById('postForm').addEventListener('submit', function (e) {
        e.preventDefault();
        const title = document.getElementById('title').value;  
        const content = document.getElementById('content').value;  

        fetch('/api/posts/create/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: JSON.stringify({ title, content })  
        })
        .then(response => response.json())
        .then(post => {
            if (post.title && post.content) {
                const postElement = document.createElement('li');
                postElement.className = 'post';
                postElement.innerHTML = `<strong>${post.title}</strong><br>${post.content}`;  
                document.getElementById('posts').prepend(postElement);
                document.getElementById('title').value = '';  
                document.getElementById('content').value = '';  
            }
        })
        .catch(error => console.error('Error:', error));
    });

    fetch('/api/posts/')
        .then(response => response.json())
        .then(posts => {
            posts.forEach(post => {
                if (post.title && post.content) {
                    const postElement = document.createElement('li');
                    postElement.className = 'post';
                    postElement.innerHTML = `<strong>${post.title}</strong><br>${post.content}`;  
                    document.getElementById('posts').append(postElement);
                }
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
});
