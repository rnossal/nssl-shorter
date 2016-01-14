var request = new XMLHttpRequest();

function shortIt() {
	var urlInput = document.getElementById('url-input').value;
	request.open('POST', '/shortIt', true);
	request.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
	request.onreadystatechange = function() {
		if(request.readyState == 4 && request.status == 200) {
			printMessage(request.responseText);
		}
	};
	request.send('urlInput=' + urlInput);
}

function printMessage(response) {
	response = JSON.parse(response);
	var message = document.createElement('span');
	message.id = 'spn';
	if (response.errorCode == null) {
		var newUrl = window.location.href + response.url;
		message.innerHTML = 'Aqui está sua URL encurtada: <a id="newURL" href="' + newUrl + '">' + newUrl + '</a>';
		message.className = 'urlDone';
	}
	else if (response.errorCode == 0) {
		message.innerHTML = 'Você precisa fornecer alguma URL para ser encurtada pelo menos.';
		message.className = 'urlError';
	}
	else if (response.errorCode == 1) {
		message.innerHTML = 'A URL que você forneceu não parace muito ser uma URL válida.';
		message.className = 'urlError';
	}
	var spn = document.getElementById('spn');
	if (spn != null) {
		spn.parentNode.removeChild(spn);
	}
	insertAfter(message, document.getElementById('cont'));
}

function insertAfter(newNode, referenceNode) {
	referenceNode.parentNode.insertBefore(newNode, referenceNode.nextSibling);
}
