$(function() {

    $.getJSON('http://www.highcharts.com/samples/data/jsonp.php?filename=aapl-c.json&callback=?', function(data) {
        // Create the chart
        window.chart = new Highcharts.StockChart({
            chart: {
                renderTo: 'wind-speed-graph'
            },

            rangeSelector: {
                selected: 1,
                buttons: [{
                    type: 'day',
                    count: 1,
                    text: '1d'
                }, {
                    type: 'month',
                    count: 1,
                    text: '1m'
                }, {
                    type: 'year',
                    count: 1,
                    text: '1y'
                }],
                inputDateFormat: '%Y.%m.%d %H:%M',
                inputBoxWidth: 150,
            },

            title: {
                text: 'Wind Speed Over Time'
            },

            series: [{
                name: 'Wind Speed',
                data: data,
                tooltip: {
                    valueDecimals: 2
                }}]

        }, function(chart) {

            // apply the date pickers
            setTimeout(function() {
                $('input.highcharts-range-selector', $('#' + chart.options.chart.renderTo)).datepicker()
            }, 0)
        });
    });

    $.getJSON('http://www.highcharts.com/samples/data/jsonp.php?filename=aapl-c.json&callback=?', function(data) {
        // Create the chart
        window.chart = new Highcharts.StockChart({
            chart: {
                renderTo: 'temperature-graph'
            },

            rangeSelector: {
                selected: 1,
                buttons: [{
                    type: 'day',
                    count: 1,
                    text: '1d'
                }, {
                    type: 'month',
                    count: 1,
                    text: '1m'
                }, {
                    type: 'year',
                    count: 1,
                    text: '1y'
                }],
                inputDateFormat: '%Y.%m.%d %H:%M',
                inputBoxWidth: 150,
            },

            title: {
                text: 'Temperature Over Time'
            },

            series: [{
                name: 'Temperature',
                data: data,
                tooltip: {
                    valueDecimals: 2
                }}]

        }, function(chart) {

            // apply the date pickers
            setTimeout(function() {
                $('input.highcharts-range-selector', $('#' + chart.options.chart.renderTo)).datepicker()
            }, 0)
        });
    });

    $.getJSON('http://www.highcharts.com/samples/data/jsonp.php?filename=aapl-c.json&callback=?', function(data) {
        // Create the chart
        window.chart = new Highcharts.StockChart({
            chart: {
                renderTo: 'density-graph'
            },

            rangeSelector: {
                selected: 1,
                buttons: [{
                    type: 'day',
                    count: 1,
                    text: '1d'
                }, {
                    type: 'month',
                    count: 1,
                    text: '1m'
                }, {
                    type: 'year',
                    count: 1,
                    text: '1y'
                }],
                inputDateFormat: '%Y.%m.%d %H:%M',
                inputBoxWidth: 150,
            },

            title: {
                text: 'Density Over Time'
            },

            series: [{
                name: 'Density',
                data: data,
                tooltip: {
                    valueDecimals: 2
                }}]

        }, function(chart) {

            // apply the date pickers
            setTimeout(function() {
                $('input.highcharts-range-selector', $('#' + chart.options.chart.renderTo)).datepicker()
            }, 0)
        });
    });



    // Set the datepicker's date format
    $.datepicker.setDefaults({
        dateFormat: 'yy-mm-dd',
        onSelect: function(dateText) {
            this.onchange();
            this.onblur();
        }
    });

});

