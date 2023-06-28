
const message_container = document.querySelector('.messages');
const form = document.querySelector('form');

form.addEventListener('submit', (e) => {
 e.preventDefault();


 var inputValue = document.getElementById("send").value;
 const input_box = document.querySelector('input');
 message_container.innerHTML += `<div class="self">${inputValue}</div> `;
 $.ajax({
    type: 'GET',
    url: '/create/',
    data:{'msg': inputValue},
    success:function(data){
        console.log(data);
        message_container.innerHTML += `<div class="mess"><div class="abc"><i class="fa-solid fa-message-bot"></i>></div><div class="bot">${data}</div></div>`;
    }
  });
input_box.value='';
});
