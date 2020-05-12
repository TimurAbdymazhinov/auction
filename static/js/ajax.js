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
            'ss':ss

        },
        success: function (data) {
            $("#main_row").html(data);
        }
    });


}

