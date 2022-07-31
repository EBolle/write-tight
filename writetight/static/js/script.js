"use strict";

const returnText = document.querySelector(".return-text");
const patternExps = document.querySelector(".pattern-explanations");
const patterns = [
  "ambiguous-openings",
  "ambiguous-pronouns",
  "passive-voice",
  "subjunctive-mood",
  "words-ending-with-ly",
];

patternExps.querySelectorAll("p").forEach(function (element) {
  element.classList.add("hide");
});

returnText.addEventListener("mouseover", function (event) {
  const classValue = event.target.classList.value;

  if (patterns.includes(classValue)) {
    patternExps.querySelector(`.${classValue}-exp`).classList.remove("hide");
  }
});
