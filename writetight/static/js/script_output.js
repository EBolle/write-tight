"use strict";

// HTML elements

const noPatterns = document.querySelector(".no-patterns");
const patternExpParagraphs = document
  .querySelector(".pattern-explanations")
  .querySelectorAll("p");
const patternSet = new Set();
const returnTextSpans = document
  .querySelector(".text-output")
  .querySelectorAll("span");

// Reveal pattern explanations when a pattern is matched, start by hiding all explanations

patternExpParagraphs.forEach(function (element) {
  element.classList.add("hide");
});

returnTextSpans.forEach(function (element) {
  patternSet.add(`${element.className}-exp`);
});

patternExpParagraphs.forEach(function (element) {
  const classValue = element.classList[0];

  if (patternSet.has(classValue)) {
    element.classList.remove("hide");
    noPatterns.classList.add("hide");
  }
});
