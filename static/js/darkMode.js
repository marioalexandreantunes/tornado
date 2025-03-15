// Function to set theme based on system preference or saved preference
function setTheme(isDark) {
    if (isDark) {
        document.documentElement.classList.add('dark');
    } else {
        document.documentElement.classList.remove('dark');
    }
    localStorage.setItem('darkMode', isDark);
}

// Check for saved preference first
const savedTheme = localStorage.getItem('darkMode');
if (savedTheme !== null) {
    setTheme(savedTheme === 'true');
} else {
    // If no saved preference, use system preference
    setTheme(window.matchMedia('(prefers-color-scheme: dark)').matches);
}

// Listen for system theme changes
window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
    if (localStorage.getItem('darkMode') === null) {
        setTheme(e.matches);
    }
});

function toggleDarkMode() {
    const isDark = !document.documentElement.classList.contains('dark');
    setTheme(isDark);
}