async function doFibonacci() {
    clearOutput();

    const n = prompt("Enter a number n:");
    if (n !== null) {
        try {
            const response = await fetch(`http://localhost:2025/fibonacci?n=${n}`);
            const data = await response.json();

            if (!response.ok) {
                showError(data.detail || "Something went wrong");
                if (data.errors && data.errors.length) {
                    showError(data.errors[0].msg);
                }
            } else {
                document.getElementById('result').innerText = `Fibonacci(${n}) = ${data.result}`;
            }
        } catch (err) {
            showError("Failed to connect to backend.");
        }
    }
}

async function doFactorial() {
    clearOutput();

    const n = prompt("Enter a number:");
    if (n !== null) {
        try {
            const response = await fetch(`http://localhost:2025/factorial?n=${n}`);
            const data = await response.json();

            if (!response.ok) {
                showError(data.detail || "Something went wrong");
                if (data.errors && data.errors.length) {
                    showError(data.errors[0].msg);
                }
            } else {
                document.getElementById('result').innerText = `${n}! = ${data.result}`;
            }
        } catch (err) {
            showError("Failed to connect to backend.");
        }
    }
}

async function doPower() {
    clearOutput();

    const base = prompt("Enter base (a):");
    const exp = prompt("Enter exponent (b):");
    if (base !== null && exp !== null) {
        try {
            const response = await fetch(`http://localhost:2025/pow?base=${base}&exp=${exp}`);
            const data = await response.json();

            if (!response.ok) {
                showError(data.detail || "Something went wrong");
                if (data.errors && data.errors.length) {
                    showError(data.errors[0].msg);
                }
            } else {
                document.getElementById('result').innerText = `${base}^${exp} = ${data.result}`;
            }
        } catch (err) {
            showError("Failed to connect to backend.");
        }
    }
}

function showError(message) {
    document.getElementById('error').innerText = message;
}

function clearOutput() {
    document.getElementById('result').innerText = "";
    document.getElementById('error').innerText = "";
}
