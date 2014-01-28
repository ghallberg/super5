<head>
    <title>
        Number of {{word}}´s on {{address}}
    </title>
</head>
<body>
    There are {{number}} {{word}}'s on {{address}}
    

    <form action = '/super5' method = 'post'>
        <label>Address: <input type = 'text' name = 'address'> </label>
        <label>Word: <input type = 'text' name = 'word'> </label>
        <input type = 'submit' value = 'COUNT!'>
    </form>
</body>
