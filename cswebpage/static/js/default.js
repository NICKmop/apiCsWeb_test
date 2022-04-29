$(document).ready(function(){
    $('.csWebTable.close').hide();
    $('.csWebTable.idle').click(function(){
        // "/pangTable"
        $('.csWebTable.idle').hide();
        $('.csWebTable.close').show();
    });
    $('.csWebTable.close').click(function(){
        // "/pangTable"
        $('.csWebTable.idle').show();
        $('.csWebTable.close').hide();
    });

    $("#keyword").keyup(function() {
        var k = $(this).val();
        $(".type08 > tbody > tr").hide();

        var temp = $(".type08 > tbody > tr > th:contains('" + k + "')");

        $(temp).parent().show();
    })
});