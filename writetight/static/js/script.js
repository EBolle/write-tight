"use strict";

// HTML elements

const form = document.querySelector("form");
const patternExps = document.querySelector(".pattern-explanations");
const refreshButton = document.querySelector(".refresh-button");
const returnText = document.querySelector(".return-text");
const submitButton = document.querySelector(".submit-button");
const noPatterns = document.querySelector(".no-patterns");

// Variables

const patterns = [
  "ambiguous-openings",
  "ambiguous-pronouns",
  "passive-voice",
  "subjunctive-mood",
  "words-ending-with-ly",
];

// There are only two functionalities for now: unhide patterns that are matched and unhide no patterns matched
// The refresh button should simply link to the input() function

// Hide the form when returnText is visible [this finally works!, now make it neat and add a REFRESH button]

const hideForm = function () {
  noPatterns.classList.add("hide");
  if (returnText.textContent) {
    form.classList.add("hide");
    if (returnText.querySelectorAll("span").length === 0) {
      noPatterns.classList.remove("hide");
    }
  } else {
    setTimeout(hideForm, 300);
  }
};

hideForm();

// Reveal pattern explanation on mouseover

const hideExplanations = function () {
  patternExps.querySelectorAll("p").forEach(function (element) {
    element.classList.add("hide");
  });
};

hideExplanations();

returnText.addEventListener("mouseover", function (event) {
  const classValue = event.target.classList.value;

  if (patterns.includes(classValue)) {
    patternExps.querySelector(`.${classValue}-exp`).classList.remove("hide");
  }
});

// Reset on click refresh-button

refreshButton.addEventListener("click", function (event) {
  form.classList.remove("hide");
  returnText.textContent = "";
  noPatterns.classList.add("hide");

  hideExplanations();
});
