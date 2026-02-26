// chat/static/chat/chat.js
(function() {
  const messagesEl = document.getElementById("messages");
  const inputEl = document.getElementById("messageInput");
  const sendBtn = document.getElementById("sendBtn");
  let currentChannel = null;
  let socket = null;
  const unreadCounts = {}; // {channelName: number}

  function setChannel(name) {
    if (socket) socket.close();
    currentChannel = name;
    // Reset unread for active channel
    unreadCounts[name] = 0;
    updateUnreadBadges();

    // Load past messages
    fetch(`/chat/channel/${name}/`, {credentials: "include"})
      .then(res => res.text())
      .then(html => { messagesEl.innerHTML = html; messagesEl.scrollTop = messagesEl.scrollHeight; });

    // Connect WebSocket
    const scheme = window.location.protocol === "https:" ? "wss" : "ws";
    socket = new WebSocket(`${scheme}://${window.location.host}/ws/chat/${name}/`);

    socket.onmessage = (e) => {
      const data = JSON.parse(e.data);
      const displayName = `${data.user} (${data.year})`;
      const node = document.createElement("div");
      node.className = "msg";
      node.innerHTML = `
        <div class="meta">${displayName} <span class="time">${data.timestamp}</span></div>
        <div class="text">${escapeHtml(data.content)}</div>
      `;
      messagesEl.appendChild(node);
      messagesEl.scrollTop = messagesEl.scrollHeight;
    };

    socket.onclose = () => { /* optional reconnect logic */ };
  }

  function updateUnreadBadges() {
    document.querySelectorAll(".chat-tab, .channel-btn").forEach(btn => {
      const ch = btn.dataset.channel;
      const pill = document.getElementById(`unread-${ch}`) || document.getElementById(`pill-${ch}`);
      if (!pill) return;
      const val = unreadCounts[ch] || 0;
      pill.textContent = val;
      pill.style.display = val > 0 ? "inline-block" : "none";
    });
  }

  // Increment unread when message arrives for non-active channels
  // You’d implement this in a global WS listener if you subscribe to multiple channels.
  // For a single-channel connection, unread is increment via server-side events or polling.

  // Send message
  sendBtn.addEventListener("click", () => {
    const text = inputEl.value.trim();
    if (text && socket && socket.readyState === WebSocket.OPEN) {
      socket.send(JSON.stringify({message: text}));
      inputEl.value = "";
    }
  });
  inputEl.addEventListener("keydown", (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      sendBtn.click();
    }
  });

  // Channel switching
  document.querySelectorAll(".chat-tab, .channel-btn").forEach(btn => {
    btn.addEventListener("click", () => setChannel(btn.dataset.channel));
  });

  // Helpers
  function escapeHtml(str) {
    const div = document.createElement("div");
    div.innerText = str;
    return div.innerHTML;
  }

  // Init: set first channel
  const first = document.querySelector(".chat-tab");
  if (first) setChannel(first.dataset.channel);
})();

// In chat.js, poll unread counts every 20s
setInterval(() => {
  fetch("/chat/unread/", {credentials: "include"})
    .then(r => r.json())
    .then(data => {
      Object.keys(data).forEach(k => unreadCounts[k] = data[k]);
      updateUnreadBadges();
    });
}, 20000);