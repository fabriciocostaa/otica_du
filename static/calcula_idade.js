function calcularIdade() {
      
    const dataHoje = new Date(document.getElementById('data').value);
    const dataNascimento = new Date(document.getElementById('data_nasc').value);

    if (dataHoje && dataNascimento) {
      let idade = dataHoje.getFullYear() - dataNascimento.getFullYear();
      const mes = dataHoje.getMonth() - dataNascimento.getMonth();
      
      // Ajustando caso o mês atual ainda não tenha passado
      if (mes < 0 || (mes === 0 && dataHoje.getDate() < dataNascimento.getDate())) {
        idade--;
      }

      document.getElementById('idade').value = idade;
    }
  }

  document.getElementById('data').addEventListener('input', calcularIdade);
  document.getElementById('data_nasc').addEventListener('input', calcularIdade);