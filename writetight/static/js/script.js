"use strict";

// HTML elements

const form = document.querySelector("form");
const patternExps = document.querySelector(".pattern-explanations");
const refreshButton = document.querySelector(".refresh-button");
const returnText = document.querySelector(".return-text");
const submitButton = document.querySelector(".submit-button");

// Variables

const patterns = [
  "ambiguous-openings",
  "ambiguous-pronouns",
  "passive-voice",
  "subjunctive-mood",
  "words-ending-with-ly",
];

// Hide the form when returnText is visible [this finally works!, now make it neat and add a REFRESH button]

const hideForm = function () {
  if (returnText.textContent) {
    form.classList.add("hide");
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

  hideExplanations();
});
