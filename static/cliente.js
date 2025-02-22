const url = window.location.href;
const divide_url = url.split('/').filter(segment => segment !== ''); // Remove elementos vazios
const id = divide_url[divide_url.length - 1]; // Captura o último segmento da URL

fetch(`/pacientes/${id}`)
.then(response => {
    if (!response.ok) {
        throw new Error(`Erro ao buscar cliente: ${response.status}`);
    }
    return response.json();
})
.then(dadosCliente => {
Object.keys(dadosCliente).forEach(key => {
    const element = document.getElementById(key);
    if (element) {
        if (element.tagName === 'INPUT' || element.tagName === 'TEXTAREA') {
            element.value = dadosCliente[key] || '';
        } else {
            element.innerText = dadosCliente[key] || '';
        }
    }
});
})

document.getElementById("excluir").addEventListener("click", function(event) {
    event.preventDefault();

    const confirmacao = confirm("você deseja excluir esse paciente?");
    if (!confirmacao) {
        return;
    }

    const url = window.location.href;
    const url_separada = url.split("/");
    const id = url_separada[url_separada.length - 1];

    fetch(`/pacientes/${id}`, {
        method: "DELETE",
        headers: {
            'Content-Type': 'application/json'
        },
        credentials: "include"  
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message || "Excluído com sucesso!");
        window.location.href = "/cadastrados";
    })
    .catch(error => {
        alert("Ocorreu um erro ao tentar excluir.");
    });
});