javascript:if(document.getElementById('submitButton') != null) {
		document.getElementById('submitButton').disabled = false;
	} else {
		$("#lightsOff").trigger("click"); play_video('play');
	}