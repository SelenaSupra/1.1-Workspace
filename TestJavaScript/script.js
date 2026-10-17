console.log("Script is loaded!");


let numberofdogs = 3;
numberofdogs = 7;
console.log("The number of dogs is: " + numberofdogs)

const nameofBestDog = "Setanta";

// nameofBestDog = "Cu"

console.log("The best dog is: " + nameofBestDog)



console.log("Found another dog!")
numberofdogs += 1;
console.log("Now I have this many dogs: " + numberofdogs)

console.log("Lost a dog.")
numberofdogs -= 1;
console.log("The new count is " + numberofdogs)



let mydogs = numberofdogs ++;
let yourdogs = ++numberofdogs;

console.log("After: " )
console.log("My Dogs: " + mydogs)
console.log("Your Dogs: " + yourdogs)

let IHaveMoreDogs = mydogs > yourdogs;
console.log("I have more dogs: " + IHaveMoreDogs)


let weHaveTheSame = mydogs ==yourdogs;

console.log("We have the same number of dogs: " + weHaveTheSame)



let one = "1"
let numberOne = 1;

console.log(one)
console.log(numberOne)
let theseAreEqual = (one === numberOne);
console.log("These are equal: " + theseAreEqual)
console.log("Because the types of variables they are (string & number) are different.")


let age = 18;
let state = "MN"
let inMN = (state === "MN")
let Adult = (age >= 18);
console.log("Adult???? " + inMN)

let AdultinMN = (Adult && inMN);
console.log("Adult in MN???: " + AdultinMN)

let AdultOrMN = (Adult || inMN)
console.log("Adult OR MN???: " + AdultOrMN)

let notAdult = !Adult;
console.log("Not Adult?? " + notAdult)

let theseThingsAreTrue = (age && inMN)
console.log("These things are true: " + theseThingsAreTrue)



function testTruth (thisVariable, variableDescription){
    if (variableDescription) console.log("Variable Description: " + variableDescription);
    console.log("Value of the variable (converted to string):" + thisVariable);
    
    if (thisVariable) {
        console.log("Results: This variable is truthy!");
    } else {
        console.log("Result: This variable is falsey!");
    }
}


testTruth(true, "the literal value true")
testTruth(0, "The number zero")
testTruth(1, "The number one")
testTruth(222, "The number 222")

testTruth (-1, "The number negative one")

testTruth (0.0, "Zero point zero")

testTruth( (5 -5), "Five minus five")

testTruth("Rin", "My name is Rin")




const ClickHereButton = document.getElementById("ClickHereButton");
const carColorBox = document.getElementById("carColorBox");

ClickHereButton.style.color = "purple";

function describeCar() {

    const carColor = carColorBox.value;

    console.log("The car is " + carColor);

}
ClickHereButton.addEventListener("click", describeCar);



let message = "";

for (let count = 1; count <= 5; count++){
    message = "This is pass #" + count;
    console.log(message)
}



let dogs = ["Ace", "Setanta", "Hwasa"]
console.log(dogs)

for (count = 0; count < dogs.length; count++){
    console.log(dogs[count] + " is a good dog.")
}


let count = 0;

while(count < 100){
    console.log("The count is: " + count)
    count++
}

ClickHereButton.addEventListener("click", () => {
    setTimeout = ("3");
})

