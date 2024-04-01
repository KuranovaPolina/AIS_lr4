async function startPage()
{
    console.log("startPage");
    await fetch('/stats', {method: 'POST'}).then(response => response.json()).then(async data => {
        console.log(data);

        document.getElementById("CPUTemp").value = data["CPUTemp"];
        document.getElementById("GPUTemp").value = data["GPUTemp"];
        document.getElementById("CPULoad").value = data["CPULoad"];
        document.getElementById("GPULoad").value = data["GPULoad"];
        document.getElementById("RAMLoad").value = data["RAMLoad"];

        document.getElementById("CPUTemp_critical").value = data["CPUTemp_critical"];
        document.getElementById("GPUTemp_critical").value = data["GPUTemp_critical"];
        document.getElementById("CPULoad_critical").value = data["CPULoad_critical"];
        document.getElementById("GPULoad_critical").value = data["GPULoad_critical"];
        document.getElementById("RAMLoad_critical").value = data["RAMLoad_critical"];

        var dataChart = {
            labels: data["datetimes"],
            datasets: [
                {
                    title: "CPUTemp",
                    data: data["CPUTemps"],
                    backgroundColor: ['#a00'],
                    borderWidth: 0.5,
                    borderColor: '#ddd'
                },
                {
                    title: "GPUTemp",
                    data: data["GPUTemps"],
                    backgroundColor: ['#a0a'],
                    borderWidth: 0.5,
                    borderColor: '#ddd'
                },
                {
                    title: "CPULoad",
                    data: data["CPULoads"],
                    backgroundColor: ['#aa0'],
                    borderWidth: 0.5,
                    borderColor: '#ddd'
                },
                {
                    title: "GPULoad",
                    data: data["GPULoads"],
                    backgroundColor: ['#a55'],
                    borderWidth: 0.5,
                    borderColor: '#ddd'
                },
                {
                    title: "RAMLoad",
                    data: data["RAMLoads"],
                    backgroundColor: ['#fa0'],
                    borderWidth: 0.5,
                    borderColor: '#ddd'
                }]
        };

        ctx = document.getElementById('graph');

        var myChart = new Chart(ctx, {
            type: 'line',
            data: dataChart,
            options: {
                legend: {
                    display: true,
                    position: 'bottom',
                    labels: {
                        boxWidth: 15,
                        // fontColor: '#111',
                        padding: 7
                    }
                }
            }
        });
    });
}

async function updateCritical()
{
    console.log("updateCritical");

    let CPUTemp = parseFloat(document.getElementById("CPUTemp_critical").value).toFixed(2); 
    let GPUTemp = parseFloat(document.getElementById("GPUTemp_critical").value).toFixed(2); 
    let CPULoad = parseFloat(document.getElementById("CPULoad_critical").value).toFixed(2); 
    let GPULoad = parseFloat(document.getElementById("GPULoad_critical").value).toFixed(2); 
    let RAMLoad = parseFloat(document.getElementById("RAMLoad_critical").value).toFixed(2); 

    await fetch('/updateCritical', {method: 'POST',  
        headers: {
            Accept: 'application/json',
            'Content-Type': 'application/json',
        }, 
        body: JSON.stringify({
            CPUTemp: (+CPUTemp), 
            GPUTemp: (+GPUTemp), 
            CPULoad: (+CPULoad), 
            GPULoad: (+GPULoad), 
            RAMLoad: (+RAMLoad)
        })});
}

async function updateGraph()
{
    console.log("updateGraph");

    freq = 0;

    if (document.getElementById('minute').checked) {
        freq = 0;
    }
    else if (document.getElementById('hour').checked) {
        freq = 1;
    }
    else if (document.getElementById('day').checked) {
        freq = 2;
    }
    else if (document.getElementById('week').checked) {
        freq = 3;
    }

    await fetch('/updateGraph', {method: 'POST',  
        headers: {
            Accept: 'application/json',
            'Content-Type': 'application/json',
        }, 
        body: JSON.stringify({
            freq: freq
        })}).then(response => response.json()).then(async data => {
            console.log(data);

            var dataChart = {
                labels: data["datetimes"],
                datasets: [
                    {
                        title: "CPUTemp",
                        data: data["CPUTemps"],
                        backgroundColor: ['#a00'],
                        borderWidth: 0.5,
                        borderColor: '#ddd'
                    },
                    {
                        title: "GPUTemp",
                        data: data["GPUTemps"],
                        backgroundColor: ['#a0a'],
                        borderWidth: 0.5,
                        borderColor: '#ddd'
                    },
                    {
                        title: "CPULoad",
                        data: data["CPULoads"],
                        backgroundColor: ['#aa0'],
                        borderWidth: 0.5,
                        borderColor: '#ddd'
                    },
                    {
                        title: "GPULoad",
                        data: data["GPULoads"],
                        backgroundColor: ['#a55'],
                        borderWidth: 0.5,
                        borderColor: '#ddd'
                    },
                    {
                        title: "RAMLoad",
                        data: data["RAMLoads"],
                        backgroundColor: ['#fa0'],
                        borderWidth: 0.5,
                        borderColor: '#ddd'
                    }]
            };

            document.getElementById('canvas').innerHTML = "";

            var ctx = document.createElement('canvas');
            ctx.setAttribute("id", "graph");

            document.getElementById('canvas').appendChild(ctx);

            var myChart = new Chart(ctx, {
                type: 'line',
                data: dataChart,
                options: {
                    legend: {
                        display: true,
                        position: 'bottom',
                        labels: {
                            boxWidth: 15,
                            // fontColor: '#111',
                            padding: 7
                        }
                    }
                }
            });
    });
}