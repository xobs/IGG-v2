function displayModal(e,title,url)
{
    $("#modalHeading").text(title);
    $("#modalBody").load(url);
    $('#modal').modal('show');
    e.preventDefault();
    e.stopPropagation();
}
function justDisplayModal(title,url)
{
    $("#modalHeading").text(title);
    $("#modalBody").load(url);
    $('#modal').modal('show');
    return false;
}
function justDisplayModalHTML(title,html)
{
    $("#modalHeading").text(title);
    $("#modalBody").html(html);
    $('#modal').modal('show');
    return false;
}
function hideModal()
{
  $('#modal').modal('hide');
}
function pad2(x)
{
    return (x < 10 ? '0' : '') + x;
}
$("a[data-toggle=modal]").click(function (e) {
    displayModal(e, $(this).attr('title'), $(this).attr('href'));
})

/* http://www.mredkj.com/javascript/nfbasic.html */
function addCommas(nStr) {
  nStr += '';
  x = nStr.split('.');
  x1 = x[0];
  x2 = x.length > 1 ? '.' + x[1] : '';
  var rgx = /(\d+)(\d{3})/;
  while (rgx.test(x1)) {
    x1 = x1.replace(rgx, '$1' + ',' + '$2');
  }
  return x1 + x2;
}

/* http://stackoverflow.com/a/9695058 */
function removeAllButLast(string, token) {
  if (string.indexOf(token) === -1) {
    return string + token + '00'
  }
  var parts = string.split(token),
      front = parts.slice(0,-1).join(''),
      back  = parts.slice(-1).join('')
  if (front.length == 0) {
    front = "0"
  }
  if (back.length > 2) {
    back = back.slice(0,2)
  }
  while (back.length < 2) {
    back += "0"
  }
  return front + token + back
}

/* https://docs.djangoproject.com/en/1.4/ref/contrib/csrf/#ajax */
jQuery(document).ajaxSend(function(event, xhr, settings) {
  function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
      var cookies = document.cookie.split(';');
      for (var i = 0; i < cookies.length; i++) {
        var cookie = jQuery.trim(cookies[i]);
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) == (name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }
  function sameOrigin(url) {
    // url could be relative or scheme relative or absolute
    var host = document.location.host; // host + port
    var protocol = document.location.protocol;
    var sr_origin = '//' + host;
    var origin = protocol + sr_origin;
    // Allow absolute or scheme relative URLs to same origin
    return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
      (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
      // or any other URL that isn't scheme relative or absolute i.e relative.
      !(/^(\/\/|http:|https:).*/.test(url));
  }
  function safeMethod(method) {
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
  }

  if (!safeMethod(settings.type) && sameOrigin(settings.url)) {
    xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
  }
});

/* local storage fun stuff! */
function lsSave(key, value) {
  if (typeof(localStorage) == 'undefined' ) {
    return false;
  } else {
    try {
      localStorage.setItem(key, value)
    } catch (e) {}
  }
}
function lsGet(key) {
  if (typeof(localStorage) == 'undefined' ) {
    return false;
  } else {
    try {
      localStorage.getItem(key)
    } catch (e) {}
  }
}
function lsDelete(key) {
  if (typeof(localStorage) == 'undefined' ) {
    return false;
  } else {
    try {
      localStorage.removeItem(key)
    } catch (e) {}
  }
}
function updateMarathonInfo() {
  $.getJSON('/ajax/info/', function(data){
    console.log(data)
    $("#infobox_total").html("$" + data.total.toFixed(2))
    $("#infobox_hours").html(data.hours + " hrs")
    setTimeout(function() { updateMarathonInfo() }, 10000); // call thyn self every 10 seconds
  })
}
updateMarathonInfo()