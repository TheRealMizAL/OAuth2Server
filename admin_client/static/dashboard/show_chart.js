function showChart() {
  const ctx = document.getElementById('myChart');

  new Chart(ctx, {
    type: 'line',
    data: {
      labels: [...Array(7).keys()].map(x => {
        var d = new Date();
        d.setDate(d.getDate() + x - 7);
        var day = d.getDate();
        var month = d.getMonth();
        return `${day < 10 ? '0' + day : day}.${month < 10 ? '0' + month : month}`;
      }),
      datasets: [{
        label: 'Количество инцедентов',
        data: [12, 19, 3, 5, 2, 3, 5, 7],
        borderWidth: 1
      }]
    },
    options: {
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  });
}