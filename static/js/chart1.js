async function fetchChartData() {
  const response = await fetch('/api_plot');
  const chartData = await response.json();

  // Create the chart with the fetched data
  var ctx = document.getElementById('lineChart').getContext('2d');
  var myChart = new Chart(ctx, {
      type: 'line',
      data: {
          labels: chartData.labels,
          datasets: [{
              label: 'Correct Answers',
              data: chartData.values,
              backgroundColor: 'rgba(85,85,85, 1)',
              borderColor: 'rgb(41, 155, 99)',
              borderWidth: 1
          }]
      },
      options: {
          responsive: true
      }
  });
}

// Fetch and create the chart when the page loads
window.onload = fetchChartData;
  




// var ctx = document.getElementById('lineChart').getContext('2d');
// var myChart = new Chart(ctx, {
//     type: 'line',
//     data: {
//         labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
//         datasets: [{
//             label: 'Earnings in $',
//             data: [2050, 1900, 2100, 2800, 1800, 2000, 2500, 2600, 2450, 1950, 2300, 2900],
//             backgroundColor: [
//                 'rgba(85,85,85, 1)'

//             ],
//             borderColor: 'rgb(41, 155, 99)',

//             borderWidth: 1
//         }]
//     },
//     options: {
//         responsive: true
//     }
// });