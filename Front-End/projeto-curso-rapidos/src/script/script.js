document.addEventListener('DOMContentLoaded', function() {
    // Código para os botões de toggle
    const buttons = document.querySelectorAll('.toggle-button');

    buttons.forEach(button => {
        const targetId = button.getAttribute('data-target');
        const content = document.getElementById(targetId);

        button.addEventListener('click', function() {
            content.classList.toggle('show');
        });
    });

    // Código para o botão Comprar
    const comprarButton = document.getElementById('comprar-button');
    const modal = document.createElement('div');
    const closeButton = document.createElement('span');

    modal.id = 'comprar-modal';
    modal.style.display = 'none';
    modal.style.position = 'fixed';
    modal.style.left = '0';
    modal.style.top = '0';
    modal.style.width = '100%';
    modal.style.height = '100%';
    modal.style.backgroundColor = 'rgba(0,0,0,0.5)';
    modal.style.zIndex = '1000';
    modal.style.overflow = 'auto';

    closeButton.className = 'close-button';
    closeButton.style.position = 'absolute';
    closeButton.style.top = '20px';
    closeButton.style.right = '20px';
    closeButton.style.fontSize = '24px';
    closeButton.style.color = '#fff';
    closeButton.style.cursor = 'pointer';
    closeButton.textContent = '×';

    modal.innerHTML = '<div style="margin: 15% auto; padding: 20px; background: #fff; border-radius: 5px; width: 80%; max-width: 500px;">' +
                      '<h2>Compra Confirmada</h2>' +
                      '<p>Sua compra foi realizada com sucesso!</p>' +
                      '<p>Obrigado por adquirir nosso curso.</p>' +
                      '</div>';
    modal.querySelector('div').appendChild(closeButton);
    document.body.appendChild(modal);

    comprarButton.addEventListener('click', function() {
        modal.style.display = 'block';
    });

    closeButton.addEventListener('click', function() {
        modal.style.display = 'none';
    });

    window.addEventListener('click', function(event) {
        if (event.target === modal) {
            modal.style.display = 'none';
        }
    });
});
