const $ = id => document.getElementById(id);
let blob = null, lastResults = [];

function showError(msg) { $("error").textContent = msg; $("error").hidden = false; }

function setImage(b) {
  blob = b;
  $("preview").src = URL.createObjectURL(b);
  $("preview").hidden = false;
  $("predict").disabled = false;
  $("error").hidden = $("warn").hidden = $("download").hidden = true;
  $("results").innerHTML = "";
}

$("file").onchange = e => {
  const f = e.target.files[0];
  if (!f) return;
  if (!/\.(jpe?g|png)$/i.test(f.name)) return showError("Invalid file type. Sirf JPG ya PNG.");
  if (f.size > 5 * 1024 * 1024) return showError("File too large. Max 5 MB.");
  setImage(f);
};

// Optional: webcam
$("cam").onclick = async () => {
  try {
    $("video").srcObject = await navigator.mediaDevices.getUserMedia({ video: true });
    $("video").hidden = $("snap").hidden = false;
  } catch { showError("Webcam access nahi mila."); }
};
$("snap").onclick = () => {
  const c = document.createElement("canvas");
  c.width = $("video").videoWidth; c.height = $("video").videoHeight;
  c.getContext("2d").drawImage($("video"), 0, 0);
  c.toBlob(b => setImage(b), "image/png");
  $("video").srcObject.getTracks().forEach(t => t.stop());
  $("video").hidden = $("snap").hidden = true;
};

$("predict").onclick = async () => {
  const fd = new FormData();
  fd.append("image", blob, blob.name || "webcam.png");
  $("predict").disabled = true; $("predict").textContent = "Predicting...";
  try {
    const res = await fetch("/predict", { method: "POST", body: fd });
    const data = await res.json();
    if (!res.ok) throw new Error(data.error);
    lastResults = data.predictions;
    $("results").innerHTML = data.predictions.map(p =>
      `<li><b>${p.label}</b> - ${p.confidence}%<div class="bar"><span style="width:${p.confidence}%"></span></div></li>`).join("");
    $("warn").textContent = data.warning || ""; $("warn").hidden = !data.warning;
    $("error").hidden = true; $("download").hidden = false;
  } catch (e) { showError(e.message || "Server error."); }
  $("predict").disabled = false; $("predict").textContent = "Predict";
};

$("download").onclick = () => {
  const txt = lastResults.map(p => `${p.label}: ${p.confidence}%`).join("\n");
  const a = document.createElement("a");
  a.href = URL.createObjectURL(new Blob([txt], { type: "text/plain" }));
  a.download = "results.txt"; a.click();
};
