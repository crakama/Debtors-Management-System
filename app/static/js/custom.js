// Bootstrap table - test of `export selected` (to csv) with server side pagination. Created to help answer https://github.com/wenzhixin/bootstrap-table/issues/2220, release 1.10.1 and onwards


$(function() {
  var $table = $('#table');
  $('#toolbar').find('select').change(function() {
    $table.bootstrapTable('refreshOptions', {
      exportDataType: $(this).val()
    });
  });

  $('#getAllSelections').click(function(e) {
    e.preventDefault();
    var selectedData = $table.bootstrapTable('getAllSelections');
    console.log('selectedData',selectedData);
    $table.bootstrapTable('load',selectedData);
  });

});
function queryParams() {
    return {
        type: 'owner',
        sort: 'updated',
        direction: 'desc',
        per_page: 100,
        page: 1
    };
}
