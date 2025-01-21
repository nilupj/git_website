document.addEventListener('DOMContentLoaded', () => {
    const alphabetButtons = document.querySelectorAll('.alphabet-btn');
    const topicSections = document.querySelectorAll('.topic-section');

    // Ensure buttons are sorted alphabetically by data-letter
    const sortedButtons = Array.from(alphabetButtons).sort((a, b) => {
        return a.dataset.letter.localeCompare(b.dataset.letter);
    });

    sortedButtons.forEach(button => {
        button.addEventListener('click', () => {
            const letter = button.dataset.letter.toUpperCase(); // Ensure consistency with uppercase

            // Hide all sections
            topicSections.forEach(section => {
                section.classList.remove('active');
            });

            // Show the selected section
            const section = document.querySelector(`#section-${letter}`);
            if (section) {
                section.classList.add('active');
            } else {
                console.warn(`No section found for letter: ${letter}`);
            }
        });
    });
});
