const API_URL = window.location.origin;

const chatBox = document.getElementById("chat-box");
const question = document.getElementById("question");
const send = document.getElementById("send");
const typing = document.getElementById("typing");
const clearChat = document.getElementById("clear-chat");

let session_id = localStorage.getItem("session_id");

if (!session_id) {
    session_id = crypto.randomUUID();
    localStorage.setItem("session_id", session_id);
}

function scrollBottom() {
    chatBox.scrollTop = chatBox.scrollHeight;
}

function createMessage(role, text) {

    const message = document.createElement("div");
    message.className = `message ${role}`;

    const avatar = document.createElement("div");
    avatar.className = "avatar";
    avatar.innerText = role === "user" ? "U" : "AI";

    const bubble = document.createElement("div");
    bubble.className = "bubble";
    bubble.innerText = text;

    if (role === "user") {
        message.appendChild(bubble);
        message.appendChild(avatar);
    } else {
        message.appendChild(avatar);
        message.appendChild(bubble);
    }

    chatBox.appendChild(message);

    scrollBottom();
}

function setLoading(status) {

    send.disabled = status;

    typing.style.display = status
        ? "flex"
        : "none";

    send.innerText = status
        ? "..."
        : "Send";
}

async function sendMessage() {

    const text = question.value.trim();

    if (text === "") return;

    createMessage(
        "user",
        text
    );

    question.value = "";

    autoResize();

    setLoading(true);

    try {

        const response = await fetch(
            `${API_URL}/chat`,
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    session_id: session_id,
                    question: text
                })
            }
        );

        if (!response.ok) {
            throw new Error("Server Error");
        }

        const data = await response.json();

        createMessage(
            "bot",
            data.answer
        );

    }

    catch (error) {

        createMessage(
            "bot",
            "Sorry, something went wrong."
        );

        console.error(error);

    }

    finally {

        setLoading(false);

    }

}

function autoResize() {

    question.style.height = "auto";

    question.style.height =
        question.scrollHeight + "px";

}

question.addEventListener(
    "input",
    autoResize
);

send.addEventListener(
    "click",
    sendMessage
);

question.addEventListener(
    "keydown",
    function (e) {

        if (
            e.key === "Enter" &&
            !e.shiftKey
        ) {

            e.preventDefault();

            sendMessage();

        }

    }
);

clearChat.addEventListener(
    "click",
    async function () {

        try {

            await fetch(
                `${API_URL}/clear-history`,
                {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({
                        session_id: session_id
                    })
                }
            );

        }

        catch (e) {

            console.log(e);

        }

        chatBox.innerHTML = "";

        createMessage(
            "bot",
            "Hello! How can I help you today?"
        );

    }
);

window.onload = function () {

    createMessage(
        "bot",
        "Welcome! Ask me anything about our products, orders, shipping, returns, or policies."
    );

};