document.addEventListener("DOMContentLoaded", function () {
  const form = document.querySelector("form");
  const inputBuscar = document.querySelector("input[name='txtBuscar']");
  const tablaDatos = document.getElementById("tblDatos").querySelector("tbody");
  const tipoInfo = document.getElementById("tipoInformacion");

  form.addEventListener("submit", async function (event) {
    event.preventDefault(); // Evita la recarga de la página

    const criterio = inputBuscar.value.trim();
    const tipoI = tipoInfo.innerHTML.trim();

    if (!criterio) {
      alert("Por favor, ingrese un criterio de búsqueda.");
      return;
    }

    // Llamada a la API usando el criterio ingresado

    switch (tipoI) {
      case "Empleados":
        buscarPersonas('persona', criterio, "E");
        break;
      case "Pacientes":
        buscaPersonas('persona', criterio, "P");
        break;
      case "Personas":
        buscaPersonas('persona', criterio, "");
        break;
      case "Turnos":
        break;
      case "Fichas":
        break;
      case "Especialidades":
        break;
    }


    // try {
    //   const response = await fetch(`http://127.0.0.1:5000/api/persona/busca/${criterio}`);
    //   if (!response.ok) {
    //     throw new Error("Error en la búsqueda. Revise el criterio ingresado.");
    //   }

    //   const data = await response.json();
    //   rellenarTabla(data);
    // } catch (error) {
    //   console.error("Error al realizar la búsqueda:", error);
    //   alert("Hubo un error en la búsqueda.");
    // }
  });

  async function buscarPersonas(url, criterio, tipo) {
    try {
      const response = await fetch(`http://127.0.0.1:5000/api/${url}/busca/${criterio}/${tipo}`);
      if (!response.ok) {
        throw new Error("Error en la busqueda. Revise el criterio ingresado");
      }

      const data = await response.json();
      rellenarTabla(data, tipo);
    } catch (error) {
      console.error("Error al ralizar la busqueda", error);
      alert("Hubo un error en la buasqueda")
    }
  }

  function rellenarTabla(datos, tipo) {
    // Limpiar la tabla antes de agregar los nuevos datos
    tablaDatos.innerHTML = "";

    // Verificar si el array de personas tiene elementos
    if (!datos.persona || datos.persona.length === 0) {
      const filaVacia = document.createElement("tr");
      filaVacia.innerHTML = '<td colspan="7">No se encontraron resultados</td>';
      tablaDatos.appendChild(filaVacia);
      return;
    }

    if ((tipo == "Empleados") || (tipo == "Pacientes") || (tipo == "Personas")) {

      // Iterar sobre los datos y crear filas en la tabla
      datos.persona.forEach((persona, index) => {
        const fila = document.createElement("tr");

        // Convertir fecha de nacimiento a formato "dd/mm/yyyy"
        const fechaNac = new Date(persona.fecha_nacimiento);
        const fechaFormateada = fechaNac.toLocaleDateString("es-ES");


        const enlaceEditar = `<a href="editarPersona/${persona.id_persona}" title="Editar"><img src="/static/assets/img/list-outline.svg" width="20" height="20" alt=""></a>`;

        fila.innerHTML = `
          <td>${index + 1}</td>
          <td>${persona.ci}</td>
          <td>${persona.nombres}</td>
          <td>${persona.paterno}</td>
          <td>${persona.materno}</td>
          <td>${fechaFormateada}</td>
          <td>${enlaceEditar}</td>
        `;
        tablaDatos.appendChild(fila);
      });
    }
  }

});  