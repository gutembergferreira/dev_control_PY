$(document).ready(function() {
    $('#tableAllDevices').on( 'draw.dt', function () {
        //console.log( 'Redraw occurred at: '+new Date().getTime() );
        document.getElementById('loader-container').style.display = 'none';
    } );
    $('#tableAllDevices').DataTable( {
        responsive: {
            details: {
                display: $.fn.dataTable.Responsive.display.modal( {
                    header: function ( row ) {
                        var data = row.data();
                        return '<h3>Details of |'+data[0]+'| '+data[3] + ' - ' + data[5] + '</h3>';
                    }
                } ),
                renderer: $.fn.dataTable.Responsive.renderer.tableAll( {
                    tableClass: 'table'
                } )
            }
        }
    });
} );
$(document).ready(function() {
    $('#tableDevices').on( 'draw.dt', function () {
        //console.log( 'Redraw occurred at: '+new Date().getTime() );
        document.getElementById('loader-container').style.display = 'none';
    } );
    $('#tableDevices').DataTable( {
        responsive: {
            details: {
                display: $.fn.dataTable.Responsive.display.modal( {
                    header: function ( row ) {
                        var data = row.data();
                        return '<h3>Details of |'+data[0]+'| '+data[3] + ' - ' + data[5] + '</h3>';
                    }
                } ),
                renderer: $.fn.dataTable.Responsive.renderer.tableAll( {
                    tableClass: 'table'
                } )
            }
        }
    });
} );

$(document).ready(function() {
    $('#tableSimCards').on( 'draw.dt', function () {
        //console.log( 'Redraw occurred at: '+new Date().getTime() );
        document.getElementById('loader-container').style.display = 'none';
    } );
    $('#tableSimCards').DataTable( {
        responsive: {
            details: {
                display: $.fn.dataTable.Responsive.display.modal( {
                    header: function ( row ) {
                        var data = row.data();
                        return '<h3>Details of |'+data[0]+'| '+data[3] + ' - ' + data[5] + '</h3>';
                    }
                } ),
                renderer: $.fn.dataTable.Responsive.renderer.tableAll( {
                    tableClass: 'table'
                } )
            }
        }
    });
} );

$(document).ready(function() {
    $('#tableAccessories').on( 'draw.dt', function () {
        //console.log( 'Redraw occurred at: '+new Date().getTime() );
        document.getElementById('loader-container').style.display = 'none';
    } );
    $('#tableAccessories').DataTable( {
        responsive: {
            details: {
                display: $.fn.dataTable.Responsive.display.modal( {
                    header: function ( row ) {
                        var data = row.data();
                        return '<h3>Details of |'+data[0]+'| '+data[3] + ' - ' + data[5] + '</h3>';
                    }
                } ),
                renderer: $.fn.dataTable.Responsive.renderer.tableAll( {
                    tableClass: 'table'
                } )
            }
        }
    });
} );
$(document).ready(function() {
    $('#allHistoryTransaction').on( 'draw.dt', function () {
        document.getElementById('loader-container').style.display = 'none';
    } );
    $('#allHistoryTransaction').DataTable({
        "order": [[0, "desc"]]
    });
} );

$(document).ready(function() {
    $('#tableLoanTransaction').on( 'draw.dt', function () {
        document.getElementById('loader-container').style.display = 'none';

    } );
    $('#tableLoanTransaction').DataTable({
        "order": [[0, "desc"]]
    });;
} );

$(document).ready(function() {
    $('#tableDevolutionTransaction').on( 'draw.dt', function () {
        //console.log( 'Redraw occurred at: '+new Date().getTime() );
        document.getElementById('loader-container').style.display = 'none';

    } );
    $('#tableDevolutionTransaction').DataTable({
        "order": [[0, "desc"]]
    });;

    $('#tableUsers').DataTable();
} );

$(document).ready(function() {
    $('#tableTransferTransaction').on( 'draw.dt', function () {
        //console.log( 'Redraw occurred at: '+new Date().getTime() );
        document.getElementById('loader-container').style.display = 'none';

    } );
    $('#tableTransferTransaction').DataTable({
        "order": [[0, "desc"]]
    });;
} );