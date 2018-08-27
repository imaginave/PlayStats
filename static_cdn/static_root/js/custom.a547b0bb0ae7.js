var currAccNum = '' // name of header
var results = 0 // sum for header
var after_rake = 0
var win = 0
var turnover = 0

var headerIdx //= $('tr[account]') //initial to prevent first zero row insertion
$(document).ready(function() {


  $('.mydatepicker').datepicker({
    format: "mm/dd/yyyy",
    todayBtn: "linked",
    autoclose: true
  });

  /*$('table.table thead tr th').each(function() { //override default ordering
    $( this ).replaceWith( "<th>" + $( this ).text() + "</th>" );
  });*/

  var lastRow = $('tr[name]:last')
  $('tr[name]').each(function() { //get each row
    if (currAccNum != $(this).attr("name")) { //new account encounterd
      var newRow = $('<tr header = "' + currAccNum + '" display="hide"><td>' + currAccNum + '<span class="sign"></span></td><td></td>'+
        '<td>'+ results.toFixed(2) + '</td>'+
        '<td>'+ after_rake.toFixed(2) + '</td>'+
        '<td>'+ win.toFixed(2) + '</td>'+
        '<td>'+ turnover.toFixed(2) + '</td>'+
        '</tr>');
      newRow.insertBefore($('table.table tbody tr:nth(' + headerIdx + ')')); //insert header in the beginning of account`s rows
      headerIdx = $(this).index() //save new index for future header
      currAccNum = $(this).attr("name") //get new accnumber
      results = 0
      after_rake = 0
      win = 0
      turnover = 0
      results = results + parseFloat($(this).children(".results").text()); //count sum
      after_rake = after_rake + parseFloat($(this).children(".after_rake").text()); //count sum
      win = win + parseFloat($(this).children(".win").text()); //count sum
      turnover = turnover + parseFloat($(this).children(".turnover").text()); //count sum
      if ($(this).is(lastRow)) { //if last row in table - one for header
        results = 0
        console.log($(this))
        results = results + parseFloat($(this).children(".results").text());
        after_rake = after_rake + parseFloat($(this).children(".after_rake").text()); //count sum
        win = win + parseFloat($(this).children(".win").text()); //count sum
        turnover = turnover + parseFloat($(this).children(".turnover").text()); //count sum
        console.log(results)
        var newRow = $('<tr header = "' + currAccNum + '" display="hide"><td>' + currAccNum + '<span class="sign"></span></td><td></td>'+
        '<td>'+ results.toFixed(2) + '</td>'+
        '<td>'+ after_rake.toFixed(2) + '</td>'+
        '<td>'+ win.toFixed(2) + '</td>'+
        '<td>'+ turnover.toFixed(2) + '</td>'+
        '</tr>');
        newRow.insertBefore($('table.table tbody tr:nth(' + headerIdx + ')'));
        return false
      };
    } else if ($(this).is(lastRow)) { //last row in table for headers with several records
        console.log($(this))
        results = results + parseFloat($(this).children(".results").text());
        after_rake = after_rake + parseFloat($(this).children(".after_rake").text()); //count sum
        win = win + parseFloat($(this).children(".win").text()); //count sum
        turnover = turnover + parseFloat($(this).children(".turnover").text()); //count sum
        console.log(results)
        var newRow = $('<tr header = "' + currAccNum + '" display="hide"><td>' + currAccNum + '<span class="sign"></span></td><td></td>'+
        '<td>'+ results.toFixed(2) + '</td>'+
        '<td>'+ after_rake.toFixed(2) + '</td>'+
        '<td>'+ win.toFixed(2) + '</td>'+
        '<td>'+ turnover.toFixed(2) + '</td>'+
        '</tr>');
        newRow.insertBefore($('table.table tbody tr:nth(' + headerIdx + ')'));
    } else { // rows of the same header
      results = results + parseFloat($(this).children(".results").text());
      after_rake = after_rake + parseFloat($(this).children(".after_rake").text()); //count sum
      win = win + parseFloat($(this).children(".win").text()); //count sum
      turnover = turnover + parseFloat($(this).children(".turnover").text()); //count sum
    }
  });


  $(function() {
    $('tr[name]').hide();
    $("table").click(function(event) {
      event.stopPropagation();
      var $target = $(event.target);
      var currAccAttr = $target.closest("tr").attr("header")
      var displayAttr = $target.parent().attr("display")
      console.log($target.parent().attr("display"))
      if (displayAttr == "hide") {
        $target.parent().attr("display","show")
      } else {
        $target.parent().attr("display","hide")
      }
      $('tr[name=' + currAccAttr + ']').each(function() {
        $(this).slideToggle();
      });
    });
  });

  //shotcut dates

  function put_date(date_diff) {
      $from = new Date();
      $to = new Date($from);
      $from.setDate($to.getDate() - date_diff); 
      
      var $date_string_min = ($from.getMonth() + 1) + '/' + $from.getDate() + '/' +  $from.getFullYear()
      var $date_string_max = ($to.getMonth() + 1) + '/' + $to.getDate() + '/' +  $to.getFullYear()

      $("input[name='date_min']").val($date_string_min)
      $("input[name='date_max']").val($date_string_max)

      return 1;
  }

  $('.pick_today').click( function(event) {
    var o = put_date(1)
  });

  $('.pick_week').click( function(event) {
    var o = put_date(7)
  });

  $('.pick_month').click( function(event) {
    var o = put_date(30)
  });


});



