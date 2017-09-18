function get_default(url, callback){
  $.getJSON(url, function (data){
    let dado = data;
  })
  .done(callback)
  .fail(function() {
    console.log("GET Failed.");
  })
};

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
        { title: "Menor Lance" },
        {title: "Inicio"},
        { title: "Fim"}
    ]
  });
get_default('/get_lic', fill_lic)
}
function fill_lic(data){
  for(result in data){
      x = data[result]
      prod = "Nome \n  Qtd  <br>"
      for(f in x.products){
        console.log(f)
        prod = prod + x.products[f].product_name
        prod = prod + x.products[f].quantity + "<br>"

    }

      window.tableLic.row.add(
      [x.id, x.applicant, prod, x.value,x.start_date, x.end_date])
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
        console.log(f)
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
});
