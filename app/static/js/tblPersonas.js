document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("frmBusqueda");
  const inputBuscar = document.querySelector("input[name='txtBuscar']");
  const tablaDatos = document.getElementById("tblDatos").querySelector("tbody");
  const tipoInfo = document.getElementById("tipoInformacion");

  form.addEventListener("submit", async function (event) {
    event.preventDefault(); // Evita la recarga de la página

    const criterio = inputBuscar.value.trim().replace(/\//g, "-"); //en caso que la fecha tenga separador /
    const tipoI = tipoInfo.innerHTML.trim();

    if (!criterio) {
      alert("Por favor, ingrese un criterio de búsqueda.");
      return;
    }

    // Llamada a la API usando el criterio ingresado


    switch (tipoI) {
      case "Pacientes":
        busqueda('persona', criterio, 'P', rellenarTabla);
        break;
      case "Empleados":
        busqueda('persona', criterio, 'E', rellenarTabla);
        break;
      case "Fichas":
        buscarFichas('ficha', criterio, 'F');
        break;
      case "Turnos":
        busqueda('turno', criterio, 'F', rellenarTablaTur);
        break;
      case "Especialidades":
        buscarEspecialidad('especialidad', criterio, 'F');
        break;
      case "Usuarios":
        buscarUsuarios('usuario', criterio, 'F');
        break;
      case "Prestaciones":
        buscarPrestacion('prestacion', criterio, 'F');
        break;
    }

  });

  async function busqueda(url, criterio, tipo, callback) {
    try {
      const response = await fetch(`http://127.0.0.1:5000/api/${url}/busca/${criterio}/${tipo}`);
      if (!response.ok) {
        throw new Error('Error en la busqueda. Revise el criterio ingresado');
      }
      const data = await response.json();
      callback(data, url, tipo);
    } catch (error) {
      console.rror(`Error al realiza la busqueda de ${url.toLowerCase()}`, error)
      alert(`Hubo un error en la busqueda de ${url.toLowerCase()}`);
    }
  }

  function rellenarTablaTur(datos, url, tipo) {
    const tb = document.getElementById("tblDatos");
    tb.innerHTML = "";

    const cabecera = document.createElement('thead');
    cabecera.innerHTML = `<th>Id</th>
                          <th>Fecha Inicio</th>
                          <th>Fecha Fin</th>
                          <th>Dia Sem</th>
                          <th>Especialidad</th>
                          <th>Nombres</th>
                          <th>Paterno</th>
                          <th>Materno</th>`;
    tb.appendChild(cabecera);

    if (!datos || datos.length === 0) {
      const filaVacia = document.createElement("tr");
      filaVacia.innerHTML = '<td colspan="8">No se encontraron resultados</td>';
      tablaDatos.appendChild(filaVacia);
      return;
    }

    datos.forEach((turno, index) => {
      const fila = document.createElement("tr")
      const fechaIni = new Date(turno.fecha_inicio);
      const fechaIniForm = fechaIni.toLocaleDateString("es-ES");
      const fechaFin = new Date(turno.fecha_fin);
      const fechaFinForm = fechaFin.toLocaleDateString("es-ES");

      const enlace = `<a href="editarTurno/${turno.id_turno}" title="Editar"><img src="/static/assets/img/list-outline.svg" width="20" height="20" alt=""></a>`
      fila.innerHTML = `
        <td>${turno.id_turno}</td>
        <td>${fechaIniForm}</td>
        <td>${fechaFinForm}</td>
        <td>${turno.dia_semana}</td>
        <td>${turno.nombre_especialidad}</td>
        <td>${turno.nombres}</td>
        <td>${turno.paterno}</td>
        <td>${turno.materno}</td>
        <td>${enlace}</td>
      `;
      tb.appendChild(fila);

    });

  }


  function rellenarTabla(datos, url, tipo) {
    // Limpiar la tabla antes de agregar los nuevos datos
    tablaDatos.innerHTML = "";

    // Verificar si el array de personas tiene elementos
    if (!datos.persona || datos.persona.length === 0) {
      const filaVacia = document.createElement("tr");
      filaVacia.innerHTML = '<td colspan="7">No se encontraron resultados</td>';
      tablaDatos.appendChild(filaVacia);
      return;
    }

    if ((tipo == "E") || (tipo == "P") || (tipo == "Personas")) {

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