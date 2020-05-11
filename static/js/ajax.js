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

