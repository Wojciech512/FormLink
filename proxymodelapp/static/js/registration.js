document.addEventListener('DOMContentLoaded', function () {
    'use strict'
    const passwordInput = document.getElementById('id_password');
    const passwordInput2 = document.getElementById('id_password2');
    const showPasswordCheckbox = document.getElementById('show-password');
  
    showPasswordCheckbox.addEventListener('change', function() {
      if (this.checked) {
        passwordInput.type = 'text';
        passwordInput2.type = 'text';
      } else {
        passwordInput.type = 'password';
        passwordInput2.type = 'password';
      }
    });
  });
  