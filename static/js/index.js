var navbar = document.getElementsByClassName("navbar")[0]
    var uls = Array.from(document.getElementsByClassName("navbar-nav"));
    var menu_btn = document.getElementById("menu_btn");
    var menu_toggled = false;
    navbar.classList.add("navbar-fixed-top", "navbar-invisible");

    if (window.innerWidth < 768) {
      menu_btn.style = "display: inline-block;float: right;";
      uls.forEach(i => {i.setAttribute("style", "display: none")});
      navbar.classList.remove("navbar-invisible");
    }

    menu_btn.addEventListener('click', function(){
      if (menu_toggled) {
        uls.forEach(i => {i.setAttribute("style", "display: none")});  
        menu_toggled = false;
      } else {
        uls.forEach(i => {i.setAttribute("style", "display: block")});
        menu_toggled = true;
      }
    });
    
    window.addEventListener('resize', () => {
      if (window.innerWidth < 768 ) {
        menu_btn.style = "display: inline-block;float: right;" ;
        uls.forEach(i => {i.setAttribute("style", "display: none")});
        navbar.classList.remove("navbar-invisible");
      } else {
        menu_btn.style = "display: none;" ;
        navbar.setAttribute("style", "display: block");
        uls.forEach(i => {i.setAttribute("style", "display: block")});
      }
    })
    window.addEventListener('scroll', () => {
      var scrolled = window.pageYOffset || document.documentElement.scrollTop;
      if (window.innerWidth > 768) {
        if(scrolled > 0) {
          navbar.classList.remove("navbar-invisible");
        } else {
          navbar.classList.add("navbar-invisible",);
        }
      }
    })