function Volver() {
    if (document.referrer) {
        window.history.back();
    } else {
        window.location.href = "{% url 'catalogo' %}";
    }
}

function Reserva(){
    
}