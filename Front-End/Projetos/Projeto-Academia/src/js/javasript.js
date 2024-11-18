let currentSlide = 0;
const slides = document.querySelectorAll('.slide');

function showSlide() {
    slides.forEach((slide, index) => {
        slide.style.opacity = index === currentSlide ? '1' : '0';
    });
    currentSlide = (currentSlide + 1) % slides.length;
}

setInterval(showSlide, 5000);
showSlide();


// Formatação dinâmica para CEP
function formatarCEP(campo) {
    let cep = campo.value.replace(/\D/g, ""); // Remove caracteres não numéricos
    if (cep.length > 5) {
        cep = cep.substring(0, 5) + "-" + cep.substring(5, 8);
    }
    campo.value = cep;
}

// Validação do CEP
function validarCEP(campo) {
    const cep = campo.value;
    const regexCEP = /^[0-9]{5}-[0-9]{3}$/; // Formato 12345-678
    if (!regexCEP.test(cep)) {
        mostrarErro(campo, "CEP inválido! Use o formato 12345-678.");
    } else {
        limparErro(campo);
    }
}

// Formatação dinâmica para Telefones
function formatarTelefone(campo) {
    let telefone = campo.value.replace(/\D/g, ""); // Remove caracteres não numéricos
    if (telefone.length > 10) {
        telefone = `(${telefone.substring(0, 2)}) ${telefone.substring(2, 7)}-${telefone.substring(7, 11)}`;
    } else if (telefone.length > 6) {
        telefone = `(${telefone.substring(0, 2)}) ${telefone.substring(2, 6)}-${telefone.substring(6, 10)}`;
    } else if (telefone.length > 2) {
        telefone = `(${telefone.substring(0, 2)}) ${telefone.substring(2)}`;
    }
    campo.value = telefone;
}

// Validação do Telefone
function validarTelefone(campo) {
    const telefone = campo.value.replace(/\D/g, ""); // Remove caracteres não numéricos
    const regexTelefone = /^[1-9]{2}(9[0-9]{8}|[2-8][0-9]{7})$/; // Celular e fixo
    if (!regexTelefone.test(telefone)) {
        mostrarErro(campo, "Número inválido! Use o formato (xx) xxxx-xxxx ou (xx) xxxxx-xxxx.");
    } else {
        limparErro(campo);
    }
}

// Função para exibir mensagens de erro
function mostrarErro(campo, mensagem) {
    campo.classList.add("erro");
    campo.setCustomValidity(mensagem);
    campo.reportValidity();
}

// Função para limpar mensagens de erro
function limparErro(campo) {
    campo.classList.remove("erro");
    campo.setCustomValidity("");
}

// Função para limpar todo o formulário
function limparFormulario() {
    const form = document.getElementById("form-inscricao");
    form.reset();

    // Remove erros visuais
    const campos = document.querySelectorAll(".erro");
    campos.forEach(campo => limparErro(campo));
}
