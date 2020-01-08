// form visible
$('#academic_info_btn').on('click', function(){
  $('.academic_info').hide();
  $('.personal_info').show();
});

// Presonal Information
$('#personal_info_btn').on('click', function(){
  $('.personal_info').hide();
  $('.address_info').show();
});

$('#personal_info_prev_btn').on('click', function(){
  $('.personal_info').hide();
  $('.academic_info').show();
});

// Address Information
$('#address_info_btn').on('click', function(){
  $('.address_info').hide();
  $('.guardian_info').show();
});

$('#address_info_prev_btn').on('click', function(){
  $('.address_info').hide();
  $('.personal_info').show();
});

// Guardian Information
$('#guardian_info_btn').on('click', function(){
  $('.guardian_info').hide();
  $('.emergency_contact_info').show();
});

$('#guardian_info_prev_btn').on('click', function(){
  $('.guardian_info').hide();
  $('.address_info').show();
});

// Emergency Contact Information
$('#emergency_contact_info_btn').on('click', function(){
  $('.emergency_contact_info').hide();
  $('.previous_academic_info').show();
});

$('#emergency_contact_info_prev_btn').on('click', function(){
  $('.emergency_contact_info').hide();
  $('.guardian_info').show();
});

// Previous Academic Information
$('#previous_academic_info_btn').on('click', function(){
  $('.previous_academic_info').hide();
  $('.previous_academic_certificate').show();
  $('#submit').show();
});

$('#previous_academic_info_prev_btn').on('click', function(){
  $('.previous_academic_info').hide();
  $('.emergency_contact_info').show();
});

// Previous Academic Certificate Information
$('#previous_academic_certificate_prev_btn').on('click', function(){
  $('.previous_academic_certificate').hide();
  $('.previous_academic_info').show();
});
