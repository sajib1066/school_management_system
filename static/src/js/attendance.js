$(document).ready(function(){
    $('.attendance').on('click', function(){
        var btn_property = $(this);
        var row = $(this).closest('tr');
        var class_name = row.find('.cls_name').text();
        var roll = row.find('.std_roll').text();
        
        var api_url = 'http://127.0.0.1:8000/attendance/set-attendance/' + class_name + '/' + roll
        
        $.ajax({
            url: api_url,
            method: 'get',
            success: function(data){
                btn_property.addClass('btn btn-secondary');
            },
            error: function(err){
                alert('Already Present');
            }
        });
    });
});