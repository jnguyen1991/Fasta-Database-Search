// this function executes our search via an AJAX call
//javscript for the search portion
function runSearch( term ) {
    // hide and clear the previous results, if any
    $('#results').hide();
    $('tbody').empty();
    
    // transforms all the form parameters into a string we can send to the server
    var frmStr = $('#fasta_search').serialize();
    $.ajax({
        url: './search_product.cgi',
        dataType: 'json',
        data: frmStr,
        success: function(data, textStatus, jqXHR) {
            processJSON(data);
        },
        error: function(jqXHR, textStatus, errorThrown){
            alert("Failed to perform gene search! textStatus: (" + textStatus +
                  ") and errorThrown: (" + errorThrown + ")");
        }
    });
}

// this function executes our search via an AJAX call
//javascript for the entry portion
//acts the same as search, but a uses a different CGI
//that processes data first, enters, then displays
//as if you searched that term to confirm entry
function enterSearch( term ) {
    // hide and clear the previous results, if any
    $('#results').hide();
    $('tbody').empty();
    
    // transforms all the form parameters into a string we can send to the server
    var frmStr = $('#fasta_entry').serialize();
    $.ajax({
        url: './enter_product.cgi',
        dataType: 'json',
        data: frmStr,
        success: function(data, textStatus, jqXHR) {
            processJSON(data);
        },
        error: function(jqXHR, textStatus, errorThrown, data){
            alert("Failed to perform gene search! textStatus: (" + textStatus +
                  ") and errorThrown: (" + errorThrown + ")" + data);
        }
    });
}


// this processes a passed JSON structure representing gene matches and draws it
//  to the result table
function processJSON( data ) {
    // set the span that lists the match count
    $('#match_count').text( data.match_count );
    
    // this will be used to keep track of row identifiers
    var next_row_num = 1;
    
    // iterate over each match and add a row to the result table for each
    $.each( data.matches, function(i, item) {
        var this_row_id = 'result_row_' + next_row_num++;
        // create a row and append it to the body of the table
        $('<tr/>', { "id" : this_row_id } ).appendTo('tbody');
        
        // add the locus column
        $('<td/>', { "text" : item.fasta_id } ).appendTo('#' + this_row_id);//*/

        // add the locus column
        $('<td/>', { "text" : item.a } ).appendTo('#' + this_row_id);//*/

        // add the locus column
        $('<td/>', { "text" : item.g } ).appendTo('#' + this_row_id);//*/

        // add the locus column
        $('<td/>', { "text" : item.c } ).appendTo('#' + this_row_id);//*/

        // add the locus column
        $('<td/>', { "text" : item.t } ).appendTo('#' + this_row_id);//*/

        // add the locus column
        $('<td/>', { "text" : item.gc } ).appendTo('#' + this_row_id);//*/

        // add the locus column
        $('<td/>', { "text" : item.pur } ).appendTo('#' + this_row_id);//*/

        // add the locus column
        $('<td/>', { "text" : item.pyr } ).appendTo('#' + this_row_id);//*/

        // add the locus column
        $('<td/>', { "text" : item.Length } ).appendTo('#' + this_row_id);//*/

        // add the locus column
        $('<td/>', { "text" : item.date } ).appendTo('#' + this_row_id);//*/
        

    });
    
    // now show the result section that was previously hidden
    $('#results').show();
}






// run our javascript once the page is ready
$(document).ready( function() {
    // define what should happen when a user clicks submit on our search form
    $('#submit').click( function() {
        runSearch();
        return false;  // prevents 'normal' form submission
    });
    $('#submit_entry').click( function() {
        enterSearch();
        return false;  // prevents 'normal' form submission
    });
});
