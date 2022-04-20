function request() {
    var name = document.getElementById("input");
    const data = {
        expression: name.value,
    };
        
    var request = new Request('http://127.0.0.1:8000/frame/');
    fetch(request, { mode: 'cors', method: 'POST', body: JSON.stringify(data) })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            document.getElementById("result").innerHTML = data.result;
        });
}

function help() {
    window.open("https://www.google.com")
}