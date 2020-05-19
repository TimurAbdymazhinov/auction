$("#id_category").change(function () {
    var url = $("#checkout-form").attr("data-subcategories-url");
    var categoryId = $(this).val();

    $.ajax({
        url: url,
        data: {
            'category': categoryId
        },
        success: function (data) {
            $("#id_subcategory").html(data);
        }
    });
});


function sortLot(type, id, ss) {

    sel = document.getElementById('sort_select');
    by = sel.options[sel.selectedIndex].value
    urls = document.getElementById('url_sort').value;


    $.ajax({
        url: urls,
        data: {
            'type': type,
            'id': id,
            'by': by,
            'ss': ss

        },
        success: function (data) {
            $("#main_row").html(data);
        }
    });


}


function loginAjax() {
    urls = '/user/accounts/login/'

    $.ajax({
        url: urls,

        data: {},
        success: function (data) {

            $("#login_form_content").html(data);
        }
    });


}

// $(document).ready(function () {
//     $("#login_form").submit(function (event) {
//
//         event.preventDefault(); //prevent default action
//         alert('wer')
//         //
//         // var post_url = $(this).attr("action");
//         // var request_method = $(this).attr("method");
//         // var form_data = $(this).serialize();
//         //
//         // $.ajax({
//         // 	url : post_url,
//         // 	type: request_method,
//         // 	data : form_data
//         // }).done(function(response){ //
//         // 	$("#login_form_content").html(response);
//         // });
//     })
// });

function submitLoginAjax() {

    form = $("#login_form")


    var post_url = form.attr("action");
    var request_method = form.attr("method");
    var form_data = form.serialize();


    $.ajax({
        url: post_url,
        type: request_method,
        data: form_data
    }).done(function (response) { //

        if (response.includes("html")) {

            location.reload();

        } else
            $("#login_form_content").html(response);


    });


}


function registerAjax() {
    urls = '/user/accounts/registration/'

    $.ajax({
        url: urls,

        data: {},
        success: function (data) {

            $("#login_form_content").html(data);
        }
    });


}

function addFavorite(id) {
    urls = '/auctions/favorite/'

    $.ajax({
        url: urls,

        data: {
            'id': id,
        },
        success: function (data) {

            alert('успешно добавлено в избранные')
        }
    });


}

function deleteFavorite(id) {
    urls = '/auctions/fdelete/'

    $.ajax({
        url: urls,

        data: {
            'id': id,
        },
        success: function (data) {

            alert('успешно добавлено удалена')
            location.reload();
        }
    });


}

