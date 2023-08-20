$(document).ready(function(){
    $("#symbol-form").submit(function(e){
        e.preventDefault();
        var symbol = $("#symbol").val();
        var currency = $("#currency").val();
        $.ajax({
            url: '/fetch_data',
            type: 'post',
            contentType: 'application/json',
            data: JSON.stringify({ 'symbol': symbol, 'currency': currency }),
            success: function(data) {
                $("#data").html(JSON.stringify(data));
                var ctx = document.getElementById('graph').getContext('2d');
                var formattedData = Object.entries(data).map(([key, value]) => ({
                    t: new Date(key),
                    y: Number(value['4a. close (USD)'])
                }));
                var lineChart = new Chart(ctx, {
                    type: 'line',
                    data: {
                        datasets: [{
                            label: 'Close Price',
                            data: formattedData,
                            borderColor: 'rgb(75, 192, 192)',
                            tension: 0.1
                        }]
                    },
                    options: {
                        scales: {
                            y: {
                                beginAtZero: false,
                                grace: '5%',
                                display: false,
                                ticks: {
                                    display: false
                                }
                            }
                        }
                    }
                });

                var candlestickCtx = document.getElementById('candlestick-chart').getContext('2d');
                var candlestickChart = new Chart(candlestickCtx, {
                    type: 'candlestick',
                    data: {
                        datasets: [{
                            label: 'Candlestick',
                            data: Object.values(data).map(d => ({
                                t: new Date(d.date),
                                o: d['1a. open (USD)'],
                                h: d['2a. high (USD)'],
                                l: d['3a. low (USD)'],
                                c: d['4a. close (USD)']
                            }))
                        }]
                    }
                });
            },
            error: function(error) {
                $("#data").html(JSON.stringify(error));
            }
        });
    });
});
