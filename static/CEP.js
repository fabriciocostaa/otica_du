function preenche_cep() {
    let cep = document.getElementById("CEP").value; 
    if (cep != "") {
        // Chama a API ViaCEP
        fetch(`https://viacep.com.br/ws/${cep}/json/`)
            .then(response => response.json())  // Converte a resposta para JSON
            .then(data => {
                // Verifica se o CEP foi encontrado
                if (!data.erro) {
                    // Preenche os campos com os dados da API
                    document.getElementById("endereco").value = data.logradouro;
                    document.getElementById("bairro").value = data.bairro;
                    document.getElementById("cidade").value = data.localidade;
                } else {
                    alert("CEP não encontrado");
                }
            })
            .catch(error => {
                console.error("Erro:", error);
                alert("Erro ao buscar o CEP");
            });
    }
}

// Adiciona o evento para chamar a função quando o campo de CEP perder o foco
document.getElementById("CEP").addEventListener("blur", preenche_cep);