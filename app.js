document.getElementById('runButton').onclick = async () => {
    try {
        const response = await fetch('http://localhost:5000/run', { method: 'POST' });
        const data = await response.json();
        console.log(data); // Обработайте вывод по желанию
    } catch (error) {
        console.error('Ошибка:', error);
    }
};
