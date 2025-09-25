(function () {
    const isEdit = new URLSearchParams(location.search).get('edit') === '1';
    if (isEdit) document.body.classList.add('pf-edit-mode');

    document.querySelectorAll('.card').forEach(card => {
        const rect = card.querySelector('.pf-rect');
        const input = card.querySelector('.pf-file');
        const img = card.querySelector('img');

        rect && rect.addEventListener('click', () => input && input.click());
        input && input.addEventListener('change', () => {
            const file = input.files && input.files[0];
            if (!file) return;
            img && (img.src = URL.createObjectURL(file));
            card.classList.add('changing');
        });
    });
})();
