<!DOCTYPE html>
<html>
  <head>
    <title>
      {{number}} {{word}}´s on {{address}}
    </title>
    <LINK href="/static/super5.css" rel="stylesheet" type="text/css">
  </head>

  <body>
    <div id = 'content'>
      <div id = 'header' class = 'centered'>
        <h1>
          super5
        </h1>
      </div>

      <div id = 'output' class = 'centered'>
        <p>
          There are <b class='num'>{{number}}</b> <b>{{word}}</b>'s on
        </p>
        <p>
          <b>{{address}}</b>
        </p>
      </div>

      <div id = 'input' class = 'centered'>
        <form action = '/super5' method = 'post'>
          <div class="block">
            <label>
              word
            </label>
            <input type = 'text' name = 'word' placeholder = 'super'>
          </div>
          <div class="block">
            <label>
              address
            </label>
            <input type = 'text' name = 'address' placeholder = 'http://aftonbladet.se'>
            <div>
              <input id='submit' type = 'submit' value = 'count'>
            </div>
          </div>
        </form>
      </div>
    </div>
  </body>
</html>
