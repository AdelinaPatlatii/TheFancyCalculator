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

    if (response.ok && data.access_token) {
      localStorage.setItem("token", data.access_token);
      window.location.href = "/calculator.html";
    } else {
      alert("Invalid credentials!");
    }
  } catch (err) {
    alert("Login failed: " + err.message);
  }
}


window.addEventListener("message", (event) => {
  if (event.data?.type === "signup-success" && event.data.token) {
    localStorage.setItem("token", event.data.token);
    window.location.href = "/calculator.html";
  }
});