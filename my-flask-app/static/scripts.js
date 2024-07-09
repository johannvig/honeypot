document.querySelectorAll('.honeypot').forEach(link => {
    link.addEventListener('click', (event) => {
        event.preventDefault();
        alert('Gotcha!');
    });
});
