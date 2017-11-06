function get_default(url, callback){
  $.getJSON(url, function (data){
    let dado = data;
  })
  .done(callback)
  .fail(function() {
    console.log("GET Failed.");
  })
};

function post_default(url, data){
jdata = JSON.stringify(data)
var settings = {
"async": true,
"crossDomain": true,
"url": url,
"method": "POST",
"headers": {
  "authorization": "Basic MzAxOjEyMjA=",
  "content-type": "application/json",
  "cache-control": "no-cache",
  "postman-token": "2b5081fd-cf21-5c84-c177-e914fe46d763"
},
"processData": false,
"data": jdata
}

$.ajax(settings).done(function (response) {
});
}

function make_lic_table(){
  window.tableLic = $('#table-lic').DataTable({
    paging: true,
    searching: true,
    order: [[0, 'desc']],
    buttons: ['copy', 'excel', 'pdf'],
    columns: [
        {title: "ID"},
        { title: "Requerente" },
        { title: "Produtos" },
        {title: "Fornecedor Atual"},
        { title: "Menor Lance" },
        {title: "Inicio"},
        { title: "Fim"},
        { title: "Lance",defaultContent: "<a href='' name='dar_lance' class='show' data-target='#novo-lance'> <i class = 'fa fa-paper-plane-o' style='color:#696969' ></i> </a> ",width: 1 },
    ]
  });
get_default('/get_lic', fill_lic)
}
function fill_lic(data){
    window.tableLic.rows().remove().draw();
  for(result in data){
      x = data[result]
      prod = ""
      for(f in x.products){
        prod = prod + x.products[f].product_name
        prod = prod +" x " +  x.products[f].quantity + "<br>"

    }
      window.tableLic.row.add(
      [x.id, x.applicant, prod, x.lowestBid.supplier ,x.lowestBid.value ,x.start_date, x.end_date])
      window.tableLic.draw()
    }
  }

function make_fab_table(){
    window.tableFab = $('#table-fab').DataTable({
      paging: true,
      searching: true,
      order: [[0, 'desc']],
      buttons: ['copy', 'excel', 'pdf'],
      columns: [
          { title: "ID" },
          { title: "Nome" },
          {title: "Produtos"}
      // { title: "Produtos",defaultContent: "<a href='' name='ver_resultados' class='show'> <i class = 'fa fa-eye fa-4' style='color:#696969' ></i> </a> ",width: 1 },
       //   { title: "produtos_html", "visible":false}
      ]
    });
  get_default('/get_fab', fill_fab)
  }

function fill_fab(data){
  for(result in data){
    x = data[result]
    prod = "[Nome     Valor]  <br>"
    for(f in x.produtos){
        prod = prod + x.produtos[f].nome + "\n"
        prod = prod + x.produtos[f].custo + "<br>"

    }
    window.tableFab.row.add(
      [x.id, x.nome,prod]
    )
    window.tableFab.draw()
  }
}

$(function() {

    $('#side-menu').metisMenu();

});

//Loads the correct sidebar on window load,
//collapses the sidebar on window resize.
// Sets the min-height of #page-wrapper to window size
$(function() {

    make_lic_table()
    make_fab_table()

    window.tableFab.on('click','a.show', function(e){
         e.preventDefault()
         var data = window.tableFab.row( $(this).parents('tr') ).data();
         console.log(data)
       })

       window.tableLic.on('click','a.show', function(e){
            e.preventDefault()
            var data = window.tableLic.row( $(this).parents('tr') ).data();
            console.log(data)
            $("#idlic").val(data[0])
            $("#data").val("")
            $("#idforn").val("")
            $("#valor").val("")

            $("#novo-lance").modal("show")
      })

    $(window).bind("load resize", function() {
        topOffset = 50;
        width = (this.window.innerWidth > 0) ? this.window.innerWidth : this.screen.width;
        if (width < 768) {
            $('div.navbar-collapse').addClass('collapse');
            topOffset = 100; // 2-row-menu
        } else {
            $('div.navbar-collapse').removeClass('collapse');
        }

        height = ((this.window.innerHeight > 0) ? this.window.innerHeight : this.screen.height) - 1;
        height = height - topOffset;
        if (height < 1) height = 1;
        if (height > topOffset) {
            $("#page-wrapper").css("min-height", (height) + "px");
        }
    });

    var url = window.location;
    var element = $('ul.nav a').filter(function() {
        return this.href == url || url.href.indexOf(this.href) == 0;
    }).addClass('active').parent().parent().addClass('in').parent();
    if (element.is('li')) {
        element.addClass('active');
    }


    $( "#savebid" ).click(function() {
        lic = $("#idlic").val()
        forn = $("#idforn").val()
        valor = $("#valor").val()
        data = $("#data").val()
        data = data.split('-')
        data = data[2] + "/" + data[1] + "/" + data[0]
        if (lic && forn && valor && $("#data").val() ){
            jsn = {}
            jsn['bidding'] = lic
            jsn['date'] = data
            jsn['supplier'] = forn
            jsn['value'] = valor

            post_default('/send_bid', jsn);
            $("#novo-lance").modal("hide");
            get_default('/get_lic', fill_lic)


        }
        });
});
