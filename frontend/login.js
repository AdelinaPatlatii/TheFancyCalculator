async function login() {
  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;

  try {
    const response = await fetch("http://localhost:2025/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ username, password })
    });

    const data = await response.json();

    if (response.ok && data.message === "User authenticated!") {
      window.location.href = "/index.html";
    } else {
      alert("Invalid credentials!");
    }
  } catch (err) {
    alert("Login failed: " + err.message);
  }
}
