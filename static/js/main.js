document.addEventListener('DOMContentLoaded', function() {
    const umb = document.querySelector('#user-menu-button');
    const um = umb.nextElementSibling;
    umb.addEventListener('click', function() {
        um.classList.toggle('hidden');
        event.stopPropagation();
    });
    document.addEventListener('click',function (event) {
        if(!umb.contains(event.target)&&!um.contains(event.target)){
            um.classList.add('hidden');
        }
    })
});
