const box = document.getElementById('myBox');

box.addEventListener('mouseenter', () => {
    box.style.width = '150px';
    box.style.height = '150px';
    box.style.backgroundColor = 'blue';
});

box.addEventListener('mouseleave', () => {
    box.style.width = '100px';
    box.style.height = '100px';
    box.style.backgroundColor = 'red';
});

box.addEventListener('click', () => {
    box.style.transform = 'translateY(200px)';
    box.style.backgroundColor = 'green';
});