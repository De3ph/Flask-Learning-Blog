const loading_screen = document.querySelector('.loader');

const btn = document.querySelector('.darkMode');

let cookieExist = document.cookie.split(';').some((item) => item.trim().startsWith('theme='))

if (!cookieExist) {
    document.cookie = 'theme=light';
}


window.addEventListener('load', function () {

    if (document.cookie
        .split('; ')
        .find(row => row.startsWith('theme='))
        .split('=')[1] == "light") {
        document.body.classList.remove('none-background');
        btn.innerHTML = 'Dark Theme';

    }
    else if (document.cookie
        .split('; ')
        .find(row => row.startsWith('theme='))
        .split('=')[1] == "dark") {
        document.body.classList.add('none-background');
        btn.innerHTML = 'Light Theme';

    }
    loading_screen.style.display = 'none';
});


/* dark theme */

btn.addEventListener("click", function () {
    if (document.cookie
        .split('; ')
        .find(row => row.startsWith('theme='))
        .split('=')[1] == "light") {
        // enable dark mode 
        document.body.classList.add('none-background');
        document.cookie = 'theme=dark';
        btn.innerHTML = 'Light Theme';
    }
    else if (document.cookie
        .split('; ')
        .find(row => row.startsWith('theme='))
        .split('=')[1] == "dark") {
        // enable light mode
        document.body.classList.remove('none-background');
        document.cookie = 'theme=light';
        btn.innerHTML = 'Dark Theme';
    }
})
