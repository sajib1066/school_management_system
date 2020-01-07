$("#id_district").change(function () {
  var url = $("#StudentRegistrationForm").attr("data-upazilla-url");
  var districtId = $(this).val();

  $.ajax({
    url: url,
    data: {
      'district': districtId
    },
    success: function (data) {
      $("#id_upazilla").html(data);
    }
  });

});
$("#id_upazilla").change(function () {
  var url = $("#StudentRegistrationForm").attr("data-upazilla-url");
  var upazillaId = $(this).val();

  $.ajax({
    url: url,
    data: {
      'upazilla': upazillaId
    },
    success: function (data) {
      $("#id_union").html(data);
    }
  });

});
