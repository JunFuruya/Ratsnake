//alert("test");

function submitByPostMethod(formId, actionUri) {
  objForm = $('#' + formId);
  objForm.attr('action', actionUri);
  objForm.attr('method', 'POST');
  objForm.submit();
}

function submitByGetMethod(formId, actionUri) {
  objForm = $('#' + formId);
  objForm.attr('action', actionUri);
  objForm.attr('method', 'GET');
  objForm.submit();
}

