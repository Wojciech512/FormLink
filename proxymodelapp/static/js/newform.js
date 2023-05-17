document.addEventListener('DOMContentLoaded', function () {
    'use strict'
  
    var forms = document.querySelectorAll('.needs-validation')
    
    Array.prototype.slice.call(forms)
      .forEach(function (form) {
        form.addEventListener('submit', function (event) {
          if (!form.checkValidity()) {
            event.preventDefault()
            event.stopPropagation()
          }
          
          if (form.checkValidity()){
            alert("Formularz utworzony!")
            window.location.replace("/")
          }
          form.classList.add('was-validated')
        }, false)
      })
  })

  function EnableDisableTextBoxNext(opt) {

    if (opt=="Yes"){
        document.getElementById("date_of_covid19").disabled = false;
    }
    else{
        document.getElementById("date_of_covid19").disabled = true;
    }
}

function EnableDisableTextBoxNext2(opt) {

  if (opt=="Yes"){
      document.getElementById("date_of_covid19_vaccinated").disabled = false;
  }
  else{
      document.getElementById("date_of_covid19_vaccinated").disabled = true;
  }
}

function enableDisableInput(fieldId){
  var inputField = document.getElementById(fieldId);

  if (inputField.value == '') {
    document.getElementById("phone_number_to_contact").disabled = true;
    document.getElementById("connection_with_patient").disabled = true;
    document.getElementById("phone_number_to_contact").value = null;
    document.getElementById("connection_with_patient").value = null;
  } else {
    document.getElementById("phone_number_to_contact").disabled = false;
    document.getElementById("connection_with_patient").disabled = false;

  }
}

function enableDisableInput2(fieldId){
  var inputField = document.getElementById(fieldId);

  if (inputField.value == '') {
    document.getElementById("drug_dose").disabled = true;
    document.getElementById("m_a_e_drug_dose").disabled = true;
    document.getElementById("drug_dose").value = null;
    document.getElementById("m_a_e_drug_dose").value = null;
  } else {
    document.getElementById("drug_dose").disabled = false;
    document.getElementById("m_a_e_drug_dose").disabled = false;
  }
}

window.onload=function(){
  var today = new Date().toISOString().split('T')[0];
  document.getElementsByName("date_of_birth")[0].setAttribute('max', today);
  document.getElementsByName("date_of_covid19")[0].setAttribute('max', today);
  document.getElementsByName("date_of_covid19_vaccinated")[0].setAttribute('max', today)
}
