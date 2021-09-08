let loading_screen = document.querySelector('.loader');

window.addEventListener('load' , function(){
    loading_screen.style.display = 'none';
});


let btn = document.querySelector('.darkMode')

let currentTheme = localStorage.getItem("theme")

function turnBlack() {
    // document.body.style.background = 'black';

    document.body.style.background = 'none';
    document.body.classList.add('bg-black');
}
