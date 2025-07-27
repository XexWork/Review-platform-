document.addEventListener('DOMContentLoaded', () => {

    const registerForm = document.querySelector('form[action="/register"]');

    if (registerForm) {
    registerForm.addEventListener('submit', e => {
      const username = registerForm.querySelector('input[name="username"]').value.trim();
      const password = registerForm.querySelector('input[name="password"]').value.trim();
      if (username.length < 3 || username.length > 20) {
        e.preventDefault();
        alert('Логин должен быть от 3 до 20 символов');
      }
      if (password.length < 6 || password.length > 50) {
        e.preventDefault();
        alert('Пароль должен быть от 6 до 50 символов');
      }
    });
  }
});
