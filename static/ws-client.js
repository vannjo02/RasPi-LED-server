$(document).ready(function(){

        var WEBSOCKET_ROUTE = "/ws";

        if(window.location.protocol == "http:"){
            //localhost
            var ws = new WebSocket("ws://" + window.location.host + WEBSOCKET_ROUTE);
            }
        else if(window.location.protocol == "https:"){
            //Dataplicity
            var ws = new WebSocket("wss://" + window.location.host + WEBSOCKET_ROUTE);
            }

        ws.onopen = function(evt) {
            $("#ws-status").html("Connected");
            };

        ws.onmessage = function(evt) {
		var msg = evt.data;
		console.log("received message: "+ evt.data )
		if (msg == "on_g"){
			$("#green_on").attr('class', "btn btn-block btn-lg btn-default");
			$("#green_off").attr('class', "btn btn-block btn-lg btn-primary");
		}
		if (msg == "off_g"){
			$("#green_on").attr('class', "btn btn-block btn-lg btn-primary");
			$("#green_off").attr('class', "btn btn-block btn-lg btn-default");
		}
		if (msg == "on_r"){
			$("#red_on").attr('class', "btn btn-block btn-lg btn-default");
			$("#red_off").attr('class', "btn btn-block btn-lg btn-primary");
		}
		if (msg == "off_r"){
			$("#red_on").attr('class', "btn btn-block btn-lg btn-primary");
			$("#red_off").attr('class', "btn btn-block btn-lg btn-default");
		}
            };

        ws.onclose = function(evt) {
            $("#ws-status").html("Disconnected");
            };

        $("#green_on").click(function(){
            ws.send("on_g");
            });

        $("#green_off").click(function(){
            ws.send("off_g");
            });

        $("#red_on").click(function(){
            ws.send("on_r");
            });

        $("#red_off").click(function(){
            ws.send("off_r");
            });

      });
