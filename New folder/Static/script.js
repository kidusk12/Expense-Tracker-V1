function showSuccess() {
    const msg = document.getElementById("success-msg");
    msg.style.display = "block";

    setTimeout(() => {
        msg.style.display = "none";
    }, 2000);
}