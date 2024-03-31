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
    });
}
