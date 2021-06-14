function toggleRotate() {
  const element = document.querySelector("#pokeball");
  element.classList.toggle("rotate");
}

for (const span of document.querySelectorAll("span")) {
  switch (span.textContent) {
    case "Grass":
      span.style.backgroundColor = "mediumseagreen";
      break;
    case "Poison":
      span.style.backgroundColor = "purple";
      break;
    case "Fire":
      span.style.backgroundColor = "crimson";
      break;
    case "Flying":
      span.style.backgroundColor = "deepskyblue";
      break;
    case "Water":
      span.style.backgroundColor = "royalblue";
      break;
    case "Bug":
      span.style.backgroundColor = "green";
      break;
    case "Normal":
      span.style.backgroundColor = "grey";
      break;
    case "Electric":
      span.style.backgroundColor = "gold";
      break;
    case "Ground":
      span.style.backgroundColor = "darkgoldenrod";
      break;
    case "Fairy":
      span.style.backgroundColor = "hotpink";
      break;
    case "Fighting":
      span.style.backgroundColor = "sandybrown";
      break;
    case "Rock":
      span.style.backgroundColor = "dimgray";
      break;
    case "Psychic":
      span.style.backgroundColor = "darkviolet";
      break;
    case "Ghost":
      span.style.backgroundColor = "darkslateblue";
      break;
    case "Ice":
      span.style.backgroundColor = "cyan";
      break;
    case "Dragon":
      span.style.backgroundColor = "goldenrod";
      break;
  }
}
