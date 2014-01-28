<head>
    <title>
        Number of {{word}}´s on {{address}}
    </title>
    <LINK href="/static/super5.css" rel="stylesheet" type="text/css">
</head>
<body>
    <div id = 'output' class = 'centered'>
        There are <b>{{number}}</b> <b>{{word}}</b>'s on <b>{{address}}</b>
    </div>
    

    <div id = 'input'>
        <form action = '/super5' method = 'post' class = 'centered'>
            <label>Address: <input type = 'text' name = 'address'> </label>
            <label>Word: <input type = 'text' name = 'word'> </label>
            <input type = 'submit' value = 'COUNT!'>
        </form>
    </div>
</body>
