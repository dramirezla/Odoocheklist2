function toggleSelection(element) {
    element.classList.toggle('selected');
}

function countSelectedParts() {
    const selectedButtons = document.querySelectorAll('.button.selected');
    const selectedParts = Array.from(selectedButtons).map(button => button.textContent.trim());

    const resultDiv = document.getElementById('selected-parts-result');
    if (selectedParts.length > 0) {
        resultDiv.innerHTML = `
            <p>Has seleccionado <strong>${selectedParts.length}</strong> partes:</p>
            <ul>${selectedParts.map(part => `<li>${part}</li>`).join('')}</ul>
        `;
    } else {
        resultDiv.innerHTML = '<p>No has seleccionado ninguna parte.</p>';
    }
}