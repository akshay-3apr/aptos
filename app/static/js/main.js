(function($) {
    "use strict";

    var timeout = 3000; // in miliseconds (3*1000)
    var reader = new FileReader();
    $('.banner').delay(timeout).fadeOut(500);

    reader.onload = function (e) {
        $('.container-fluid').find('.row.justify-content-between .uploadedImage').last().remove()
        $('.container-fluid').find('.row.justify-content-between').first().append('<div class="col-xs-12 col-sm-8 col-md-4 col-sm-offset-2 col-md-offset-4 align-self-end uploadedImage"><br><img src = "' + e.target.result + '" alt="Uploaded Image" width="400px" height="400px"></div>');
    };

    $('#image').change(function(e) {
        reader.readAsDataURL(e.target.files[0]);
        var file = this.files;
        var formData = new FormData($('form')[0]);
        formData.append('file', file[0]);
        if (this.files.length > 0) {
            $.ajax({
                url: '/displayImage',
                type: 'POST',
                data: formData,
                contentType: false,
                cache: false,
                processData: false,
                async: true,
                success: function(data) {
                    console.log(data);
                    $('.uploadedImage').append('<div class="label">'+data.label+'</div>');
                    $('.label').css({"background-color": "green", "width": "400px","text-align":"center"})
                },
                error: function(data) {
                    //debugger;
                    console.log(data.responseJSON)
                    if ($('hr + ul').length == 0)
                        $('hr').after('<ul class="list-group"><li class="list-group-item d-flex justify-content-between align-items-center">' + data.responseJSON.error_msg + '<span class="badge badge-primary badge-pill">1</span></li></ul>')
                    else {
                        let value = $('hr + ul .badge').text();
                        value = parseInt(value) + 1;
                        $('hr + ul .badge').text(value);
                        $('#image').val('')
                    }
                },
            });
        }
    });

    $(document).on('hidden.bs.modal', '#cameraModal', function() {
        const player = document.getElementById('player');
        player.srcObject.getVideoTracks().forEach(track => track.stop());
        $('body').find('.modal').remove()
    });

})(jQuery);