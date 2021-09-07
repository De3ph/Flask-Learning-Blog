let loading_screen = document.querySelector('.loader');

window.addEventListener('load' , function(){
    loading_screen.style.display = 'none';
});

const message_content = document.querySelector('.message').innerHTML;

const message = document.querySelector('.message');

message.addEventListener('mouseover' , ()=> message.innerHTML='X');
message.addEventListener('mouseout' , ()=> message.innerHTML=message_content);

