const CHART = document.getElementById("lineChart");


var data = {
    labels: ['2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016'],
    datasets: [
        {label: "Yearly Average petroleum Price",
        fill: true ,
        lineTension: 0.,
        backgroundColor: "rgba(250, 142, 142, 0.1)",  /*fill color*/
        borderColor: "rgba(250, 142, 142, .4)", /*line color*/
        borderCapStyle: 'butt',
        borderDash: [],
        borderDashOffset: 0.0,
        borderJoinStyle: 'miter',
        pointBorderColor: "rgba(250, 142, 142, 1)", /*data point color*/
        pointBackgroundColor: "#fff",
        pointBorderWidth: 1,
        pointHoverRadius: 1,
        pointHoverBackgroundColor: "rgba(75,192,192,1)",
        pointHoverBorderColor: "rgba(220,220,220,1)",
        pointHoverBorderWidth: 1,
        pointRadius: 1,
        pointHitRadius: 10,
        data: [27.39, 23, 22.81, 27.69, 37.66, 50.04, 58.3, 64.2, 91.48, 53.48, 71.21, 87.04, 86.46, 91.17, 85.6, 41.85, 34.39],
        spanGaps: false,}
    	]
};

let lineChart = new Chart(CHART, {type: 'line', data})


