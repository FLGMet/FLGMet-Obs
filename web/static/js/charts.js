let ctx = document.getElementById("weatherChart").getContext("2d");

let weatherChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: [],
        datasets: [{
            label: 'Température (°C)',
            borderColor: 'red',
            data: []
        }]
    },
    options: {
        responsive: true,
        scales: {
            x: { title: { display: true, text: 'Temps' } },
            y: { title: { display: true, text: 'Valeur' } }
        }
    }
});
