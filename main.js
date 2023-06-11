function handleSubmit() {
  const data = document.getElementById("text-to-summarize").value;
  const url = "http://localhost:5000/summarize";
  const xhr = new XMLHttpRequest();
  xhr.open("POST", url);
  xhr.setRequestHeader("Content-Type", "application/json");
  xhr.setRequestHeader("Access-Control-Allow-Origin", "*");
  xhr.onreadystatechange = (xhr) =>
    xhr.target.readyState === XMLHttpRequest.DONE &&
    xhr.target.status === 200 &&
    handleResponseFromServer(xhr);
  xhr.send(JSON.stringify(data));
}

function handleResponseFromServer(xhr) {
  const { target } = xhr;
  const response = JSON.parse(target.responseText);
  displaySummarizedText(response);
}

function displaySummarizedText(response) {
  const { data } = response;
  const textArea = document.getElementById("summarized-text");

  textArea.value = data;
}

// TODO: Convert xhr request to promise based syntax
