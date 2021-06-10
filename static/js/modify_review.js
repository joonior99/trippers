function update(value) {
    let id_value = value;

    $.ajax({
        type: "POST",
        url: "/update",
        data: {
            id_value_give: id_value
        },
        success: function (response) {
            if (response["result"] == "success") {
                $('#modal-post2').addClass('is-active');
                title = response["title"];
                comment = response["comment"]
                file_name = response["file_name"]
                $("#hidden-id").val(value);
                $("#post-title2").val(title);
                $("#textarea-post2").text(comment);
                $("#preview-image2").attr("src", "static/img/" + file_name);
            } else {
                alert(response["msg"]);
            }
        }
    });
}

function setThumbnail2(value) {
    let file = $("#input-pic2").val().split("\\");
    let file_name = file[file.length - 1];
    console.log(file, file_name);
    $("#file-name2").text(file_name);

    if (value.files && value.files[0]) {
        let reader = new FileReader();
        reader.onload = function (e) {
            $("#preview-image2").attr("src", e.target.result);
        }
        reader.readAsDataURL((value.files[0]));
    }
}

function modifyCard() {
    let id_value = $("#hidden-id").val();
    let file = $("#input-pic2")[0].files[0];
    let title = $("#post-title2").val();
    let comment = $("#textarea-post2").val();

    let form_data = new FormData();
    /*console.log(id_value, file, title, comment);*/

    if (file === undefined) {
        form_data.append("id_value_give", id_value);
        form_data.append("title_give", title);
        form_data.append("comment_give", comment);
    } else {
        form_data.append("id_value_give", id_value);
        form_data.append("file_give", file);
        form_data.append("title_give", title);
        form_data.append("comment_give", comment);
    }

    $.ajax({
        type: "POST",
        url: "/modify_card",
        data: form_data,
        cache: false,
        contentType: false,
        processData: false,
        success: function (response) {
            alert(response["msg"]);
            $("#modal-post2").removeClass("is-active")
            window.location.reload()
        }
    });
}

