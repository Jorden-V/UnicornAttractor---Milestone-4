$(function() {
  $('#submit_payment_btn').on('click', function() {
    $(this).prop('disabled', true);
    $("#payment-form").submit();
  });
});

 $('#payment-reset').click(function(){
            $('#payment-form').trigger("reset");
            $('#submit_payment_btn').prop('disabled', false);
 });
