// This is a Greasemonkey user script.
//
// ==UserScript==
// @name          GMail ad replacement (new design)
// @namespace     https://mail.google.com/mail
// @include       https://mail.google.com/*
// ==/UserScript==

var imageElement= document.getElementsByClassName("mq nH oy8Mbf");
imageElement.parentNode.removeChild(imageElement);