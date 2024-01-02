const button = document.getElementById('LogMenuButton');

button.addEventListener('click', function() {
    const menu = document.getElementById('LogMenu');
    if(menu.classList.contains("show")){
        menu.classList.add("hide");
        menu.classList.remove("show");
    }else{
        menu.classList.add("show");
        menu.classList.remove("hide");
    }
    console.log(menu)
})
