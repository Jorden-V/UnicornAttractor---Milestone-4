/* ---------- Loads modal to display information on payment ---------*/
$(window).on('load', function() {
    $('#paymentGuide').modal('show');
  });


/* ---------- changes text when payment form is submitted ---------*/
$('#payment-form').submit(function()
 {
    $("input[type='submit']", this)
      .val("Please Wait...");
    return true;
  });