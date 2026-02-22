// Function to handle switching between pages without loading
function showSection(sectionId) {
    // Hide all sections first
    const sections = document.querySelectorAll('.content-section');
    sections.forEach(section => {
        section.classList.remove('active');
    });

    // Show the targeted section
    const activeSection = document.getElementById(sectionId);
    activeSection.classList.add('active');

    // Scroll to the top of the page smoothly
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
}

// Simple effect to highlight active nav link (Optional)
document.querySelectorAll('.nav-links a').forEach(link => {
    link.addEventListener('click', function() {
        document.querySelectorAll('.nav-links a').forEach(l => l.style.color = '#94a3b8');
        this.style.color = 'white';
    });
});
