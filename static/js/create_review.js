function post() {
    let file = $("#input-pic")[0].files[0];
    let title = $("#post-title").val();
    let comment = $("#textarea-post").val();
    let date = new Date().toISOString();

    let form_data = new FormData();

    form_data.append("file_give", file);
    form_data.append("title_give", title);
    form_data.append("comment_give", comment);
    form_data.append("date_give", date);

    $.ajax({
        type: "POST",
        url: "/posting",
        data: form_data,
        cache: false,
        contentType: false,
        processData: false,
        success: function (response) {
            alert(response["msg"]);
            $("#modal-post").removeClass("is-active")
            window.location.reload()
        }
    });
}

function setThumbnail(value) {
    let file = $("#input-pic").val().split("\\");
    let file_name = file[file.length - 1];
    $("#file-name").text(file_name);

    if (value.files && value.files[0]) {
        let reader = new FileReader();
        reader.onload = function (e) {
            $("#preview-image").attr("src", e.target.result);
        }
        reader.readAsDataURL((value.files[0]));
    }
}