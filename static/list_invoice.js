$(document).ready(function () {

    $(document).on('click','.cancel_invoice', function(){
      id = this.id
      alert = null;
      $.ajax({
        url:"{% url 'cancel_invoice' %}",
        data:{'pk_invoice': id},
        success: function(e){
          if(JSON.parse(e).result){
            $(".state"+id).text("Factura Anulada")
            $(".total"+id).text('$0')
            alert = "EXITOSO"
          }
          else{
            alert = "ERROR"
          }
          var text = JSON.parse(e).message;
          var notification = new Notification(alert, {
            body: text,
            icon: "{% static 'logo.png' %}"
          });
        }
      })
    })

    $(".searchInput").on("input", function() {
      var searchText = $(this).val().toLowerCase();
      $("table tbody tr").each(function() {
        var ccNitText = $(this).find(".date_invoice").text().toLowerCase();
        var razonSocialText = $(this).find(".client").text().toLowerCase();
        if (ccNitText.includes(searchText) || razonSocialText.includes(searchText)) {
          $(this).show();
        } else {
          $(this).hide();
        }
      });
    });

    $(".copy_invoice").click(function(){
      id = this.id
      let params = "scrollbars=no,resizable=no,status=no,location=no,toolbar=no,menubar=no,width=800,height=600,left=100,top=100";
      window.open(url_path + "/order/Print_Invoice/"+id, "invoice", params);
    })

  });