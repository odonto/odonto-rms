var chart = c3.generate({
    data: {
        columns: [
            ['data5', 0, 140, 120, 155, 135, 150, 0],
            ['data4', 140, 140, 140, 140, 140, 140, 140, 140],
            ['data1', 0, 0, 0, 0, 0, 0, 230],
        ],
        type: 'bar',
        types: {
            data4: 'line',
        },
        groups: [
            ['data1','data2']
        ]
    }
});
