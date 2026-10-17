console.log("Script loaded!");


function moveTheThing(){
    const theThing = document.getElementById("theThing");
    const leftBlock = document.getElementById("leftBlock");
    const rightBlock = document.getElementById("rightBlock");

    if (leftBlock.childElementCount > 0) {
        rightBlock.append(theThing);
    } else {
        leftBlock.append(theThing);
    }
}

function styleTheText(){
    const fancyText = document.getElementById("fancyText");
    fancyText.style.color = "purple";
    fancyText.style.fontFamily = "Symbol, sans-serif";
    fancyText.style.fontSize = "4em";

}

function getFormValues(){
    const firstField = document.getElementById("firstField");
    const secondField = document.getElementById("secondField");
    const thirdField = document.getElementById("thirdField");

    const firstResult = document.getElementById("firstResult");
    firstResult.textContent = firstField.value;

    const secondResult = document.getElementById("secondResult");
    secondResult.textContent = secondField.value;

    const thirdResult = document.getElementById("thirdResult");
    thirdResult.textContent = thirdField.checked;      


}

function countTheStuff(){
    const countOfP = document.querySelectorAll("P").length;
    const countOfH2 = document.querySelectorAll("H2").length;
    const countOfTD = document.querySelectorAll("TD").length;

    const countOfPResult = document.getElementById("countOfP");
    countOfPResult.innerText = countOfP;

    const countOfH2Result = document.getElementById("countOfH2");
    countOfH2Result.innerText = countOfH2;

    const countOfTDResult = document.getElementById("countOfTD");
    countOfTDResult.innerText = countOfTD;
}

function addNewRow(){
    const addRowsTable = document.getElementById("addRowsTable");
    const theTable = addRowsTable.childNodes[1];
    const lastRow = theTable.children[theTable.children.length-1];
    const currentCount = lastRow.innerText;
    const newRow = addRowsTable.insertRow();
    newRow.innerHTML = `<td>${+currentCount +1}</td>`;


}

function yourBonusChallenge(){
        window.open(404);

}