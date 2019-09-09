/* ---------- Disables payment button once clicked and submits form ---------*/
$(function() {
    $('#submit_payment_btn').on('click', function() {
         $("#submit_payment_btn").attr("disabled", true);
         $("#payment-form").submit();
    });
});

/* ---------- Resets payment form and re-enables payment button ---------*/
$('#payment-reset').click(function() {
  $('#form-reset').trigger("reset");
  $('#submit_payment_btn').prop('disabled', false);
});

/* ---------- Loads modal to display information on payment ---------*/
$(window).on('load', function() {
    $('#paymentGuide').modal('show');
  });
