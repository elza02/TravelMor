const button = document.getElementById('LogMenuButton');

button.addEventListener('click', function () {
    const menu = document.getElementById('LogMenu');
    if (menu.style.top == '-300px') {
        menu.style.top = '65px';
    } else {
        menu.style.top = '-300px';
    }
});

buttonNotif = document.querySelector('i.fa-bell');

buttonNotif.addEventListener('click', function () {
    const user_notif = document.querySelector('.user-notifications');
    if(user_notif.style.top == '-200px') {
        user_notif.style.top = '65px';
    }else {
        user_notif.style.top = '-200px'
    }
})



