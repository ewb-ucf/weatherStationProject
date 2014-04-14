/* Links to JSON Data */
tempData = 'http://www.highcharts.com/samples/data/jsonp.php?filename=aapl-c.json&callback=?';

rangeSel = {
                selected: 0,
                enabled: false,
                inputEnabled: false,
            };

function renderWindSpeedGraph(JSON_link) {

    $.getJSON(JSON_link, function(data) {
        // Create the chart
        window.chart = new Highcharts.StockChart({
            chart: {
                renderTo: 'wind-speed-graph'
            },
            
            navigator: {
                enabled: true
            },

            title: {
                text: 'Windspeed Over Time'
            },
            
            legend: {
                layout: 'vertical',
                backgroundColor: '#FFFFFF',
                floating: true,
                align: 'left',
                verticalAlign: 'top',
                x: 90,
                y: 45,
                labelFormatter: function() {
                    return this.name +' (click to hide)';
                }
             },
            
            rangeSelector: {
                selected: 0,
                enabled: true,
                inputDateFormat: '%Y-%m',
                inputEnabled: false,
                buttons: [{
                    type: 'all',
                    text: 'Daily',
                }, {
                    type: 'month',
                    text: 'Monthly'
                }, {
                    type: 'year',
                    text: 'Yearly',
                }],
                buttonTheme: { // styles for the buttons
                width: null             
                }
            },

            series: [{
                name: 'High',
                data: data,
                color: 'red',
                tooltip: {
                    valueDecimals: 2
                }}, {
                name: 'Average',
                data: data,
                color: 'green',
                tooltip: {
                    valueDecimals: 2
                }}, {
                name: 'Low',
                data: data,
                color: 'blue',
                tooltip: {
                    valueDecimals: 2
                }}]
        });
    });         
}

function renderTemperatureGraph(JSON_link) {

    $.getJSON(JSON_link, function(data) {
        // Create the chart
        window.chart = new Highcharts.StockChart({
            chart: {
                renderTo: 'temperature-graph'
            },

            rangeSelector: rangeSel,

            title: {
                text: 'Temperature Over Time'
            },
            
            navigator: {
                enabled: true
            },

            series: [{
                name: 'Temperature',
                id: 'temp_x_axis',
                xAxis: 0,
                data: data,
                tooltip: {
                    valueDecimals: 2
                }}],
            series: [{
                name: 'High',
                data: data,
                color: 'red',
                tooltip: {
                    valueDecimals: 2
                }}, {
                name: 'Average',
                data: data,
                color: 'green',
                tooltip: {
                    valueDecimals: 2
                }}, {
                name: 'Low',
                data: data,
                color: 'blue',
                tooltip: {
                    valueDecimals: 2
                }}]
        });
    });         
}

function renderDensityGraph(JSON_link) {

    $.getJSON(JSON_link, function(data) {
        // Create the chart
        window.chart = new Highcharts.StockChart({
            chart: {
                renderTo: 'density'
            },

            rangeSelector: rangeSel,

            title: {
                text: 'Density Over Time'
            },

            series: [{
                name: 'Density',
                data: data,
                tooltip: {
                    valueDecimals: 2
                }}],
            series: [{
                name: 'High',
                data: data,
                color: 'red',
                tooltip: {
                    valueDecimals: 2
                }}, {
                name: 'Average',
                data: data,
                color: 'green',
                tooltip: {
                    valueDecimals: 2
                }}, {
                name: 'Low',
                data: data,
                color: 'blue',
                tooltip: {
                    valueDecimals: 2
                }}]
        });
    });         
}


/*
renderWindSpeedGraph(tempData);
renderTemperatureGraph(tempData);
renderDensityGraph(tempData);
*/

