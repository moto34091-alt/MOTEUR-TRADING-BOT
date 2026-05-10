const signals = [
    "BUY 🟢",
    "SELL 🔴"
];

const pairs = [
    "EUR/USD OTC",
    "GBP/USD OTC",
    "USD/JPY OTC",
    "EUR/JPY OTC"
];

const signalBox = document.querySelector(".signal");
const pairBox = document.querySelector(".pair");
const accuracyBox = document.querySelector(".accuracy");

document.querySelector(".generate-btn").addEventListener("click", () => {

    signalBox.innerHTML = "SCANNING...";

    setTimeout(() => {

        const signal = signals[Math.floor(Math.random() * signals.length)];

        const pair = pairs[Math.floor(Math.random() * pairs.length)];

        const accuracy = Math.floor(Math.random() * 10) + 90;

        pairBox.innerHTML = pair;

        signalBox.innerHTML = signal;

        accuracyBox.innerHTML = `ACCURACY ${accuracy}%`;

    }, 2000);

});
