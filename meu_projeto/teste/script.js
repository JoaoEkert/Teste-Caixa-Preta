function runTests() {
    const resultadosDiv = document.getElementById('resultados');
    resultadosDiv.innerHTML = 'Executando testes...';

    fetch('http://localhost:5000/run_all_test.py')
        .then(response => response.json())
        .then(data => {
            resultadosDiv.innerHTML = '';
            data.results.forEach(result => {
                const p = document.createElement('p');
                p.textContent = result;
                resultadosDiv.appendChild(p);
            });
        })
        .catch(error => {
            resultadosDiv.textContent = 'Erro ao executar os testes';
            console.error('Erro:', error);
        });
}
