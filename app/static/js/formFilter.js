document.getElementById('filterFormId').addEventListener('click', function () {
    var locationFilter = document.getElementById('locationFilter').value.toLowerCase();
    var elements = document.getElementsByClassName('filterable');
    for (var i = 0; i < elements.length; i++) {
        var element = elements[i];
        var content = element.innerText.toLowerCase();

        if (locationFilter === '' || content.includes(locationFilter)) {
            element.style.display = '';
        } else {
            element.style.display = 'none';
        }
    }
});