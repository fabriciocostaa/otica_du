let clientesData = []; 

// Função para renderizar a lista de clientes
function renderizarClientes(clientes) {
    const tbody = document.getElementById('dados-clientes');
    const semDados = document.getElementById('sem-dados');

    tbody.innerHTML = ''; // Limpar a tabela antes de adicionar os dados

    if (clientes.length > 0) {
        clientes.forEach(cliente => {
            const tr = document.createElement('tr');
            tr.innerHTML = `
                <td><a href="/clientes/${cliente.id_cliente}">${cliente.id_cliente}</a></td>
                <td>${cliente.nome}</td>
                <td>${cliente.data_nasc ?? ''}</td>
                <td>${cliente.sexo ?? ''}</td>
                <td>${cliente.telefone_res ?? ''}</td>
                <td>${cliente.profissao ?? ''}</td>
                <td>${cliente.idade ?? ''}</td>
            `;
            tbody.appendChild(tr);
        });
        semDados.style.display = 'none';
    } else {
        semDados.style.display = 'block';
    }
}

// Função para aplicar filtros
function aplicarFiltros() {
    const idClienteFiltro = document.getElementById('pesquisa-id_cliente').value;
    const nomeFiltro = document.getElementById('pesquisa-nome').value.toLowerCase();
    const dataNascFiltro = document.getElementById('pesquisa-data_nasc').value;
    const sexoFiltro = document.getElementById('pesquisa-sexo').value.toUpperCase(); 
    const profissaoFiltro = document.getElementById('pesquisa-profissao').value.toLowerCase();
    const idadeFiltro = document.getElementById('pesquisa-idade').value;

    // Filtra os dados
    const clientesFiltrados = clientesData.filter(cliente => {
        const idClienteMatch = idClienteFiltro === '' || cliente.id_cliente.toString().includes(idClienteFiltro);
        const nomeMatch = cliente.nome.toLowerCase().includes(nomeFiltro);
        const dataNascMatch = dataNascFiltro === '' || (cliente.data_nasc ?? '').toString().includes(dataNascFiltro);
        const sexoMatch = sexoFiltro === '' || (cliente.sexo ?? '').toUpperCase().includes(sexoFiltro); 
        const profissaoMatch = profissaoFiltro === '' || (cliente.profissao ?? '').toLowerCase().includes(profissaoFiltro); 
        const idadeMatch = idadeFiltro === '' || cliente.idade.toString().includes(idadeFiltro); 

        return idClienteMatch && nomeMatch && dataNascMatch && sexoMatch && profissaoMatch && idadeMatch;
    });

    // Atualiza a tabela com os clientes filtrados
    renderizarClientes(clientesFiltrados);
}

// Adiciona os eventos para os filtros
document.getElementById('pesquisa-id_cliente').addEventListener('input', aplicarFiltros);
document.getElementById('pesquisa-nome').addEventListener('input', aplicarFiltros);
document.getElementById('pesquisa-data_nasc').addEventListener('input', aplicarFiltros);
document.getElementById('pesquisa-sexo').addEventListener('input', aplicarFiltros);
document.getElementById('pesquisa-profissao').addEventListener('input', aplicarFiltros);
document.getElementById('pesquisa-idade').addEventListener('input', aplicarFiltros);

// Função para buscar os dados dos clientes
fetch('/registrar')
    .then(response => response.json())
    .then(data => {
        if (data.message && data.message.length > 0) { 
            clientesData = data.message; // Armazena os dados dos clientes
            renderizarClientes(clientesData); 
        } else {
            document.getElementById('sem-dados').style.display = 'block';
        }
    })
    .catch(error => {
        console.error('Erro ao carregar os dados:', error);
        document.getElementById('sem-dados').style.display = 'block';
    });

document.getElementById("logout").addEventListener("click", function(event){
    event.preventDefault();

    fetch('logout_usuario', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        credentials: "include"  
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message || "Você foi deslogado com sucesso");
        window.location.href = "/";
    })
    .catch(error => {
        alert("Ocorreu um erro ao tentar deslogar.");
    });
});