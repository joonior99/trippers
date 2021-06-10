function logout() {
    $.removeCookie("mytoken");
    alert("로그아웃 되었습니다.");
    window.location.href = "/";
}

function time2str(date) {
    let today = new Date()
    let time = (today - date) / 1000 / 60  // 분

    if (time < 60) {
        return parseInt(time) + "분 전"
    }
    time = time / 60  // 시간
    if (time < 24) {
        return parseInt(time) + "시간 전"
    }
    time = time / 24
    if (time < 7) {
        return parseInt(time) + "일 전"
    }
    return `${date.getFullYear()}년 ${date.getMonth() + 1}월 ${date.getDate()}일`
}

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

function deleteCard(post_id) {
    let id_value = post_id;

    $.ajax({
        type: "DELETE",
        url: "/deleteCard",
        data: {
            id_value_give: id_value
        },
        success: function (response) {
            alert(response["msg"]);
            window.location.reload()
        }
    });
}

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