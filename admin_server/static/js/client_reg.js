var modal = new bootstrap.Modal(document.getElementById('success-modal'), {
  keyboard: false,
  backdrop: "static"
});

function sendRegistrationRequest() {
  var object = {};
  var list_keys = ['redirect_uris', 'grant_types', 'response_types', 'contacts', 'jwks'];
  new FormData(document.forms.client_info).forEach((value, key) => {
    var field = document.getElementById(key);
    field.classList.remove('is-invalid');
    field.parentElement.querySelectorAll('.invalid-feedback').forEach(elem => field.parentElement.removeChild(elem));

    if (value) object[key] = list_keys.indexOf(key) >= 0 ? value.trim().split(' ') : value;
  });
  var initial_token = object['initial-token'];
  var json = JSON.stringify(object);
  delete json['initial-token'];

  fetch('/oauth/register', {
    method: 'POST',
    body: json,
    headers: {
      'content-type': "application/json",
      'authorization': `Bearer ${initial_token}`
    }
  }).then(response => {
    if (!response.ok) {
      return Promise.reject(response);
    }
    return response.json();
  }).then(data => {
    document.getElementById('modal-message').innerHTML = `<p>Your client credentials are:</p>
                                                          <p>client_id: ${data['client_id']}</p>
                                                          <p>client_secret: ${data['client_secret']}</p>
                                                          <p>Save this data, OTHERWISE YOU'LL LOSE IT FOREVER!</p>`
    modal.toggle();
  }).catch(err => {
    err.json().then(data => {
      switch (err.status) {
        case 422:
          data['detail'].forEach(detail => {
            var elem = document.getElementById(detail['loc'][1]);
            elem.classList.add('is-invalid');
            if (elem.parentElement.querySelector('.invalid-feedback') === null) {
              var invalid_text = document.createElement('div');
              invalid_text.innerHTML = detail['msg'];
              invalid_text.classList.add('invalid-feedback');
              elem.parentElement.appendChild(invalid_text);
            }
          })
          break;
        case 400:
          console.log('Other error');
          break;
      }
    });
  });
}