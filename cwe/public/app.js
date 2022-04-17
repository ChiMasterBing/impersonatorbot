document.getElementById('pp').addEventListener('submit', (token) => {
        token.preventDefault();
        var tok = document.getElementById('pp').elements[0].value;
        console.log(tok);
        var xhr = new XMLHttpRequest();
        xhr.open("POST", 'http://127.0.0.1:5000/result', true);
        console.log("HERE");
        xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");

        console.log("HERE");
        xhr.onreadystatechange = function() { // Call a function when the state changes.
            if (this.readyState === XMLHttpRequest.DONE && this.status === 200) {
                // Request finished. Do processing here.
            }
        }
        var cid;
        chrome.tabs.query({active: true, currentWindow: true}, tabs => {
            cid= tabs[0].url.split("/").pop();
        console.log(cid);
                //cid = "844600766575542362";
         payload = "cid="+cid+"&token="+tok;
                console.log(payload);
        xhr.send(payload);
            // use `url` here inside the callback because it's asynchronous!
        });
});
