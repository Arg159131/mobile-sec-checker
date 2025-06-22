function checkNumber() {
  const number = document.getElementById("number").value;
  const error = document.getElementById("error");
  error.textContent = "";

  if (!number.startsWith("+") || number.length < 10) {
    error.textContent = "Please enter a valid international number.";
    return;
  }

  fetch("/check-number", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ number }),
  })
  .then(res => res.json())
  .then(data => {
    document.getElementById("result").textContent = JSON.stringify(data, null, 4);
  });
}
