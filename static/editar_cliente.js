// carregar informações
document.addEventListener("DOMContentLoaded", function() {
    const url = document.referrer;
    const divide_url = url.split('/');
    const id = divide_url[divide_url.length - 1];

    fetch(`/pacientes/${id}`)
    .then(response => response.json())
    .then(dadosCliente => {
        Object.keys(dadosCliente).forEach(key => {
            const element = document.getElementById(key);
            if (element) {
                element.value = dadosCliente[key] || '';
            }
        });
    })
    .catch(error => console.error('Erro:', error));

    // editar cliente
    document.getElementById("formulario").addEventListener("submit", function(event) {
        event.preventDefault();

        const form = document.getElementById("formulario");
        const formData = new FormData(form);

        const json = {};
        formData.forEach((value, key) => {
            json[key] = value;
        });

        console.log("Dados enviados:", json);

        fetch(`/pacientes/${id}`, {
            method: "PUT",
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(json)
        })
        .then(response => {
            console.log("Status da resposta:", response.status);
            if (response.ok) {
                alert('Atualizado com sucesso');
                window.location.href = "/index";
            } else {
                return response.json().then(data => {
                    console.error("Erro do servidor:", data);
                    alert(data.message || "Erro ao atualizar.");
                });
            }
        })
        .catch(error => {
            console.error("Erro na requisição:", error);
            alert("Ocorreu um erro inesperado.");
        });
    });
});