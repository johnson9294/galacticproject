document.getElementById('jsonForm').addEventListener('submit', async (e) => {
  e.preventDefault();
  const data = document.getElementById('myInput').value;
  fetch('<網址>', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ link: data })
  })
  .then(response => response.text())
  .then(body => {
    console.log(body);
    document.getElementById('responseDisplay').textContent = body;
  });
});