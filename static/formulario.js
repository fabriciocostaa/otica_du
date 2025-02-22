document.getElementById("formulario").addEventListener("submit", function(event) {
    event.preventDefault();

    const form = document.getElementById("formulario");
    const formData = new FormData(form);

    const json = {};
    formData.forEach((value, key) => {
        json[key] = value;
    });

    fetch("/registrar", {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(json)
    })
    .then(response => {
        if (response.ok) {
            window.location.href="/index";
            alert('Cadastro feito com sucesso');
        } else 
            alert("deu ruim");
        })
    .catch(error => {
        alert(`${error}`);
    });
});