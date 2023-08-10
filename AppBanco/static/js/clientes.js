document.addEventListener("DOMContentLoaded", function() {

    document.getElementById("frminsertar").addEventListener("submit", function(event) {
      event.preventDefault();  // Evitar el envío del formulario por defecto
    
      // Capturar los datos del formulario
      var data = {
        Documento: document.getElementById("Documento").value,
        Nombre: document.getElementById("Nombre").value,
        Apellido: document.getElementById("Apellido").value,
        Correo: document.getElementById("Correo").value,
        Celular: document.getElementById("Celular").value
      };
      //probamos si los datos se estan enviando
      console.log( document.getElementById("Documento").value,document.getElementById("Nombre").value,)
  
      // Convertir el objeto a una cadena JSON
      var jsonData = JSON.stringify(data);
  
      // Realizar la solicitud POST con fetch
      fetch("http://127.0.0.1:8000/insertar/", {
        method: "POST",
        body: jsonData,
        headers: {
          "Content-Type": "application/json"
        }
      })
      .then(response => response.json())
      .then(data => {
        // Procesar la respuesta del servidor
        console.log(data);
      })
      .catch(error => {
        console.error("Error:", error);
      });

      consultar();

    });

   // Importar archivo2.js


// Llamar a la función



  });




  