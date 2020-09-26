let itemsArray = {
    0:{
        0:{},
        1:{},
        2:{},
    },
    1:{
        0:{},
        1:{},
        2:{},
    },
    2:{
        0:{},
        1:{},
        2:{},
    },
};
let eachElementObj = {
    fill: false,
    player: null,
    count: null,
};
for (var i = 0; i < 3; i++) {
    for (var j = 0; j < 3; j++) {
        itemsArray[i][j] = eachElementObj;
    }
}

let mainObject = {
    starter: null,
    userPlayer: null,
    computerPlayer: null,
    this_turn_player: null,
    turn: null,
    items: itemsArray,
    result: {
        user: false,
        computer: false,
        row: false,
    },
};


$(document).ready(function () {

    const doozSocket = new WebSocket(
        'wss://'
        + window.location.host
        + '/wss/dooz/'
    );

    $(".start_button").click(function () {
        mainObject.starter = getRadioValue();
        mainObject.userPlayer = getRadioValue();
        if (mainObject.userPlayer === "green") {
            mainObject.computerPlayer = "red";
        } else if (mainObject.userPlayer === "red") {
            mainObject.computerPlayer = "green";
        }
        mainObject.turn = 1;
        mainObject.this_turn_player = 'green';
        if (doozSocket.readyState === WebSocket.OPEN){
            doozSocket.send(JSON.stringify({
                message: mainObject,
            }));
        }
        $(".start_button").css("display","none");
        $(".green-container").css("display", "none");
        $(".red-container").css("display", "none");
        $(".restart_button").css("display", "block");
        $(".start").css("width", "100%");

        $(".restart_button").click(function () {
            window.location.reload();
        })
    });

    doozSocket.onmessage = function (e) {
        let data = JSON.parse(e.data).message;
        console.log(data);
        let game = continue_game(data);
        if (game === "continue"){
            showMessage("continue");

            if (data.this_turn_player === data.userPlayer){
                $(".grid-row-item").off("click");
                $(".grid-row-item").click(function () {
                    let first = this.id[4];
                    let second = this.id[5];
                    if (!($("#item" + first + second).css("background-color") === data.userPlayer)){
                        $("#item" + first + second).css("background-color", data.this_turn_player);
                        data.items[first][second].fill = true;
                        data.items[first][second].player = data.this_turn_player;
                        data.items[first][second].count = data.turn;
                        data.this_turn_player = data.computerPlayer;
                        data.turn += 1;
                        doozSocket.send(JSON.stringify({
                            message: data,
                        }))
                    }else{
                        alert("Entry Is Selected before!")
                    }
                })
            }else if (data.this_turn_player === data.computerPlayer){

            }
        }else if (game === "User Won!"){
            $(".grid-row-item").off("click");
            showMessage("User Won!");
        }else if (game === "Computer Won!"){
            $(".grid-row-item").off("click");
            showMessage("Computer Won!");
        }else if (game === "Draw!"){
            $(".grid-row-item").off("click");
            showMessage("Draw!");
        }
    }

});


function createMessage(message) {
    let para = document.createElement("p");
    para.innerText = message;
    return para
}

function showMessage(message) {
    let paragraph = createMessage(message);
    $(".console").append(paragraph);
    $(".console").scrollTop($(".console")[0].scrollHeight);
}

function continue_game(mainObject) {
    if (mainObject.result.user){
        return "User Won!";
    }else if (mainObject.result.computer){
        fill_place(mainObject);
        return "Computer Won!";
    }else if (mainObject.result.row){
        fill_place(mainObject);
        return "Draw!";
    }else{
        fill_place(mainObject);
        return "continue";
    }

}

function fill_place(mainObject) {
    for (let i=0; i<3; i++){
        for (let j=0; j<3; j++){
            if (mainObject.items[i.toString()][j.toString()].fill){
                $("#item" + i + j).css("background-color", mainObject.items[i.toString()][j.toString()].player);
            }
        }
    }
}

function getRadioValue() {
    let value_green = $(".green_input:checked").val();
    let value_red = $(".red_input:checked").val();
    if (value_green === undefined){
        return 'red';
    }else if (value_red === undefined){
        return 'green';
    }
}




