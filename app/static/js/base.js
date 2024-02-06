const button = document.getElementById('LogMenuButton');

button.addEventListener('click', function () {
    const menu = document.getElementById('LogMenu');
    if (menu.classList.contains("show")) {
        menu.classList.add("hide");
        menu.classList.remove("show");
    } else {
        menu.classList.add("show");
        menu.classList.remove("hide");
    }
    console.log(menu)
})

buttonNotif = document.querySelector('i.fa-bell');

// buttonNotif.addEventListener('click', function () {
//         console.log('cliked')
//         const user_notif = document.querySelector('.user-notifications');
//         if(user_notif.style.display == 'block') {
//             user_notif.style.display = 'none';
//         }else {
//             user_notif.style.display = 'block'
//         }
// })

buttonNotif.addEventListener('click', function () {
    // console.log('cliked')
    const user_notif = document.querySelector('.user-notifications');
    if(user_notif.style.top == '-200px') {
        user_notif.style.top = '65px';
    }else {
        user_notif.style.top = '-200px'
    }
})



