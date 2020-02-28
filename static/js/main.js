(function () {
  var regalo = document.getElementById('regalo');
  document.addEventListener('DOMContentLoaded', function(){
    //DATOS USUARIOS
    var nombre = document.getElementById('nombre');
    var apellido_paterno = document.getElementById('apellido_paterno');
    var apellido_materno = document.getElementById('apellido_materno');
    var email = document.getElementById('email');

    //CAMPOS PASES
    var pase_dia = document.getElementById('pase_dia');
    var pase_dosdias = document.getElementById('pase_dosdias');
    var pase_completo = document.getElementById('pase_completo');
    //BOTONES Y DIVS

    var calcular = document.getElementById('calcular');
    var errorDiv = document.getElementById('error');
    var btnRegistro = document.getElementById('btnRegistro');
    var lista_productos = document.getElementById('lista-productos');
    var suma = document.getElementById('suma-total');

    //Extras
    var etiquetas = document.getElementById('etiquetas');
    var camisas = document.getElementById('camisa_evento');

    btnRegistro.disable = true;


    if(document.getElementById('calcular')){



    calcular.addEventListener('click',calcularMontos);

    pase_dia.addEventListener('blur', mostrarDias);

    pase_dosdias.addEventListener('blur', mostrarDias);

    pase_completo.addEventListener('blur', mostrarDias);

    nombre.addEventListener('blur', validarCampos);
    apellido_paterno.addEventListener('blur', validarCampos);
    apellido_materno.addEventListener('blur', validarCampos);
    email.addEventListener('blur', validarMail);

    function validarCampos() {
      if(this.value == ''){
        errorDiv.style.display = 'block';
        errorDiv.innerHTML = "esta campo es obligatorio";
        this.style.border = '1px solid red';
        errorDiv.style.border = '1px solid red';
      } else {
        errorDiv.style.display = 'none';
        this.style.border = '1px solid #cccccc';
      }
    }

    function validarMail() {
      if (this.value.indexOf("@") > -1) {
        errorDiv.style.display = 'none';
        this.style.border = '1px solid #cccccc';

      } else {
        errorDiv.style.display = 'block';
        errorDiv.innerHTML = "Dede de tener un @";
        this.style.border = '1px solid red';
        errorDiv.style.border = '1px solid red';

      }

    }


    function calcularMontos(event) {
      event.preventDefault();
      if (regalo.value === '') {
        alert("Debes de elegir un regalo");
        regalo.focus();
      } else {
        var boletosDia = parseInt(pase_dia.value, 10) || 0,
            boletos2Dias = parseInt(pase_dosdias.value, 10) || 0,
            boletoCompleto = parseInt(pase_completo.value, 10) || 0,
            cantCamisas = parseInt(camisas.value, 10) || 0,
            cantEtiquetas = parseInt(etiquetas.value, 10) || 0;

        var totalPagar = (boletosDia * 30) + (boletos2Dias * 45) + (boletoCompleto * 50) + ((cantCamisas * 100) *.93) + (cantEtiquetas * 2);

        var listadoProductos = [];

        if (boletosDia >= 1) {
          listadoProductos.push(boletosDia + ' Pases Por Dia');

        }
        if (boletos2Dias >= 1) {
          listadoProductos.push(boletos2Dias + ' Pases Por  2 Dias');

        }
        if (boletoCompleto >= 1) {
          listadoProductos.push(boletoCompleto + ' Pases Completos');

        }
        if (cantCamisas >= 1) {
          listadoProductos.push(cantCamisas + ' Cantidad de Camisas');

        }
        if (cantEtiquetas >= 1) {
          listadoProductos.push(cantEtiquetas + ' Cantidad de Etiquetas');

        }

        lista_productos.style.display = "block";
        lista_productos.innerHTML = '';
        for (var i = 0; i < listadoProductos.length; i++) {
          lista_productos.innerHTML += listadoProductos[i] + '<br/>';
        }
        suma.innerHTML = "$" + totalPagar.toFixed(2);
        btnRegistro.disable=false;
        document.getElementById('total_pagado').value=total_pagado
        }
    }

 function mostrarDias() {

      var boletosDia = parseInt(pase_dia.value, 10) || 0,
          boletos2Dias = parseInt(pase_dosdias.value, 10) || 0,
          boletoCompleto = parseInt(pase_completo.value, 10) || 0;

      var diasElegidos = [];

      if (boletosDia > 0) {
        diasElegidos.push('viernes');
      }
      if (boletos2Dias > 0) {
        diasElegidos.push('viernes','sabado');

      }
      if (boletoCompleto > 0) {
        diasElegidos.push('viernes','sabado','domingo');

      }
      for (var i = 0; i < diasElegidos.length; i++) {
        document.getElementById(diasElegidos[i]).style.display='block';
      }




    }
  }

  });//CARGANDO DOM content
  $(function(){

//MENU FIJO
var windowHeight = $(window).height();
var barraAltura = $('.barra').innerHeight();



$(window).scroll(function(){
  var scroll = $(window).scrollTop();
  if (scroll > windowHeight) {
    $('.barra').addClass('fixed');
    $('body').css({'margin-top': barraAltura+'px'});
    console.log("LA VAS A MATAR PERRO");
  } else {
    $('.barra').removeClass('fixed');
    $('body').css({'margin-top': '0px'});
    console.log("TAN POCO :V dale dale xddxxdxd");
  }


});

//MENU PA TODOS XD

$('.menu-movil').on('click', function(){
  $('.navegacion-principal').slideToggle();
});

  $('.programa-evento .info-curso:first').show();
   $('.menu-programa a:first').addClass('activo');

   $('.menu-programa a').on('click', function(){

     $('.menu-programa a').removeClass('activo');
     $(this).addClass('activo');
     $('.ocultar').fadeOut(1000);
     var enlace = $(this).attr('href');
     $(enlace).fadeIn(1000);
     return false;
      });

      //ANIMACIONES PAPU

      var resumenLista = jQuery('.resumen-evento');
      if (resumenLista.length > 0) {
        $('.resumen-evento').waypoint(function(){
          $('.resumen-evento li:nth-child(1) p').animateNumber({ number: 6}, 1200);
          $('.resumen-evento li:nth-child(2) p').animateNumber({ number: 36}, 1200);
          $('.resumen-evento li:nth-child(3) p').animateNumber({ number: 46}, 1500);
          $('.resumen-evento li:nth-child(4) p').animateNumber({ number: 46}, 1500);

        }, {
          offset: '50%'
        });
      }

$('.cuenta-regresiva').countdown('2019/09/14 09:00:00', function(event){
  $('#dias').html(event.strftime('%D'));
  $('#horas').html(event.strftime('%H'));
  $('#minutos').html(event.strftime('%M'));
  $('#segundos').html(event.strftime('%S'));
  });

});

})();
