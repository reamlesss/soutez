class Animal {
  constructor(name, species, color) {
    this.name = name;
    this.species = species;
    this.color = color;
  }
}

//funciton for saving animals to local storage

function saveToLocal(animals) {
  localStorage.setItem("animals", JSON.stringify(animals));
}
//function for loading animalss from local storage
function loadFromLocal() {
  const animalsString = localStorage.getItem("animals");
  return animalsString ? JSON.parse(animalsString) : [];
}

//function to add new animal to the list and then save to local storage
function addAnimal() {
  const name = document.getElementById("name").value;
  const species = document.getElementById("species").value;
  const color = document.getElementById("color").value;

  // check if user entered name and species and color right
  if (name == undefined || species == "" || color == "") {
    alert("Please enter something if u want to add!!!");
  } else {
    const animal = new Animal(name, species, color);

    let animals = loadFromLocal();
    animals.push(animal);
    saveToLocal(animals);
    alert("Animal added!");
  }
}

//function to search an animal by name in the list
function searchAnimal() {
  const searchName = document.getElementById("searchName").value.toLowerCase();
  let found = false;
  let result = "";

  const animals = loadFromLocal();
  for (const anim of animals) {
    if (anim.name.toLowerCase() === searchName.toLowerCase()) {
      result =
        "Jmeno:" +
        anim.name +
        ", Druh:" +
        anim.species +
        ", Barva: " +
        anim.color;
      // result = 'Jméno: ${anim.name}, Druh: ${anim.species}, Barva: ${anim.color}';
      found = true;
      break;
    }
  }

  if (!found) {
    result = "This animal was not found in the collection";
  }

  document.getElementById("result").innerHTML = result;
}
