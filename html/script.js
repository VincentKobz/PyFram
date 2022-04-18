function request() {
    var name = document.getElementById("input");
    const data = {
        expression: name.value,
    };
        
    const options = {
        method: 'POST',
        mode: 'cors',
        headers: {
        'Content-Type': 'application/json',
        },
        body: data
        };
    var request = new Request('http://127.0.0.1:8000/frame/');
    fetch(request, { mode: 'cors', method: 'POST', body: JSON.stringify(data) })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            document.getElementById("output").innerHTML = data.answer;
        });
}

function changeText(json) {
    var text = document.getElementById("result");
    text.innerHTML = json;
}