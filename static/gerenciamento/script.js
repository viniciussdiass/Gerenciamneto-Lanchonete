function confirmarExclusao(nome) {
    return confirm(`Tem certeza que deseja excluir ${nome}?`);
}

document.addEventListener('DOMContentLoaded', function () {
    const submitButtons = document.querySelectorAll('input[type="submit"], button[type="submit"]');
    
    submitButtons.forEach(button => {
        button.addEventListener('click', (event) => {
            button.textContent = 'Processando...';
            button.disabled = true;

            // Evitar o envio do formulário imediatamente
            const form = button.closest('form');
            if (form) {
                event.preventDefault();
                
                // Simular a execução de algum processo (se necessário)
                setTimeout(() => {
                    form.submit(); // Enviar o formulário após o processamento
                }, 2000); // Simulação de processamento de 2 segundos, você pode ajustar o tempo ou realizar outra ação antes de submeter
            }
        });
    });
});

function filtrarTabela() {
    const input = document.getElementById('filtroTabela');
    const filter = input.value.toLowerCase();
    const rows = document.querySelectorAll('table tbody tr');

    rows.forEach(row => {
        const cells = row.querySelectorAll('td');
        const match = Array.from(cells).some(cell => cell.textContent.toLowerCase().includes(filter));
        row.style.display = match ? '' : 'none';
    });
}
