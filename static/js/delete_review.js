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