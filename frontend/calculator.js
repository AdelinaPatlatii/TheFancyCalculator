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
                document.getElementById('result').innerHTML = `${base}<sup>${exp}</sup> = ${data.result}`;
            }
        } catch (err) {
            showError("Failed to connect to backend.");
        }
    }
}


async function doGCD() {
    clearOutput();

    const a = prompt("Enter first number (a):");
    const b = prompt("Enter second number (b):");
    if (a !== null && b !== null) {
        try {
            const response = await fetch(`http://localhost:2025/gcd?a=${a}&b=${b}`);
            const data = await response.json();

            if (!response.ok) {
                showError(data.detail || "Something went wrong");
                if (data.errors && data.errors.length) {
                    showError(data.errors[0].msg);
                }
            } else {
                document.getElementById('result').innerText = `GCD(${a}, ${b}) = ${data.result}`;
            }
        } catch (err) {
            showError("Failed to connect to backend.");
        }
    }
}


async function doLCM() {
    clearOutput();

    const a = prompt("Enter first number (a):");
    const b = prompt("Enter second number (b):");
    if (a !== null && b !== null) {
        try {
            const response = await fetch(`http://localhost:2025/lcm?a=${a}&b=${b}`);
            const data = await response.json();

            if (!response.ok) {
                showError(data.detail || "Something went wrong");
                if (data.errors && data.errors.length) {
                    showError(data.errors[0].msg);
                }
            } else {
                document.getElementById('result').innerText = `LCM(${a}, ${b}) = ${data.result}`;
            }
        } catch (err) {
            showError("Failed to connect to backend.");
        }
    }
}


async function doLogarithm() {
    clearOutput();

    const base = prompt("Enter base (a):");
    const value = prompt("Enter value (b):");
    if (base !== null && value !== null) {
        try {
            const response = await fetch(`http://localhost:2025/logarithm?base=${base}&value=${value}`);
            const data = await response.json();

            if (!response.ok) {
                showError(data.detail || "Something went wrong");
                if (data.errors && data.errors.length) {
                    showError(data.errors[0].msg);
                }
            } else {
                document.getElementById('result').innerHTML = `log<sub>${base}</sub>${value} = ${data.result}`;
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
