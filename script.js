// Genel Portfolyo Etkileşim Dosyası

document.addEventListener('DOMContentLoaded', () => {
    console.log("Portfolyo başarıyla yüklendi.");

    // Sayfa içindeki linklere yumuşak geçiş (smooth scroll) ekler
    const links = document.querySelectorAll('a[href^="#"]');
    links.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });

    // Proje kutularına basit bir parlama efekti verir
    const boxes = document.querySelectorAll('.gpa-box, .badge');
    boxes.forEach(box => {
        box.addEventListener('mouseenter', () => {
            box.style.opacity = '0.8';
        });
        box.addEventListener('mouseleave', () => {
            box.style.opacity = '1';
        });
    });
});
