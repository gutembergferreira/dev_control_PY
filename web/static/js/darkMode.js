// Função para verificar o estado do modo noturno no carregamento da página
function checkDarkMode() {
    var toggleDarkMode = document.getElementById('toggleDarkMode');
    var tableElement = document.getElementById('table-responsive');
    var tableallTransactions = document.getElementById('collapseExample');
    var tableallLoans = document.getElementById('collapseTwo');
    var tableallDevolution = document.getElementById('collapseThree');
    var tableallTransfer = document.getElementById('collapseFour');
    var tablemydevices = document.getElementById('mydevices');
    var tableAllDevices = document.getElementById('tableAllDevices');
    var tableAllAccessories = document.getElementById('tableAccessories');
    // Verificar se o estado do modo noturno está armazenado
    if (localStorage.getItem('darkMode') === 'true') {
        document.body.classList.add('dark-mode');
        toggleDarkMode.checked = true;
        if(tableAllDevices){tableAllDevices.setAttribute('data-bs-theme', 'dark');}
        if(tableElement){tableElement.setAttribute('data-bs-theme', 'dark');}
        if(tableallTransactions){tableallTransactions.setAttribute('data-bs-theme', 'dark');}
        if(tableallLoans){tableallLoans.setAttribute('data-bs-theme', 'dark');}
        if(tableallDevolution){tableallDevolution.setAttribute('data-bs-theme', 'dark');}
        if(tableallTransfer){tableallTransfer.setAttribute('data-bs-theme', 'dark');}
        if(tablemydevices){tablemydevices.setAttribute('data-bs-theme', 'dark');};
        if(tableAllAccessories){tableAllAccessories.setAttribute('data-bs-theme', 'dark');};
    } else {
        document.body.classList.remove('dark-mode');
        toggleDarkMode.checked = false;
        if(tableAllDevices){tableAllDevices.setAttribute('data-bs-theme', 'light');}
        if(tableElement){tableElement.setAttribute('data-bs-theme', 'light');}
        if(tableallTransactions){tableallTransactions.setAttribute('data-bs-theme', 'light');}
        if(tableallLoans){tableallLoans.setAttribute('data-bs-theme', 'light');}
        if(tableallDevolution){tableallDevolution.setAttribute('data-bs-theme', 'light');}
        if(tableallTransfer){tableallTransfer.setAttribute('data-bs-theme', 'light');}
        if(tablemydevices){tablemydevices.setAttribute('data-bs-theme', 'light');}
        if(tableAllAccessories){tableAllAccessories.setAttribute('data-bs-theme', 'light');}
    }
}

// Função para alternar o modo noturno
function toggleDarkMode() {
    var toggleDarkMode = document.getElementById('toggleDarkMode');
    var tableElement = document.getElementById('table-responsive');
    var tableallTransactions = document.getElementById('collapseExample');
    var tableallLoans = document.getElementById('collapseTwo');
    var tableallDevolution = document.getElementById('collapseThree');
    var tableallTransfer = document.getElementById('collapseFour');
    var tablemydevices = document.getElementById('mydevices');
    var tableAllDevices = document.getElementById('tableAllDevices');
    var tableAllAccessories = document.getElementById('tableAccessories');
    if (toggleDarkMode.checked) {
        // Ativar o modo noturno
        document.body.classList.add('dark-mode');
        localStorage.setItem('darkMode', 'true');
        if(tableElement){tableElement.setAttribute('data-bs-theme', 'dark');}
        if(tableallTransactions){tableallTransactions.setAttribute('data-bs-theme', 'dark');}
        if(tableallLoans){tableallLoans.setAttribute('data-bs-theme', 'dark');}
        if(tableallDevolution){tableallDevolution.setAttribute('data-bs-theme', 'dark');}
        if(tableallTransfer){tableallTransfer.setAttribute('data-bs-theme', 'dark');}
        if(tablemydevices){tablemydevices.setAttribute('data-bs-theme', 'dark');}
        if(tableAllDevices){tableAllDevices.setAttribute('data-bs-theme', 'dark')};
        if(tableAllAccessories){tableAllAccessories.setAttribute('data-bs-theme', 'dark');};
    } else {
        // Desativar o modo noturno
        document.body.classList.remove('dark-mode');
        localStorage.setItem('darkMode', 'false');
        if(tableElement){tableElement.setAttribute('data-bs-theme', 'light');}
        if(tableallTransactions){tableallTransactions.setAttribute('data-bs-theme', 'light');}
        if(tableallLoans){tableallLoans.setAttribute('data-bs-theme', 'light');}
        if(tableallDevolution){tableallDevolution.setAttribute('data-bs-theme', 'light');}
        if(tableallTransfer){tableallTransfer.setAttribute('data-bs-theme', 'light');}
        if(tablemydevices){tablemydevices.setAttribute('data-bs-theme', 'light');}
        if(tableAllDevices){tableAllDevices.setAttribute('data-bs-theme', 'light')};
        if(tableAllAccessories){tableAllAccessories.setAttribute('data-bs-theme', 'light');}
    }
}

// Verificar o estado do modo noturno no carregamento da página
checkDarkMode();

// Evento para alternar entre os modos de acordo com o estado atual
document.getElementById('toggleDarkMode').addEventListener('change', toggleDarkMode);
