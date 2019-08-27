/* ---------- Disables payment button once clicked and submits form ---------*/
$(function() {
  $('#submit_payment_btn').on('click', function() {
    $(this).prop('disabled', true);
    $("#payment-form").submit();
  });
});

/* ---------- Resets payment form and re-enables payment button ---------*/
 $('#payment-reset').click(function(){
            $('#payment-form').trigger("reset");
            $('#submit_payment_btn').prop('disabled', false);
 });
