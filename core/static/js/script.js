function togglePasswordVisibility() {
    const senhaField = document.getElementById("senha");
    const senhaToggle = document.querySelector(".password-toggle");

    if (senhaField.type === "password") {
        senhaField.type = "text";
        senhaToggle.classList.add("visible"); // Adicione a classe "visible" ao ícone de olho
    } else {
        senhaField.type = "password";
        senhaToggle.classList.remove("visible"); // Remova a classe "visible" do ícone de olho
    }
}





