document.getElementById('btn').addEventListener('click', () => {
        $.ajax({
                type: "POST",
                url: "http://127.0.0.1:5000/result",
                data: JSON.stringify({ "token": token, "cid" : cid}),
                contentType: "application/json",
                success: function (result) {
                        console.log(result);
                },
                error: function (result, status) {
                        console.log(result);
                }
        });
});
