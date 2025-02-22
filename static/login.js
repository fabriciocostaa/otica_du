document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("login_form").addEventListener("submit", function(event) {
        event.preventDefault();

        const login = document.getElementById("login");
        const senha = document.getElementById("senha");

        const json = {
            login: login.value,
            senha: senha.value
        };

        const responseMessage = document.getElementById("response-message");

        fetch('/login_usuario', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(json) 
        })

        .then(response => {
            if (response.ok){
            responseMessage.innerHTML= `<div class="alert alert-success">Login feito com sucesso</div>`;
            return response.json()
            } else {
            return response.json().then(err => {
                throw new Error(err.message || `Erro HTTP: ${response.status}`);
            })
            }
        })
        .then(data =>{
            setTimeout(() =>{
            window.location.href = "/index";
            }, 1000);
        })
        
        .catch(error => {
            responseMessage.innerHTML = `<div class="alert alert-danger">${error}</div>`;
        });
    });
});