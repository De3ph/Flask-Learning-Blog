let btn = document.querySelector('.darkMode')

let currentTheme = localStorage.getItem("theme")

function turnBlack() {
    // document.body.style.background = 'black';

    document.body.style.background = 'none';
    document.body.classList.add('bg-black');
}
