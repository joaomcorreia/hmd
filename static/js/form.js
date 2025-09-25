document.addEventListener('DOMContentLoaded', function () {
    const checkboxes = document.querySelectorAll('.quote-item');
    const totalDisplay = document.getElementById('quoteTotal');
    const adminInputs = document.querySelectorAll('.admin-price');

    const prices = {};

    // Update checkbox label text with price
    function updateLabels() {
        checkboxes.forEach(cb => {
            const item = cb.dataset.item;
            const label = cb.parentElement;
            const price = prices[item] !== undefined ? prices[item] : '0';
            label.innerHTML = `<input type="checkbox" class="quote-item" data-item="${item}" ${cb.checked ? 'checked' : ''}> ${capitalize(item)} installeren (€${price})`;
        });

        // Re-bind checkboxes after innerHTML update
        bindCheckboxEvents();
    }

    // Update total cost
    function updateTotal() {
        let total = 0;
        const activeCheckboxes = document.querySelectorAll('.quote-item');
        activeCheckboxes.forEach(cb => {
            if (cb.checked) {
                const item = cb.dataset.item;
                total += prices[item] || 0;
            }
        });
        totalDisplay.textContent = total.toFixed(2);
    }

    // Capitalize first letter
    function capitalize(word) {
        return word.charAt(0).toUpperCase() + word.slice(1);
    }

    // Bind checkbox listeners
    function bindCheckboxEvents() {
        const checkboxes = document.querySelectorAll('.quote-item');
        checkboxes.forEach(cb => {
            cb.addEventListener('change', updateTotal);
        });
    }

    // Setup admin price inputs
    adminInputs.forEach(input => {
        const item = input.dataset.item;
        prices[item] = parseFloat(input.value);

        input.addEventListener('input', () => {
            prices[item] = parseFloat(input.value) || 0;
            updateLabels();
            updateTotal();
        });
    });

    updateLabels();
    updateTotal();
});
