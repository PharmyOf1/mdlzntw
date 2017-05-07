    $('#high_chart').pharmchart({
        chart: {
            type: 'column',
            backgroundColor: '#FFF'


        },
        title: {
            text: 'MDLZ Biscuit Network'
        },

        xAxis: {
            categories: [
                'January',
                'February',
                'March',
                'April',
                'May',
                'June',
                'July',
                'August',
                'September',
                'October',
                'November',
                'December' ]
        },
        yAxis: {
            min: 0,
            title: {
                text: 'US DOLLARS $ MM'
            }
        },
        tooltip: {
            headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
            pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
                '<td style="padding:0"><b>{point.y:.1f} mm</b></td></tr>',
            footerFormat: '</table>',
            shared: true,
            useHTML: true
        },
        plotOptions: {
            column: {
                pointPadding: 0.2,
                borderWidth: 0
            }
        },
        series: [{
            name: 'OREO',
            data: [49.9, 71.5, 106.4, 129.2, 144.0, 176.0, 135.6, 100, 100, 100, 100, 100]

        }, {
            name: 'CHIPS AHOY',
            data: [42.4, 33.2, 34.5, 39.7, 52.6, 75.5, 57.4]

        }]
    });


    $('#dashView1').pharmchart({
        chart: {
            type: 'area'

        },
        title: {
            text: 'CFR'
        },

        xAxis: {
            categories: [
                'January',
                'February',
                'March',
                'April',
                'May',
                'June',
                'July',
                'August',
                'September',
                'October',
                'November',
                'December' ]
        },
        yAxis: {
            min: 0,
            title: {
                text: 'US DOLLARS $ MM'
            }
        },
        tooltip: {
            headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
            pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
                '<td style="padding:0"><b>{point.y:.1f} mm</b></td></tr>',
            footerFormat: '</table>',
            shared: true,
            useHTML: true
        },
        plotOptions: {
            column: {
                pointPadding: 0.2,
                borderWidth: 0
            }
        },
        series: [{
            name: 'PY',
            data: [49.9, 71.5, 106.4, 129.2, 144.0, 176.0, 135.6, 100, 100, 100, 100, 100]

        }, {
            name: 'YTD',
            data: [42.4, 33.2, 34.5, 39.7, 52.6, 75.5, 57.4]

        }]
    });


            $('#dashView2').pharmchart({
        chart: {
            type: 'line'

        },
        title: {
            text: 'AC YTD'
        },

        xAxis: {
            categories: [
                'January',
                'February',
                'March',
                'April',
                'May',
                'June',
                'July',
                'August',
                'September',
                'October',
                'November',
                'December' ]
        },
        yAxis: {
            min: 0,
            title: {
                text: 'US DOLLARS $ MM'
            }
        },
        tooltip: {
            headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
            pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
                '<td style="padding:0"><b>{point.y:.1f} mm</b></td></tr>',
            footerFormat: '</table>',
            shared: true,
            useHTML: true
        },
        plotOptions: {
            column: {
                pointPadding: 0.2,
                borderWidth: 0
            }
        },
        series: [{
            name: 'AC Target',
            data: [49.9, 71.5, 106.4, 129.2, 144.0, 176.0, 135.6, 100, 100, 100, 100, 100]

        }, {
            name: 'AC YTD',
            data: [42.4, 33.2, 34.5, 39.7, 52.6, 75.5, 57.4]

        }]
    });

            $('#dashView3').pharmchart({
        chart: {
            type: 'line'

        },
        title: {
            text: 'AC YTD'
        },

        xAxis: {
            categories: [
                'January',
                'February',
                'March',
                'April',
                'May',
                'June',
                'July',
                'August',
                'September',
                'October',
                'November',
                'December' ]
        },
        yAxis: {
            min: 0,
            title: {
                text: 'US DOLLARS $ MM'
            }
        },
        tooltip: {
            headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
            pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
                '<td style="padding:0"><b>{point.y:.1f} mm</b></td></tr>',
            footerFormat: '</table>',
            shared: true,
            useHTML: true
        },
        plotOptions: {
            column: {
                pointPadding: 0.2,
                borderWidth: 0
            }
        },
        series: [{
            name: 'AC Target',
            data: [49.9, 71.5, 106.4, 129.2, 144.0, 176.0, 135.6, 100, 100, 100, 100, 100]

        }, {
            name: 'AC YTD',
            data: [42.4, 33.2, 34.5, 39.7, 52.6, 75.5, 57.4]

        }]
    });

    

