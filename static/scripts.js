document.getElementById('draw-button').addEventListener('click', function() {
    const spread = document.getElementById('spread').value;

    fetch(`/.netlify/functions/draw_cards?spread=${spread}`)
        .then(response => response.json())
        .then(data => {
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '';

            data.cards.forEach(card => {
                const img = document.createElement('img');
                img.src = `data:image/png;base64,${card.image}`;
                resultDiv.appendChild(img);
            });
        })
        .catch(error => {
            console.error('Error:', error);
        });
});
