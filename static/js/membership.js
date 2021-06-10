function sign_up() {
    let username = $("#username").val();
    let userid = $("#userid").val();
    let userpw = $("#userpw").val();
    let userpw2 = $("#userpw2").val();

    $.ajax({
        type: "POST",
        url: "/sign_up/save",
        data: {
            username_give: username,
            userid_give: userid,
            userpw_give: userpw
        },
        success: function (response) {
            alert("회원가입되었습니다.");
            window.location.replace("/")
        }
    });
}