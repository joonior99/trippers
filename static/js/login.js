function sign_in() {
    let userid = $("#userid").val();
    let userpw = $("#userpw").val();
    console.log(userid, userpw);

    if (userid == "") {
        alert("아이디를 입력하세요.");
        $("#userid").focus();
        return;
    }
    if (userpw == "") {
        alert("비밀번호를 입력하세요.");
        $("#userpw").focus();
        return;
    }

    $.ajax({
        type: "POST",
        url: "/sign_in",
        data: {
            userid_give: userid,
            userpw_give: userpw
        },
        success: function (response) {
            if (response["result"] == "success") {
                $.cookie("mytoken", response["token"], {path: "/"});
                username = response["username"];
                alert(`${username}님 환영합니다.`);
                window.location.replace("/");
            } else {
                alert(response["msg"]);
            }
        }
    });
}