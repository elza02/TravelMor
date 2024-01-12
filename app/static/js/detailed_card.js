let slideIndex = 1;
showSlides(slideIndex);

function plusSlides(n) {
showSlides(slideIndex += n);
}

function currentSlide(n) {
showSlides(slideIndex = n);
}

function showSlides(n) {
let i;
let slides = document.getElementsByClassName("mySlides");
let dots = document.getElementsByClassName("demo");
let captionText = document.getElementById("caption");
if (n > slides.length) {slideIndex = 1}
if (n < 1) {slideIndex = slides.length}
for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
}
for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
}
slides[slideIndex-1].style.display = "block";
dots[slideIndex-1].className += " active";
captionText.innerHTML = dots[slideIndex-1].alt;
}


const evaluation_divs1 = document.querySelectorAll('div[class="evaluation"]');
document.addEventListener('DOMContentLoaded', function() {
    evaluation_divs1.forEach((ev_div) => {
        let stars = parseInt(ev_div.dataset.stars);
        let icons = ev_div.querySelectorAll('i');
        icons.forEach((icon, index) => {
            if (index < stars) {
                icon.classList.add('checked');
            }
        });
    });
});

const rating_stars = document.querySelectorAll('div[class="evaluation-interact"]');

rating_stars.forEach((star) => {
star.addEventListener('click', function(event) {
    let target = event.target;
    
    if (target.tagName === 'I') {
        let index = Array.from(target.parentNode.children).indexOf(target);
        // console.log(index);
        let icons = target.parentNode.querySelectorAll('i');
        icons.forEach((icon, i) => {
            if (i <= index) {
            icon.classList.add('checked');
            } else {
            icon.classList.remove('checked');
            }
        });
        star.dataset.stars = index + 1;
    }
});
});


var stars = document.querySelectorAll('.star');
var rating = 0;
stars.forEach(function(star, index) {
star.addEventListener('mouseenter', function() {
    stars.forEach(function(innerStar, innerIndex) {
    if (innerIndex <= index) {
        innerStar.classList.add('yellow');
    }
    else {
        innerStar.classList.remove('yellow');
    }
    });
});
star.addEventListener('mouseleave', function() {
    stars.forEach(function(innerStar, innerIndex) {
    if (innerIndex < rating) {
        innerStar.classList.add('yellow');
    }
    else {
        innerStar.classList.remove('yellow');
    }
    });
});
// star.addEventListener('click', function() {
//     rating = index + 1;
//     document.getElementById('output').innerHTML = 'Rating: ' + rating;
// });
});