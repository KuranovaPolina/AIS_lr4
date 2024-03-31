async function startPage()
{
  console.log("data");
    await fetch('/stats', {method: 'POST'}).then(response => response.json()).then(async data => {
        console.log(data);
    });
}
