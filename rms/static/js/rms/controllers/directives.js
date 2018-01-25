directives.directive('lineChart', function($http){
    return function(scope, element, attrs){
        var el = element
        if(attrs.lineChart == 'clinic'){
            var columns = [
                    ['Appointments Booked',  0,  70, 45, 59, 48, 64, 0,   0],
                    ['Average Appointments', 52, 52, 52, 52, 52, 52, 52, 52],
                    ['Referrals Pending',    0,   0,   0,    0,   0,   0,  23,  0],
                ]
        }else{
            var columns = [
                    ['Appointments Booked', 0,   140, 120, 155, 135, 150, 0,   0],
                    ['Average Appointments', 140, 140, 140, 140, 140, 140, 140, 140],
                    ['Referrals Pending', 0,   0,   0,    0,   0,   0,  230,  0],
                ]
        }

        var chart = c3.generate({
            bindto: el[0],
            data: {
                columns: columns,
                type: 'bar',
                types: {
                    'Average Appointments': 'line',
                },
            },
            tooltip: {
                show: false
            },



        });

        // $http.get('/dashboards/widgets/line-chart/' + attrs.lineChart).then(
        //     function(response){

        //         var ticks = response.data[0]
        //         var tick_values = [
        //             moment(ticks[1])._d,
        //             moment(ticks[ticks.length/2])._d,
        //             moment(ticks[ticks.length-1])._d
        //         ]

        //         console.log(tick_values)

        //         c3.generate({
        //             bindto: el[0],
        //             data: {
        //                 x: 'x',
        //                 columns: response.data,
        //             },
        //             color: {
        //                 pattern: [
        //                     '#f76c51', // Red
        //                     '#9cc96b', // Green
        //                     '#5fa2dd' // Blue
        //                 ]
        //             },

        //             axis: {
        //                 x: {
        //                     type: 'timeseries',
        //                     tick: {
        //                         fit: true,
        //                         format: '%Y-%m',
        //                         values: tick_values
        //                     }
        //                 }
        //             }
        //         });
        //     }
        // )
    }
})


directives.directive("fileread", [function () {
    return {
        scope: {
            fileread: "="
        },
        link: function (scope, element, attributes) {
            element.bind("change", function (changeEvent) {
                var reader = new FileReader();
                reader.onload = function (loadEvent) {
                    scope.$apply(function () {
                        scope.fileread = loadEvent.target.result;
                    });
                }
                reader.readAsDataURL(changeEvent.target.files[0]);
            });
        }
    }
}]);
