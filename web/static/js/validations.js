// Função para validar o valor do input
function validateTransferForm() {
    var input = document.getElementById('new_user');
    var options = input.getElementsByTagName('option');
    var userInput = input.value.toLowerCase();
    for (var i = 1; i < options.length; i++) {
        var optionValue = options[i].value.toLowerCase();
        if (userInput === optionValue) {
            CallLoadScreen();
            return true;
        }
    }
    return false;
};

function validateDevolutionForm() {
    var ArmarioInput = document.getElementById('armario');
    if (ArmarioInput.value.trim() === "") {
        return false; 
    }
    CallLoadScreen();
    return true; 
}

function limitarTamanho(elemento, tamanhoMaximo) {
    if (elemento.value.length > tamanhoMaximo) {
        elemento.value = elemento.value.slice(0, tamanhoMaximo);
    }
}

document.querySelectorAll('[data-bs-toggle="collapse"]').forEach(function (button) {
    button.addEventListener('click', function () {
        var target = document.querySelector(button.getAttribute('data-bs-target'));
        var otherCollapseElements = document.querySelectorAll('.collapse.show');
        otherCollapseElements.forEach(function (element) {
            if (element !== target) {
                var bsCollapse = new bootstrap.Collapse(element);
                bsCollapse.hide();
            }
        });
    });
});
