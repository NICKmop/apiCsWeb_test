$(document).ready(function(){
    $('.pangTable.close').hide();
    $('.pangTable.idle').click(function(){
        // "/pangTable"
        $('.pangTable.idle').hide();
        $('.pangTable.close').show();
    });
    $('.pangTable.close').click(function(){
        // "/pangTable"
        $('.pangTable.idle').show();
        $('.pangTable.close').hide();
    });

    $("#keyword").keyup(function() {
        var k = $(this).val();
        $(".type08 > tbody > tr").hide();

        var temp = $(".type08 > tbody > tr > th:contains('" + k + "')");

        $(temp).parent().show();
    })
});