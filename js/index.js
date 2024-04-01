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
